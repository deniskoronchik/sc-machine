from hashlib import sha256


def mix_passwd_with_salt(passwd_hash, salt):

  assert(len(salt) == len(passwd_hash))
  result = ""
  for i in range(len(salt)):
    result += salt[i]
    result += passwd_hash[i]

  return result
