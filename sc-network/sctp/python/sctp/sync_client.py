import logging
import socket
import struct
import time

from hashlib import sha256

from .request import Request
from .utils import *

import sctp.sctp_pb2 as pb

watermark = ord('s') << 3 | ord('c') << 2 | ord('t') << 1 | ord('p')
max_packet_size = 2 << 31
header_size = 8


class Client:

  def __init__(self):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.events = []
    self.req_id = 0

  def next_request_id(self):
    self.req_id += 1
    return self.req_id

  def connect(self, host, port, login, password) -> bool:
    """Connect to server
    Args:
      host (str): Host server address
      port (int): Port number
      login (str): User login
      password (str): User password
    """
    logging.info("Conencting to {}:{}".format(host, port))
    try:
      self.socket.connect((host, port))
    except ConnectionRefusedError:
      logging.info("Wasn't able to connect")
      return False

    # try to login
    self.send_handshake(login)
    handshake = self.recv_handshake()
    password_hash = sha256(password.encode("ascii")).hexdigest()
    salted = mix_passwd_with_salt(password_hash, handshake.salt)
    salted_hash = sha256(salted.encode("ascii")).hexdigest()

    self.send_auth(salted_hash)
    auth = self.recv_auth()

    if auth.status == pb._AUTHORIZATIONRESPONSE_AUTHSTATUS.values_by_name['Success'].number:
      return True

    return False

  def disconnect(self):
    """Disconnect client from server
    """
    self.events = []
    self.socket.close()

  def _check_response(self, response: pb.Response, field: str):
    if not response.HasField(field):
      raise "Response have no field {}".format(field)

  def _create_request(self) -> pb.Request:
    req = pb.Request()
    req.id = self.next_request_id()
    req.timestamp = int(time.time())
    return req

  def send_handshake(self, login):
    req = self._create_request()
    req.handshake.login = login
    self._send_request(req)

  def recv_handshake(self):
    response = self._read_response()
    self._check_response(response, "handshake")

    return response.handshake

  def send_auth(self, salted_hash):
    req = self._create_request()
    req.auth.hash = salted_hash
    self._send_request(req)

  def recv_auth(self):
    response = self._read_response()
    self._check_response(response, "auth")

    return response.auth

  def _send_request(self, req: pb.Request):
    assert isinstance(req, pb.Request)
    msg = req.SerializeToString()

    packet_header = struct.pack('II', watermark, len(msg))
    self.socket.send(packet_header)

    if len(msg) >= max_packet_size:
      raise RuntimeError("Message is too long")

    self.socket.send(msg)

  def _read_response(self) -> pb.Response:
    # read header
    header_buff = self._read_buffer(header_size)
    packet_watermark, packet_size = struct.unpack('II', header_buff)

    if packet_watermark != watermark:
      raise RuntimeError("Invalid watermark")

    msg = self._read_buffer(packet_size)
    response = pb.Response()

    if not response.ParseFromString(msg):
      raise "Can't parse response"

    return response

  def _read_buffer(self, message_len):
    remain_bytes = message_len
    chunks = []

    while remain_bytes > 0:
      chunk = self.socket.recv(min([remain_bytes, 2048]))
      if chunk == b'':
        raise RuntimeError("socket connection broken")

      remain_bytes -= len(chunk)
      chunks.append(chunk)

    return b''.join(chunks)
