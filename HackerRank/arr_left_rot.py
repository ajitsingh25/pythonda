def arr_left_rot(arr, d):

  for _ in range(d):
    tmp = arr[0]
    arr.remove(tmp)
    arr.append(tmp)

  return arr