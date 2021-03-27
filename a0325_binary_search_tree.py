"""
Binary Search Tree
二分探索木
動的な集合を取り扱うデータ構造として連結リストがあるが、
要素を探索するにはO(n)の計算量を必要とする
より効率的に追加・削除・探索をするのに二分探索木がある
各節点にキーを持ち、二分探索木条件を常に満たす
二分探索木条件は以下である
・ある節点xにおける左部分木yは(yのキー <=  xのキー）を満たす
・ある節点xにおける右部分木zは(xのキー <=  zのキー）を満たす
"""

import dataclasses
from typing import ClassVar

root_node = None

@dataclasses.dataclass
class Node:
    key:int = None
    parent:ClassVar = None
    left:ClassVar = None
    right:ClassVar = None


def insert(new_node:Node):
    global root_node
    parent_node = None

    r_node = root_node
    while r_node != None:
        parent_node = r_node
        if new_node.key <= r_node.key:
            r_node = r_node.left
        else:
            r_node = r_node.right
    
    new_node.parent = parent_node
    if parent_node == None:
        root_node = new_node
    elif new_node.key <= parent_node.key:
        parent_node.left = new_node
    else:
        parent_node.right = new_node


def find(t_key):
    global root_node

    t_node = root_node
    while (t_node != None) and (t_node.key != t_key):
        if t_key <= t_node.key:
            t_node = t_node.left
        else:
            t_node = t_node.right
    
    return t_node


def getMinimum(t_node):
    while t_node.left != None:
        t_node = t_node.left
    return t_node

def getSuccessor(d_node:Node):
    if d_node.right != None:
        return getMinimum(d_node.right)

    t_node = d_node.parent
    while t_node != None and d_node == t_node.right:
        d_node = t_node
        t_node = t_node.parent

    return t_node


def delete(d_node:Node):
    global root_node

    if d_node.left == None or d_node.right == None:
        t_node = d_node
    else:
        t_node = getSuccessor(d_node)
    
    c_node = t_node.left if t_node.left != None else t_node.right

    if c_node != None:
        c_node.parent = t_node.parent
    
    if t_node.parent == None:
        root_node = c_node
    elif t_node == t_node.parent.left:
        t_node.parent.left = c_node
    else:
        t_node.parent.right = c_node
    
    if t_node != d_node:
        d_node.key = t_node.key




def PreOrderWalk(r,walkList):
    walkList.append(r.key)

    if r.left != None:
        PreOrderWalk(r.left,walkList)
    if r.right != None:
        PreOrderWalk(r.right,walkList)


def InOrderWalk(r,walkList):
    if r.left != None:
        InOrderWalk(r.left,walkList)
    
    walkList.append(r.key)

    if r.right != None:
        InOrderWalk(r.right,walkList)

if __name__ == "__main__":

    input_data = []

    # while True:
    #     tmp=input()
    #     if tmp == "end":
    #         break
    #     else:
    #         input_data.append(int(tmp))

    input_data.append("32")
    input_data.append("12")
    input_data.append("40")
    input_data.append("50")
    input_data.append("9")
    input_data.append("13")
    input_data.append("14")

    for node_data in input_data:
        new_node = Node(key=int(node_data))
        insert(new_node)
    
    pre_list = []
    PreOrderWalk(root_node,pre_list)
    print(pre_list)

    in_list = []
    InOrderWalk(root_node,in_list)
    print(in_list)

    ans = find(12)
    print("Yes") if ans != None else print("No")

    delete(ans)

    in_list = []
    InOrderWalk(root_node,in_list)
    print(in_list)