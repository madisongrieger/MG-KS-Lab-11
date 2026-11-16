def merge(dictionary1, dictionary2):
  """
  dict,dict-> dict
  merges two dictionaries with numeric values following the rule that if a key 

  >>> merge({"age": 3, "height": 35, "c": 5}, {"ID": 983749, "c": 2})
  {"age": 3, "height": 35, "c": 7, "ID": 983749}
  >>> merge({"a": 1, "b": 2}, {"c": 3, "d": 4})
  {'a': 1, 'b': 2, 'c': 3, 'd': 4}
  >>> merge({"age": 5, "height": 40, "c": 7}, {"ID": 9804, "c": 2})
  {"age": 5, "height": 40, "c": 9, "ID": 9804}
  """
  merge_dict= {}
  for key in dictionary1:
    merge_dict[key] = dictionary[key]
  for key in dictionary2:
    if key in merge_dict:
      merge_dict[key] = merge_dict[key] + dictionary2[key]
  else:
    merge_dict[key] = dictionary2[key]
  return merge_dict
