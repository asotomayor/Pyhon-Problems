# Python 2.7
# List of tuples movies watched
# Test cases
  # [(0,9),(0,10),(1,9)]
  # [(0,15),(10,25)]
  # [(0, 10), (15, 25), (12, 20), (30, 48)]
  # [(0, 10), (13, 18), (15, 23), (21, 26)]

# Solution 1
def Movietime():
 #time = [(0, 10), (13, 18), (15, 23), (21, 26)]
 time = [(0,15),(10,25)]
 sorted_t = sorted(time)
 print sorted_t
 start = 0
 end = 0
 total = 0
 for a, b in sorted_t:
  if start > b:
   continue
  if (a < start):
   total += b - start
   start = b
  else:
   total += b-a
   start = b
 return total


print(Movietime())










