
import os
import sys

curr_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(curr_dir, '../'))

from unittest import defaultTestLoader, TestCase, TextTestRunner, TestSuite

from fixture import TestServer
from test_connect import TestServerConnect
from optparse import OptionParser

if __name__ == "__main__":
  
  parser = OptionParser()
  parser.add_option("-e", "--external-server",
                    action="store_false", dest="run_server", default=True,
                    help="Do not run server")

  (options, args) = parser.parse_args()

  TestServer.self_run = options.run_server

  tests = [
    TestServerConnect
  ]

  for testItem in tests:
    suite = defaultTestLoader.loadTestsFromTestCase(testItem)
    res = TextTestRunner(verbosity=2).run(suite)
    if not res.wasSuccessful():
      raise Exception("Unit test failed")
