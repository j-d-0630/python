"""
Maximum Heap
最大ヒープ
データ構造を作成する上で、データの到着順ではなくデータがもつあるキーを基準にして
優先度順が高いものから取り出す優先度付きキューは、
二分ヒープ（完全二分木）を用いることにより比較的簡単に実装できる
最も大きい値が根になるような最大ヒープを作成する
キーを連続でinputされた時に作成された
Maxヒープをノード番号を１から順に出力する
"""

parent  = lambda data : int(data/2)
left  = lambda data : int(data*2)
right  = lambda data : int(data*2+1)

def maxHeapfify(input_data,i):
    l = left(i)
    r = right(i)

    N = len(input_data)
    large_i = i
    if l < N:
        if input_data[l] > input_data[large_i]:large_i = l
    if r < N:
        if input_data[r] > input_data[large_i]:large_i = r
    
    if large_i != i:
        tmp = input_data[large_i]
        input_data[large_i] = input_data[i]
        input_data[i] = tmp

        maxHeapfify(input_data,large_i)


if __name__ == "__main__":

    input_data = []

    # while True:
    #     tmp=input()
    #     if tmp == "end":
    #         break
    #     else:
    #         input_data.append(int(tmp))

    input_data.append(4)
    input_data.append(1)
    input_data.append(3)
    input_data.append(2)
    input_data.append(16)
    input_data.append(9)
    input_data.append(10)
    input_data.append(14)
    input_data.append(8)
    input_data.append(7)
    
    input_data.insert(0,None)
    N = len(input_data)
    H = int(N/2)
    for i in reversed(range(1,H)):
        maxHeapfify(input_data,i)
    input_data.pop(0)

    print(input_data)