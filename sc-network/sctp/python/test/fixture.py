import os
import subprocess
import unittest

curr_dir = os.path.dirname(os.path.abspath(__file__))
bin_dir = os.path.join(curr_dir, '../../../../bin/')

class TestServer(unittest.TestCase):

  self_run = False
  process = None

  @classmethod
  def setUpClass(self):
    if TestServer.self_run:
      executable = os.path.join(bin_dir, 'sc-server')
      config = os.path.join(bin_dir, 'sc-server.ini')
      TestServer.process = subprocess.Popen([executable, config])

  @classmethod
  def tearDownClass(self):
    if TestServer.process is not None:
      TestServer.process.terminate()