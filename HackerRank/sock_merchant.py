from collections import defaultdict

def sock_merchant(arr):

  d = defaultdict(int)
  pair = 0

  for i in arr:
    d[i] += 1

  for i in d:
    pair += d[i] // 2

  return pair