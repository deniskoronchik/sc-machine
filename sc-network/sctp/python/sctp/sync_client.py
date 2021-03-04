import asyncio
import logging
from .async_client import AsyncClient


class Client:

  def __init__(self):
    self.client = AsyncClient()
    self.event_loop = asyncio.get_event_loop()

  def connect(self, host, port):
    """Connect to server
    Args:
      host (str): Host server address
      port (int): Port number
    """
    self.event_loop.create_task(self.client.connect(host, port))

  def disconnect(self):
    """Disconnect client from server
    """
    self.event_loop.run_until_complete(self.client.disconnect())
