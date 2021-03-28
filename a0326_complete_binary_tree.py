"""
Complet Binary Tree
完全二分木
データ構造を作成する上で、データの到着順ではなくデータがもつあるキーを基準にして
優先度順が高いものから取り出す優先度付きキューは、
二分ヒープ（完全二分木）を用いることにより比較的簡単に実装できる
二分ヒープの作り方をまずは実装する
キーを連続でinputされた時に、
二分ヒープの各ノード情報を出力するプログラムを書く
node id, key, parent key, left key,right key
"""

import dataclasses
from typing import ClassVar

parent = lambda data : int(data/2)
left = lambda data : int(data*2)
right = lambda data : int(data*2+1)


def comple_binary_tree(input_data):

    N = len(input_data)

    for i in range(1,N+1):
        print("node id:{}".format(i))
        print("key={}".format(input_data[i-1]))
        if parent(i)>= 1: print("parent key ={}".format(input_data[parent(i)-1]))
        if left(i)<= N: print("left key ={}".format(input_data[left(i)-1]))
        if right(i)<= N: print("right key ={}".format(input_data[right(i)-1]))
        print()


if __name__ == "__main__":

    input_data = []

    # while True:
    #     tmp=input()
    #     if tmp == "end":
    #         break
    #     else:
    #         input_data.append(int(tmp))

    input_data.append(7)
    input_data.append(8)
    input_data.append(1)
    input_data.append(2)
    input_data.append(3)

    comple_binary_tree(input_data)