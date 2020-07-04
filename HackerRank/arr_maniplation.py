def arr_man(n, q):
    
    arr = [0] * (n)
    for a, b, k in q:
        arr[a-1] += k
        if b+1 <= n:
            arr[b] -= k
        # print(arr)
            
    max_sum = 0
    s = 0
    for i in arr:
        s += i
        max_sum = max(max_sum, s)
        
    print(max_sum)