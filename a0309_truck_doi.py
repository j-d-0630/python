import time
#バブルソート
def sort_original(input_data):
    rslt_temp = input_data
    
    for i in range(len(rslt_temp)):
        #先頭～後端の範囲で後端から比較していき、最小値が先頭に来るようにする
        #2番目～後端の範囲で後端から比較し、2番目に２番目に小さい数が来るようにする
        #3番目～後端・・・・・・
        for j in range(len(rslt_temp)-1, i, -1):
            #昇順ソート
            if  rslt_temp[j] < rslt_temp[j-1]:
                small_num = rslt_temp[j]
                large_num = rslt_temp[j-1]
                rslt_temp[j] = large_num
                rslt_temp[j-1] =small_num
        
        rslt = rslt_temp

    return(rslt)


class truck():
    def __init__(self, size):
        self.size = size
        self.stack_list = [None] * size
        self.count = 0
 
    def pick_up(self, w):
        if w > (self.size - self.count):#積めない
            return("Incomplete")
        else:#積める            
            self.count += w
            return("Complete")


time_1 = time.time()
if __name__ == "__main__":
    input_data = [8,1,7,3,9]
    input_data = sort_original(input_data)
    
    flag = 0
    P = 0
    while flag == 0:
        truck_A = truck(P)
        truck_B = truck(P)
        truck_C = truck(P)

        for i in range(len(input_data)-1, -1, -1):
            min_tmp = min(truck_A.count, truck_B.count, truck_C.count)
            if truck_A.count == min_tmp:
                most_vacant_truck = truck_A
            elif truck_B.count == min_tmp:
                most_vacant_truck = truck_B
            else:
                most_vacant_truck = truck_C
            
            tmp = most_vacant_truck.pick_up(input_data[i])
            if tmp == "Incomplete":
                P += 1
                break
            elif tmp == "Complete" and i > 0:
                pass
            else:
                ans = P
                flag = 1

    
    time_2 = time.time()
    elapsed_time = time_2 - time_1

    print(elapsed_time)
    print("最小なPは{0}".format(ans))