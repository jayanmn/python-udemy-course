def concatenate(**kwargs):
  result = "" 
  for arg in kwargs.values():
     result += arg
  return result

print(concatenate(a="Hello", b="World", c="!"))