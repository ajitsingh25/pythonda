from collections import defaultdict

def count_valleys(s):
  d = defaultdict(int)
  valley = 0

  for i in s:

    if i == 'U':
      d['temp'] += 1

      if d['temp'] == 0:
        valley += 1

    else:
      d['temp'] -= 1

  return valley

