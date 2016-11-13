def find_max_min(number):
  if min(number) == max(number):
    return [len(number)]
  else:
    return [min(number), max(number)]