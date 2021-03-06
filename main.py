from HackerRank \
import jumping_on_the_cloud, \
       sock_merchant, \
       count_valleys, \
       repeated_string, \
       hourglassSum, \
       arr_left_rot, \
       new_year_chaos, \
       min_swap_2, \
       arr_maniplation


if __name__ == "__main__":

# Cloud Jump
  print(jumping_on_the_cloud.jumping_on_the_cloud([0,0,1,0,0,1,0]))
  print(jumping_on_the_cloud.jumping_on_the_cloud([0,0,0,0,1,0]))

# Sock Merchant
  print(sock_merchant.sock_merchant([10,20,20,10,10,30,50,10,20]))

# Valleys Count
  print(count_valleys.count_valleys('UDDDUDUU'))

# Repeated String
  print(repeated_string.repeatedString('aba', 10))

#hour glass
  arr = [[1, 1, 1, 0, 0, 0],
 [0, 1, 0, 0, 0, 0],
 [1, 1, 1, 0, 0, 0],
 [0, 0, 2, 4, 4, 0],
 [0, 0, 0, 2, 0, 0],
 [0, 0, 1, 2, 4, 0]]

  print(hourglassSum.hourglassSum(arr))

# array left rotation
  print(arr_left_rot.arr_left_rot([1,2,3,4,5], 4))

# New year Chaos
  new_year_chaos.minBribes([2,1,5,3,4])
  new_year_chaos.minBribes([2,5,1,3,4])
  new_year_chaos.minBribes([1,2,5,3,7,8,6,4])

# Min Swap 2
  print(min_swap_2.min_swap2([1, 3, 5, 2, 4, 6, 7]))
  print(min_swap_2.min_swap2([2,3,4,1,5]))

# Array Manipulation
  queries1 = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
  queries2 = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]

  arr_maniplation.arr_man(5, queries1)
  arr_maniplation.arr_man(10, queries2)