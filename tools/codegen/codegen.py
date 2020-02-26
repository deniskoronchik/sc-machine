import os

import cpp_parser as cpp

from cpp_parser.tools import clang_init
from termcolor import colored

from typing import List

class Generator:

  def __init__(self, input_path: str, flags: str, output_path: str):
    self.input_path = input_path
    self.output_path = output_path
    self.flags = flags    

  def run(self) -> bool:
    parser = cpp.Parser()
    status = parser.parse(self.input_path, flags=self.flags)
    if not status:
      return False

    # 
    parser.print_objects()

    return True


class Codegen:

  class Params:

    def __init__(self, target: str, input_path: str,
      output: str, flags: str, is_debug: bool):

      self.target = target
      self.input = input_path
      self.output = output
      self.flags = flags
      self.is_debug = is_debug

  def __init__(self, params: Params):
    self.params = params

  def collect_files(self, input_dir, extensions) -> List[str]:
    collected_files = []
    for root, _, files in os.walk(input_dir):
      for f in files:
        file_path = os.path.join(root, f)
        _, ext = os.path.splitext(file_path)

        if ext in extensions and '.generated.' not in file_path:
          collected_files.append(file_path)

    return collected_files

  def log(self, msg, newline=True):
    if self.params.is_debug:
      if newline:
        print(msg)
      else:
        print(msg, end='')

  def process(self, extensions=['.hpp', '.h']):
    
    files = self.collect_files(self.params.input, extensions)
    index = 1
    for f in files:
      self.log(colored('[{}/{}] Process {} ... '.format(index, len(files), f), 'white'), newline=False)

      generator = Generator(f, 
        flags=self.params.flags,
        output_path=self.params.output
        )
      status = generator.run()
      
      self.log(colored('✓', 'green') if status else colored('✕', 'red'))

      index += 1
