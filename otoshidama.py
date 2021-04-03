def otoshidama(N,Y):
    tmp = int(Y/1000)
    up_lim_1 = int(Y/5000)
    up_lim_2 = int(Y/10000)
    sabun = tmp-N
    if sabun == 0:
        return[0,0,tmp]
    
    for i in range(0,up_lim_2+1):
        for j in range(0,up_lim_1+1-2*i):
            sabun2 = sabun-9*i-4*j
            if sabun2==0:
                return[i,j,N-i-j]
    
    return[-1,-1,-1]

tmp = input()
tmp_2 = tmp.split()
N = int(tmp_2[0])
Y = int(tmp_2[1])
ans = otoshidama(N,Y)
print("{0} {1} {2}".format(ans[0],ans[1],ans[2]))