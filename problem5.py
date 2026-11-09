def key_value_swap(dictionary):
  """
  dictionary-> dictionary
  takes a dictionary and swaps its keys and values 
 
  >>> key_value_swap({'a': 1, 'b': 3, 'c': 4})
  {1: 'a', 3: 'b', 4: 'c'}
  >>> key_value_swap({'a': 1, 3: 'b', 'c': 4})
  {1: 'a', 'b': 3, 4: 'c'}
  >>> key_value_swap({'a': 1, 'b': 1, 'c': 4})
  {1: ['a','b'], 4: 'c'}
  
  ## keys cannot be identical (but values can) so when we swap in this case we'll have to be extra careful
  """
  ## add to this
