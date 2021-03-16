"""
Basic Sorting Problem
"""


def sort_bubble(input_data):
    """
    bubble sort バブルソート
    隣り合う要素を入れ替えることを繰り返す
    入れ替わりが起きなくなったら終了
    安定なソート
    """
    rslt = input_data.copy()
    flag = 1
    j=0
    while flag:
        flag = 0
        for i in range(0,len(rslt)-j-1):
            if rslt[i] > rslt[i+1]:
                tmp = rslt[i+1]
                rslt[i+1] = rslt[i]
                rslt[i] = tmp
                flag = 1
        j+=1
    
    return rslt

def sort_insert(input_data):
    """
    insert sort 挿入ソート
    ソート済み領域をどんどん拡張していく
    拡張していく中で拡張をする先頭要素を適切な場所に挿入していく
    安定なソート
    """
    rslt = input_data.copy()
    for i in range(1,len(input_data)):
        v = rslt[i]
        j = i-1
        while( ( j>=0 and rslt[j] < v ) ):
            rslt[j+1] = rslt[j]
            j-=1
        rslt[j+1] = v
    
    return rslt

if __name__ == "__main__":
    '''
    数値を標準入力で連続で受け取るメインプログラム
    '''
    print("start input data. if you completed input, you type \"end\".")

    input_data = []
    while(1):
        tmp = input()
        if tmp == "end":
            break
        else:
            input_data.append(int(tmp))
    
    a = 1
    b =2



    output = sort_insert(input_data)
    # output = sort_bubble(input_data)

    print(output)    