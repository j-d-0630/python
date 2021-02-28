"""
スタッククラス、キュークラスの作成
"""
#スタックはFILO
#キューはFIFO

class stack():
    def __init__(self, size):
        self.size = size
        self.stack_list = [None]*self.size
        self.count = 0
    
    def stack_push(self, push_data):
        i = self.count
        self.stack_list[i] = push_data
        self.count += 1
    
    def stack_pop(self):
        # key = 0
        # for i in range(len(self.stack_list)-1, 0, -1):
        #     if self.stack_list[i] != None:
        #         key = i
        #         break

        poped_value = self.stack_list[self.count-1]
        self.stack_list[self.count-1] = None
        self.count -= 1
        return(poped_value)
    
    def stack_is_empty(self):
        if self.stack_list == [None]*self.size:
            return(True)
        else:
            return(False)


class que():
    def __init__(self, size):
        self.size = size
        self.que_list = [None]*self.size
        self.count = 0
    
    def que_enqueue(self, enqueue_data):
        i = self.count
        self.que_list[i] = enqueue_data
        self.count += 1
    
    def que_dequeue(self):
        dequeued_value = self.que_list[0]
        for i in range(0, len(self.que_list)-1):
            self.que_list[i] = self.que_list[i+1]
        
        self.que_list[len(self.que_list)-1] = None
        return(dequeued_value)
    
    def que_is_empty(self):
        if self.que_list == [None]*self.size:
            return(True)
        else:
            return(False)


if __name__ == "__main__":
    #################################################################################################
    #stack
    #################################################################################################
    print("stack構造のデータを作成する")
    #サイズ10のインスタンスの作成
    stack_class = stack(10)

    print("リストは空か？ ⇒ {0}".format(stack_class.stack_is_empty()))

    #push
    stack_class.stack_push(5)
    stack_class.stack_push(9)
    stack_class.stack_push(10)
    stack_class.stack_push(7)
    stack_class.stack_push(1)

    print("データリストは{0}".format(stack_class.stack_list))
    print("リストは空か？ ⇒ {0}".format(stack_class.stack_is_empty()))

    #pop
    poped_value_1 = stack_class.stack_pop()
    print("取り出した値は{0}。データリストは{1}".format(poped_value_1, stack_class.stack_list))
    print("リストは空か？ ⇒ {0}".format(stack_class.stack_is_empty()))

    poped_value_2 = stack_class.stack_pop()
    print("取り出した値は{0}。データリストは{1}".format(poped_value_2, stack_class.stack_list))
    print("リストは空か？ ⇒ {0}".format(stack_class.stack_is_empty()))

    poped_value_3 = stack_class.stack_pop()
    print("取り出した値は{0}。データリストは{1}".format(poped_value_3, stack_class.stack_list))
    print("リストは空か？ ⇒ {0}".format(stack_class.stack_is_empty()))

    poped_value_4 = stack_class.stack_pop()
    print("取り出した値は{0}。データリストは{1}".format(poped_value_4, stack_class.stack_list))
    print("リストは空か？ ⇒ {0}".format(stack_class.stack_is_empty()))

    poped_value_5 = stack_class.stack_pop()
    print("取り出した値は{0}。データリストは{1}".format(poped_value_5, stack_class.stack_list))
    print("リストは空か？ ⇒ {0}".format(stack_class.stack_is_empty()))


    #################################################################################################
    #que
    #################################################################################################
    print("que構造のデータを作成する")
    #サイズ10のインスタンスの作成
    que_class = que(10)

    print("リストは空か？ ⇒ {0}".format(que_class.que_is_empty()))

    #enqueue
    que_class.que_enqueue(5)
    que_class.que_enqueue(9)
    que_class.que_enqueue(10)
    que_class.que_enqueue(7)
    que_class.que_enqueue(1)

    print("データリストは{0}".format(que_class.que_list))
    print("リストは空か？ ⇒ {0}".format(que_class.que_is_empty()))

    #dequeue
    dequeued_value_1 = que_class.que_dequeue()
    print("取り出した値は{0}。データリストは{1}".format(dequeued_value_1, que_class.que_list))
    print("リストは空か？ ⇒ {0}".format(que_class.que_is_empty()))
    
    dequeued_value_2 = que_class.que_dequeue()
    print("取り出した値は{0}。データリストは{1}".format(dequeued_value_2, que_class.que_list))
    print("リストは空か？ ⇒ {0}".format(que_class.que_is_empty()))
    
    dequeued_value_3 = que_class.que_dequeue()
    print("取り出した値は{0}。データリストは{1}".format(dequeued_value_3, que_class.que_list))
    print("リストは空か？ ⇒ {0}".format(que_class.que_is_empty()))
    
    dequeued_value_4 = que_class.que_dequeue()
    print("取り出した値は{0}。データリストは{1}".format(dequeued_value_4, que_class.que_list))
    print("リストは空か？ ⇒ {0}".format(que_class.que_is_empty()))
    
    dequeued_value_5 = que_class.que_dequeue()
    print("取り出した値は{0}。データリストは{1}".format(dequeued_value_5, que_class.que_list))
    print("リストは空か？ ⇒ {0}".format(que_class.que_is_empty()))