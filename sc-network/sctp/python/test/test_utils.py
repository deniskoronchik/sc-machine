import sctp
import unittest
import time

from fixture import TestServer

import sys


class TestUtils(TestServer):

  def test_mix_passwd_with_salt(self):
    passwd_hash = "1234567890"
    salt = "qwertyuiop"

    salted = sctp.mix_passwd_with_salt(passwd_hash, salt)

    self.assertEqual(
        salted, "q1w2e3r4t5y6u7i8o9p0")
