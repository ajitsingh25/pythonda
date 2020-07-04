def arr_man(n, q):
    
    arr = [0] * (n)
    for a, b, k in q:
      # add k in the list
        arr[a-1] += k
        if b+1 <= n:
          # Substract the k from the list to keep the list balance
          # so that while adding list element we can get the max sum
            arr[b] -= k
        # print(arr)
            
    max_sum = 0

    #sum of all alements in the  list
    #max_sum to assign max sum while adding all elements in the list
    s = 0
    for i in arr:
        s += i    
        max_sum = max(max_sum, s)
        
    print(max_sum)