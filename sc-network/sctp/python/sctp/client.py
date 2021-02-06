import socket
import logging

class client:

  def __init__(self):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def connect(self, host, port) -> bool:
    try:
      self.socket.connect((host, port))
      return True
    except:
      pass

    return False

  def disconnect(self):
    self.socket.close()