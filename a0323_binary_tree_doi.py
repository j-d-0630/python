"""
Binary Tree
根付き二分木の表現
id left rightの情報が付与されたときに
節点の情報をその番号が小さい順に出力する
node id, parent , depth, heigth
Preorder Tree Walk 先行順巡回
    根節点, 左部分木, 右部分木の順番
Inorder Tree Walk 中間順巡回
    左部分木, 根節点, 右部分木の順番
Postorder Tree Walk 後行順巡回
    左部分木, 右部分木, 根節点の順番
"""

import dataclasses

@dataclasses.dataclass
class Node:
    parent:int = None
    left:int = None
    right:int = None
    depth:int = 0
    height:int = 0
    value:int = None

def rec(r,d):
    Tree[r].depth = d
    if Tree[r].right != None:
        rec(Tree[r].right,d+1)
    if Tree[r].left != None:
        rec(Tree[r].left,d+1)

def set_hegiht(r):
    h1 = 0
    h2 = 0
    if Tree[r].right != None:
        h1 = set_hegiht(Tree[r].right) + 1
    if Tree[r].left != None:
        h2 = set_hegiht(Tree[r].left) + 1
    
    Tree[r].height = h1 if h1 > h2 else h2

    return Tree[r].height

def PreOrderWalk(r,walkList):
    walkList.append(Tree[r].value)
    if Tree[r].left != None:
        PreOrderWalk(Tree[r].left,walkList)
    if Tree[r].right != None:
        PreOrderWalk(Tree[r].right,walkList)

def InOrderWalk(r,walkList):
    if Tree[r].left != None:
        InOrderWalk(Tree[r].left,walkList)
    
    walkList.append(Tree[r].value)

    if Tree[r].right != None:
        InOrderWalk(Tree[r].right,walkList)

def PostOrderWalk(r,walkList):
    if Tree[r].left != None:
        PostOrderWalk(Tree[r].left,walkList)
    if Tree[r].right != None:
        PostOrderWalk(Tree[r].right,walkList)
    
    walkList.append(Tree[r].value)

if __name__ == "__main__":
    input_data = []

    input_data.append("0 1 4")
    input_data.append("1 2 3")
    input_data.append("2 -1 -1")
    input_data.append("3 -1 -1")
    input_data.append("4 5 8")
    input_data.append("5 6 7")
    input_data.append("6 -1 -1")
    input_data.append("7 -1 -1")
    input_data.append("8 -1 -1")

    N = len(input_data)

    Tree = [ Node() for i in range(N) ]

    for data_str in input_data:
        data = data_str.split()
        node_id = int(data[0])
        node_left = int(data[1])
        node_right = int(data[2])

        Tree[node_id].value = node_id
        if node_right != -1:
            Tree[node_id].right = node_right
            Tree[node_right].parent = node_id 
        if node_left != -1:
            Tree[node_id].left = node_left
            Tree[node_left].parent = node_id
        
    r_index = 0
    for i in range(N):
        if Tree[i].parent == None:
            r_index = i
    
    rec(r_index,0)
    set_hegiht(r_index)

    print(Tree)

    walkList = []
    PreOrderWalk(0,walkList)
    print("PreOrderWalk Result")
    print(walkList)


    walkList = []
    InOrderWalk(0,walkList)
    print("InOrderWalk Result")
    print(walkList)

    walkList = []
    PostOrderWalk(0,walkList)
    print("PostOrderWalk Result")
    print(walkList)

     # Treeを可視化 # graphviz
    from graphviz import Digraph

    g = Digraph(format='png')
    g.attr('node', shape='circle')
    for edge_info in Tree:
        if edge_info.parent != None:
            g.edge(str(edge_info.parent), str(edge_info.value))
    g.view()