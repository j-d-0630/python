def function(a,b):
    product = a*b

    if product%2 == 0:
        return "Even"
    else:
        return "Odd"


inputdata = input()
inputdata_2 = inputdata.split()
a = int(inputdata_2[0])
b = int(inputdata_2[1])

ans = function(a,b)
print(ans)