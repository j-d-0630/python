def solve(i, m):
    if m == 0:
        return True
    elif i == n:
        return False

    rslt = solve(i+1, m) or solve(i+1, m-input_data[i])
    return rslt 

input_data = [3,6,2,1]
n = len(input_data)
M = 5

rslt = solve(0, M)
print(rslt)