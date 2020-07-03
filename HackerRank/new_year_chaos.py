def minBribes(q):

  bribes = 0
  chaos = False

  for i in range(len(q)):
    if q[i] - (i+1) > 2:
      chaos = True

    j = max(0, q[i] - 2)
    while j < i:
      if q[j] > q[i]:
        bribes += 1
      j += 1

  if chaos:
    print("Too chaotic")
  else:
    print(bribes)

