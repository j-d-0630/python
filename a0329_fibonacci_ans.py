count = 0
count_dp = 0

memory = []

def fibonacci(i):
    global count
    if i == 0:
        count += 1
        return 0
    if i == 1:
        count += 1
        return 1
    
    if i >= 2:
        count += 1
        return fibonacci(i-1) + fibonacci(i-2)


def fibonacci_dp(i):
    global count_dp
    count_dp += 1
    if i == 0:
        return 0
    elif i == 1:
        return 1        
    else:
        rslt = 0
        if memory[i] != None:
            rslt = memory[i]
        else:
            rslt = fibonacci_dp(i-1) + fibonacci_dp(i-2)
            memory[i] = rslt

        return rslt

# i = [1,2,4,5]

# for input_value in i:
#     ans = fibonacci(input_value)
#     print(ans)
input_value = 6

memory = [None]*(input_value+1)
ans = fibonacci(input_value)
print(ans)
print(count)
ans = fibonacci_dp(input_value)
print(ans)
print(count_dp)
