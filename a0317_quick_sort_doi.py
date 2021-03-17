import random
import string
import time
import copy

def partition(data,p,r):
    """
    keyを境界にkeyより小さいものと大きいものとに分ける
    変数：keyのindex
    """
    #最後尾の値をkeyに設定
    x = data[r]
    i = p - 1

    #p~rの範囲(keyより右側の範囲)を探索し、keyより小さいものを見つけたらkeyより左側の領域で交換されたことがないものと交換する
    #これにより左側はkeyより小さいものが集まっていく
    for j in range(p,r):
        if data[j][1] >= x[1]:
            i += 1
            t = data[i]
            data[i] = data[j]
            data[j] = t
    
    t = data[i+1]
    data[i+1] = data[r]
    data[r] = t
    return i+1


def quickSort(data,p,r):
    if p < r:
        q = partition(data,p,r)
        quickSort(data,p,q-1)
        quickSort(data,q+1,r)


#挿入ソート
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
        while( ( j>=0 and rslt[j][1] < v[1] ) ):
            rslt[j+1] = rslt[j]
            j-=1
        rslt[j+1] = v
    
    return rslt


if __name__ == "__main__":
    data_num = 1000
    data = [[random.choice(string.ascii_uppercase),random.randint(0,1000)] for i in range(data_num)]
    data_for_quick = copy.deepcopy(data)
    data_for_insert = copy.deepcopy(data)

    time1 = time.time()
    quickSort(data_for_quick,0,len(data_for_quick)-1)
    time2 =time.time()
    elapsed_time_1 = time2 - time1

    time3 = time.time()
    rslt = sort_insert(data_for_insert)
    time4 =time.time()
    elapsed_time_2 = time4 - time3
    # print(data_for_quick)
    # print(rslt)

    diagnose =  rslt == data_for_quick
    print("quick sortは安定なソート？　⇒　",diagnose)
    print("quick sortの処理時間　⇒　",elapsed_time_1)
    print("insert sortの処理時間　⇒　",elapsed_time_2)