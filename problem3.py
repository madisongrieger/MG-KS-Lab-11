from problem1 import string_to_char_dict
def is_permutation(string1, string2):
  """
  string-> boolean
  evaluates if two strings are permutations of eachother 
  
  >>> is_permutation("aaaa", "aaaa")
  True
  >>> is_permutation("aba", "aab")
  True
  >>> is_permutation("abc", "cbd")
  False
  >>> is_permutation("bca", "acb")
  True
  >>> is_permutation("abd", "abc")
  False
  """
return string_to_char_dict(string1)== string_to_char_dict(string2)
