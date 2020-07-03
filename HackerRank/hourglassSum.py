def hourglassSum(arr):
  # arr row length
  ar = 6

  # arr col length
  ac = 6

  # Hour glass has 7 elements, value of each elements lies between -9 to 0
  # so Max sum in worst case should be -9*7 if all elements are -9
  max_sum = -9*7

  for r in range(ar - 2):
    hsum = 0
    for c in range(ac - 2):
      top = arr[r][c] + arr[r][c+1] + arr[r][c+2]
      mid = arr[r+1][c+1]
      bot = arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2]
      hsum = top + mid + bot
      max_sum = max(max_sum, hsum)

  return max_sum