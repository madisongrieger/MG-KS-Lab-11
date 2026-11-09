def string_to_char_dict(string):
  """
  string-> dictionary
  takes a string of text and returns a dictionary mapping each unique character to the number of times it appears

  >>> string_to_char_dict("aaaaaa")
  {'a': 6}
  >>> string_to_char_dict("abaaaab")
  {'a': 5, 'b': 2}
  >>> string_to_char_dict("aabbaabb")
  {'a': 4, 'b': 4}
  >>> string_to_char_dict("ababababa")
  {'a': 5, 'b':4}
  """
  amt_of_letters={}
  value=0
  for i in string:
    if i=='a':
      if amt_of_letters['a']:
        ['a']= value+1
      elif i=='b':
      if amt_of_letters['b']:
        ['b']=value+1
        print dict(amt_of_letters)
