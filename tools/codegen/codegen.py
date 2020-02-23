import argparse


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-t', '--target', dest='target', 
    type=str, required=True, help='Project name')
  parser.add_argument('-i', '--input', dest='input',
    type=str, required=True, help='Source path')
  parser.add_argument('-o', '--output', dest='output',
    type=str, required=True, help='Output path for generated headers')
  parser.add_argument('-f', '--flags', dest='flags',
    type=str, required=False, default='',
    help='List of flags that should be passed to compiler')
  parser.add_argument('--debug', dest='debug',
    action='store_true', default=False, help='Display diagnostic messages')
  
  args = parser.parse_args()

