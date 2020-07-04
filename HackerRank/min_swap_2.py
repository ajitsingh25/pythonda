def min_swap2(arr):
  n = len(arr)
  swaps = 0
  for i in range(n-1):
    while arr[i] != i+1:
      t = arr[arr[i] -1]   
      arr[arr[i] -1] = arr[i]
      arr[i] = t
      swaps += 1

  return swaps