import sctp
import unittest

from fixture import TestServer

class TestServerConnect(TestServer):

  def test_connection_smoke(self):
    client = sctp.client()
    self.assertTrue(client.connect('127.0.0.1', 55770))
    client.disconnect()