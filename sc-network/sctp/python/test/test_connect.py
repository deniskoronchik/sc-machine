import sctp
import unittest
import time

from fixture import TestServer

import sys


class TestServerConnect(TestServer):

  def test_connection_smoke(self):
    client = sctp.Client()
    client.connect('127.0.0.1', 55770)
    time.sleep(1)
    client.disconnect()
