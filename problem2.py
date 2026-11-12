from problem1 import string_to_char_dict
def is_unique(string):
  """
  string-> boolean
  using string_to_char_dict, checks to see if a string has all unique characters
  
  >>> is_unique("aaaa")
  False
  >>> is_unique("abce")
  True
  >>> is_unique("lmnop")
  True
  >>> is_unique("ooma")
  False
  """
  result= string_to_char_dict(string)
  for i in result:
    if result[i] >1:
      return False
  return True
