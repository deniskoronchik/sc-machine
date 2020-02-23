import os

search_directories = [
  '/usr/lib/llvm-6.0/lib/'
]

def find():
  clang_dir = None
  for d in search_directories:
    if os.path.isdir(d) and os.path.exists(d):
      clang_dir = d
      break
    
  return clang_dir