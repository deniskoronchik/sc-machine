# -*- coding: utf-8 -*-

import os
import re
import shutil

import cpp_parser as cpp

from jinja2 import Environment, FileSystemLoader
from cpp_parser.tools import clang_init
from termcolor import colored

from typing import List

current_path = os.path.dirname(os.path.abspath(__file__))

class Generator:

  def __init__(self, input_path: str, flags: str, output_path: str, is_debug: bool):
    self.input_path = input_path
    self.output_path = output_path
    self.flags = flags    
    self.is_debug = is_debug
    self.templ_env = Environment(
      loader=FileSystemLoader(os.path.join(current_path, 'templates')),
      lstrip_blocks=True,
      trim_blocks=True)

  def run(self) -> bool:
    parser = cpp.Parser()
    status = parser.parse(
      self.input_path,
      flags=self.flags.split(';'),
      is_debug=self.is_debug
    )
    if not status:
      return False

    if self.shouldGenerate(parser):
      self.generate(parser)

    if self.is_debug:
      parser.print_objects()

    return True

  def generateFileID(self, fileName: str) -> str:
    return re.sub('[^0-9a-zA-Z]+', '_', fileName)

  def generate(self, parser: cpp.Parser):
    fileName = os.path.basename(self.input_path)
    fileID = self.generateFileID(fileName)

    # make output file
    name, ext = os.path.splitext(fileName)
    outputFileName = os.path.join(self.output_path, name + '.generated' + ext)

    template = self.templ_env.get_template('header.hpp.j2')

    content = template.render({
      'fileID': fileID,
      'classes': parser.classes
    })

    file = open(outputFileName, 'w')
    file.write(content)
    file.close()

  def isNativeClass(self, className):
    return className in [
      'ScObject',
      'ScAgent',
      'ScAgentAction',
      'ScModule'
    ]

  def shouldGenerate(self, parser: cpp.Parser) -> bool:
    for c in parser.classes:
      for base in c.base_classes:
        if self.isNativeClass(base):
          return True

    return False


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

    # recreate output directory
    if os.path.isdir(self.params.output):
      shutil.rmtree(self.params.output)
    
    try:
      os.makedirs(self.params.output)
    except:
      pass
    
    files = self.collect_files(self.params.input, extensions)
    index = 1
    for f in files:
      self.log(colored('[{}/{}] Process {} ... '.format(index, len(files), f), 'white'), newline=False)

      generator = Generator(f, 
        flags=self.params.flags,
        output_path=self.params.output,
        is_debug=self.params.is_debug
        )
      status = generator.run()
      
      self.log(colored('✓', 'green') if status else colored('✕', 'red'))

      index += 1
