import asyncio
import logging


class AsyncClient:

  def __init__(self):
    self.is_running = False

    self.write_queue = asyncio.Queue()

  async def connect(self, host, port, login, password):
    """Connect to server
    Args:
      host (str): Host server address
      port (int): Port number
      login (str): User login
      password (str): User password
    """
    await self._run(host, port, login, password)

  async def disconnect(self):
    """Disconnect client from server
    """
    self.is_running = False

  async def _run(self, host, port, login, passwd):
    """This function runs whole processing loop
    """
    self.is_running = True

    logging.info("Connecting to {}:{}".format(host, port))
    reader, writer = await asyncio.open_connection(host, port)
    is_connected = reader is not None and writer is not None

    if is_connected:
      logging.info("Connected")
      await asyncio.gather(
          self._read_loop(reader),
          self._write_loop(writer),
          self._do_login(login, passwd))
    else:
      logging.error("Wasn't able to connect")

    if is_connected:
      logging.info("Disconnecting")
      writer.close()
      await writer.wait_closed()

  async def _read_loop(self, reader):
    """This function implements response processing loop
    """
    logging.info("Start read loop")
    while self.is_running:
      pass

  async def _write_loop(self, writer):
    """This function implement request processing loop
    """
    logging.info("Start write loop")
    while self.is_running:

      if not self.write_queue.empty():
        req = await self.write_queue.get()

        writer.write(req.data)
        await writer.drain()
      else:
        await asyncio.sleep(0.001)

  async def _do_request(self, req):
    """Sends common request to the server and waits response
    """
    await self.write_queue.put(req)

  async def _do_login(self, login, passwd):
    logging.info("Trying to login")
    handshake_req = serial.make_handshake_request(login)

    print(handshake_req)
    res = await self._do_request(handshake_req)
