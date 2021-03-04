import asyncio
import logging


class AsyncClient:

  def __init__(self):
    self.is_running = False

  async def connect(self, host, port):
    """Connect to server
    Args:
      host (str): Host server address
      port (int): Port number
    """
    await self._run(host, port)

  async def disconnect(self):
    """Disconnect client from server
    """
    self.is_running = False

  async def _run(self, host, port):
    self.is_running = True

    logging.info("Connecting to {}:{}".format(host, port))
    reader, writer = await asyncio.open_connection(host, port)
    is_connected = reader is not None and writer is not None

    if is_connected:
      logging.info("Connected")
      await asyncio.gather(self._read_loop(reader), self._write_loop(writer))
    else:
      logging.error("Wasn't able to connect")

    if writer is not None:
      logging.info("Disconnecting")
      writer.close()
      await writer.wait_closed()

  async def _read_loop(self, reader):

    while self.is_running:
      pass

  async def _write_loop(self, writer):

    while self.is_running:
      pass
