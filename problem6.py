def merge(dictionary1, dictionary2):
  """
  dict,dict-> dict
  merges two dictionaries with numeric values following the rule that if a key 

  >>> merge({"age": 3, "height": 35, "c": 5}, {"ID": 983749, "c": 2})
  {"age": 3, "height": 35, "c": 7, "ID": 983749}
  ## order of the key-value pairs does not have to match to still agree
  """
  merge_dict= {}
  for key in dictionary1:
    merge_dict[key] =dictionary[key]
  for key in dictionary2:
    if key in merge_dict:
      merge_dict[key]= merge_dict[key]+ dictionary2[key]
  else:
    merge_dict[key] = dictionary2[key]
  return merge_dict
