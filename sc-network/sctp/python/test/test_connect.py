import sctp
import unittest
import time

from fixture import TestServer

import sys


class TestServerConnect(TestServer):

  def test_connection_smoke(self):
    client = sctp.Client()
    self.assertTrue(client.connect('127.0.0.1', 55770,
                                   login='user', password='passwd'))
    time.sleep(0.1)
    client.disconnect()

  def test_connection_invalid_login(self):
    client = sctp.Client()
    self.assertFalse(client.connect('127.0.0.1', 55770,
                                    login='non_existing_login', password='passwd'))
    time.sleep(0.1)
    client.disconnect()

  def test_connection_invalid_password(self):
    client = sctp.Client()
    self.assertFalse(client.connect('127.0.0.1', 55770,
                                    login='login', password='non_existing_passwd'))
    time.sleep(0.1)
    client.disconnect()
