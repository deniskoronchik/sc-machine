import os

import clang.cindex

from termcolor import colored

search_directories = [
  '/usr/lib/llvm-7/lib',
  '/usr/lib/llvm-6.0/lib'
]

def clang_find():
  clang_dir = None
  for d in search_directories:
    if os.path.isdir(d) and os.path.exists(d):
      clang_dir = d
      break
    
  return clang_dir

def clang_init():
  cl = clang_find()
  if cl:
    print (colored('Found clang: {}'.format(cl), 'green'))
  else:
    print (colored("Can't find clang", 'red'))
    
  clang.cindex.Config.set_library_path(clang_find())
  
