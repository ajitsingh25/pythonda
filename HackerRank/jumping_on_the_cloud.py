def jumping_on_the_cloud(arr):
  l = len(arr)
  jump = 0
  currCloud = 0

  while currCloud < l -1:
    if currCloud < l -2 and arr[currCloud+2] == 0:
      currCloud += 2  ## jump two Place
    else:
      currCloud += 1 ## jump one place

    jump += 1

  return jump



  