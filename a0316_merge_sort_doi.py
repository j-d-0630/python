import random
import time

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
        v = rslt[i][0]
        j = i-1
        while( ( j>=0 and rslt[j][0] < v ) ):
            rslt[j+1][0] = rslt[j][0]
            j-=1
        rslt[j+1][0] = v
    
    return rslt


def merge(data,left,right):
    mid = int( (left+right) / 2 )
    n1 = mid - left
    n2 = right - mid
    leftData = [ data[i+left] for i in range(n1) ]
    rightData = [ data[i+mid] for i in range(n2) ]
    i = 0
    j = 0
    leftData.append([-1,"ダミー"])
    rightData.append([-1,"ダミー"])
    for k in range(left,right):
        if leftData[i][0] >= rightData[j][0]:
            data[k] = leftData[i]
            i += 1
        else:
            data[k] = rightData[j]
            j += 1


def mergeSort(data,left,right):
    if left + 1 < right:
        mid = int( (left+right) / 2 )
        mergeSort(data,left,mid)
        mergeSort(data,mid,right)
        merge(data,left,right)


if __name__ == "__main__":
    input_data = []
    for i in range(100000):
        input_data.append([random.randint(0,1000),random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')])
        
    input_data_for_insert = input_data.copy()
    input_data_for_merge = input_data.copy()

    # インサートソート
    time1 = time.time()
    sort_insert_rslt = sort_insert(input_data_for_insert)
    time2 =time.time()
    elapsed_time_1 = time2 - time1

    #マージソート
    time3 = time.time()
    mergeSort(input_data_for_merge,0,len(input_data_for_merge))
    time4 =time.time()
    elapsed_time_2 = time4 - time3

    print("================================================================")
    print("input_dataは",input_data)
    print("================================================================")
    print("insert sortの結果は",sort_insert_rslt)
    print("================================================================")
    print("merge sortの結果は",input_data_for_merge)
    print("================================================================")
    print("insert sortの処理時間は",elapsed_time_1)
    print("merge sortの処理時間は",elapsed_time_2)

    diagnose =  sort_insert_rslt == input_data_for_merge
    print("merge sortは安定なソート？　⇒　",diagnose)