def key_value_swap(dictionary):
  """
  dictionary-> dictionary
  takes a dictionary and swaps its keys and values 
 
  >>> key_value_swap({'a': 1, 'b': 3, 'c': 4})
  {1: 'a', 3: 'b', 4: 'c'}
  >>> key_value_swap({'a': 1, 3: 'b', 'c': 4})
  {1: 'a', 'b': 3, 4: 'c'}
  >>> key_value_swap({'a': 1, 'b': 1, 'c': 4})
  {1: ['a', 'b'], 4: 'c'}
  >>> key_value_swap({'a': 2, 'b': 5, 'c': 8})
  {2: 'a', 5: 'b', 8: 'c'}
  >>> key_value_swap({'a': 7, 'b': 7, 'c': 9})
  {7: ['a', 'b'], 9: 'c'}
  """
  swap={}
  for key in dictionary:
    val = dictionary[key]
    if val in swap:
      if type (swap[val])==list:
        swap[val].append(key)
      else:
        swap[val]=[swap[val],key]
    else:
      swap[val] = key
   return swap
