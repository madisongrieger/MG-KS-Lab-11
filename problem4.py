def compression(string):
  """
  string -> string
  compresses a string into an alternating sequence of characters and integers in which the integer represents the number of consecutive duplicates of that character

  >>> compression("aabcccccaaa")
  'a2b1c5a3'
  >>> compression ("aaaabbccca")
  'a4b2c3a1'
  >>> compression ("bbbccaaa")
  'b3c2a3'
  """ 
  letters=[]
  count = 1
  for i in range(1, len(string)):
    if string[i]== string[i-1]:
      count += 1
    else:
      result += string[i-1] + str(count)
      count=1
  result += string[-1] + str(count)
  return result 
