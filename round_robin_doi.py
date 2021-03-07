import stack_que as d_que

def round_robin(que_class, process_list, quantum):
    for i in process_list:
        que_class.enqueue(i)

    while not que_class.is_empty():
        process = que_class.dequeue()
        if process[1] > quantum:
            que_class.enqueue((process[0], process[1] - quantum))
            print(process[0], quantum)
        else:
            print(process[0], process[1])


if __name__ == "__main__":
    #ID, process_time
    process_list = [("[ID]1001", 50), ("[ID]1002", 30), ("[ID]1003", 500), ("[ID]1004", 10)]
    quantum = 200

    que_class = d_que.que(10)

    round_robin(que_class, process_list, quantum)