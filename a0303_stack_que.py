"""
スタッククラス、キュークラスの定義
"""
#スタックはFILO
#キューはFIFO

class stack():
    """
    stackクラス
    引数：リストのサイズ
    """
    def __init__(self, size):
        """
        引数：リストのサイズ
        変数：size, stack_list, count
        """
        self.size = size
        self.stack_list = [None]*self.size
        self.count = 0
    
    def push(self, push_data):
        """
        引数：プッシュしたい数値
        """
        i = self.count
        self.stack_list[i] = push_data
        self.count += 1
    
    def pop(self):
        if self.count > 0:
            poped_value = self.stack_list[self.count-1]
            self.stack_list[self.count-1] = None
            self.count -= 1
            return(poped_value)
        else:
            # print("取り出せる値がありません")
            return(None)
    
    def is_empty(self):
        if self.stack_list == [None]*self.size:
            return(True)
        else:
            return(False)


class que():
    """
    queクラス
    引数：リストのサイズ
    """
    def __init__(self, size):
        """
        引数：リストのサイズ
        """
        self.size = size
        self.que_list = [None]*self.size
        self.count = 0
    
    def enqueue(self, enqueue_data):
        """
        引数：エンキューしたい数値
        """
        i = self.count
        self.que_list[i] = enqueue_data
        self.count += 1
    
    def dequeue(self):
        """
        デキューした値を返す
        """
        dequeued_value = self.que_list[0]
        for i in range(0, len(self.que_list)-1):
            self.que_list[i] = self.que_list[i+1]
        
        self.que_list[len(self.que_list)-1] = None
        self.count -= 1
        return(dequeued_value)
    
    def is_empty(self):
        """
        空ならTrue, 空でないならFalseを返す
        """
        if self.que_list == [None]*self.size:
            return(True)
        else:
            return(False)