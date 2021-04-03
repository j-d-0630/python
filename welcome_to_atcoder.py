def function(a,b,c,text):
    return[a+b+c,text]

tmp1 = input()
tmp2 = input()
tmp3 = tmp2.split()
tmp4 = input()

a = int(tmp1)
b = int(tmp3[0])
c = int(tmp3[1])
text = tmp4

ans = function(a,b,c,text)
print("{0} {1}".format(ans[0],ans[1]))