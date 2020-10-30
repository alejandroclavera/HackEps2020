result={'n':None,'max_length':0}
for n in range(1,100001):
    result[n] = 1
    number = n
    while number != 1:
        if n != number and number in result:
            result[n]+= result[number]    
            break
        number = number/2 if number%2==0 else number * 3 + 1
        result[n] += 1 
    if result['max_length'] < result[n]:
                result['max_length'] = result[n]
                result['n'] = n 
print(result['n'])
