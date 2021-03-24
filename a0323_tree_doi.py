"""
Rooted Tree
根付き木の表現
id k c1 ... ckの情報が付与されたときに
節点の情報をその番号が小さい順に出力する
node id, parent , depth, type , c1 ... ck
左子右兄弟表現(left-child, right-sibling representation)を用いる
"""
from collections import namedtuple
import dataclasses

@dataclasses.dataclass
class Node:
    parent:int = None
    left:int = None
    right:int = None
    depth:int = 0
    value:int = None

def rec(r,d):
    Tree[r].depth = d
    if Tree[r].right != None:
        rec(Tree[r].right,d)
    if Tree[r].left != None:
        rec(Tree[r].left,d+1)    


if __name__ == "__main__":
    input_data = []

    # while True:
    #     tmp=input()
    #     if tmp == "end":
    #         break
    #     else:
    #         input_data.append(int(tmp))

    input_data.append("0 3 1 4 10")
    input_data.append("1 2 2 3")
    input_data.append("2 0")
    input_data.append("3 0")
    input_data.append("4 3 5 6 7")
    input_data.append("5 0")
    input_data.append("6 0")
    input_data.append("7 2 8 9")
    input_data.append("8 0")
    input_data.append("9 0")
    input_data.append("10 2 11 12")
    input_data.append("11 0")
    input_data.append("12 0")

    N = len(input_data)
    # Tree = [Node()]*N
    Tree = [ Node() for i in range(N) ]
    
    for data_str in input_data:
        data = data_str.split()
        tree_id = int(data[0])
        tree_degree = int(data[1])

        Tree[tree_id].value = tree_id
        for i in range(tree_degree):
            child_id = int(data[2+i])
            if i == 0:
                Tree[tree_id].left = child_id
            else:
                Tree[left].right = child_id
            left = child_id
            Tree[child_id].parent = tree_id
    
    r_index = 0
    for i in range(N):
    # サンプルみたいに１行目に根がくるとは限らない.
    # そのため根を探す処理を入れる
        if Tree[i].parent == None:
            r_index = i
    
    rec(r_index,0)

    print(Tree)
    
    # Treeを可視化 # graphviz
    from graphviz import Digraph

    g = Digraph(format='png')
    g.attr('node', shape='circle')
    for edge_info in Tree:
        if edge_info.parent != None:
            g.edge(str(edge_info.parent), str(edge_info.value))
    g.view()