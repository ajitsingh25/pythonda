def repeatedString(s, n):
#   aba aba aba aba
    # n = n // len(s) + n % len(s)
    # occurance of 'a' will be 
    # no of occurance in string 's' * (n//len(s))
    # plus no of occurance in s[:(n%len(s))]
    q = n // len(s)
    r = n % len(s)
    d = {}
    d['a'] = 0
    
    for i in range(len(s)):
        if s[i] == 'a':
            d['a'] = d['a'] + 1
    
    total =q*d['a']
    
    d['a'] = 0
    
    for i in range(r):
        if s[i] == 'a':
            d['a'] += 1
        
    total = total + d['a']

    return total