from HackerRank \
import jumping_on_the_cloud, \
       sock_merchant, \
       count_valleys, \
       repeated_string, \
       hourglassSum, \
       arr_left_rot


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

