#バブルソート
def sort_original(input_data):
    """
    昇順のバブルソート
    """
    rslt_temp = input_data
    
    for i in range(len(rslt_temp)):
        for j in range(len(rslt_temp)-1, i, -1):
            #昇順ソート
            if  rslt_temp[j] < rslt_temp[j-1]:
                small_num = rslt_temp[j]
                large_num = rslt_temp[j-1]
                rslt_temp[j] = large_num
                rslt_temp[j-1] =small_num
        
        rslt = rslt_temp

    return(rslt)


#線形探索
def linear_search(target, input_data):
    """
    線形探索
    """
    for i in input_data:
        if i == target:
            return(input_data.index(i))


#二分木探索
def binary_search_tree(target, input_data):
    """
    二分木探索
    """
    tmp = []
    for i in range(0, len(input_data)):
        tmp_1 =  (input_data[i], i)
        tmp.append(tmp_1)

    sorted_data = sort_original(tmp)

    while (1):
        median = sorted_data[round(len(sorted_data)/2) - 1]
        if target > median[0]:
            sorted_data = sorted_data[round(len(sorted_data)/2) - 1:]
            if len(sorted_data) == 2:
                if sorted_data[0][0] == target:
                    answer = sorted_data[0][1]
                else:
                    answer = sorted_data[1][1]
                break
        elif target < median[0]:
            sorted_data = sorted_data[:round(len(sorted_data)/2) - 1]
            if len(sorted_data) == 2:
                if sorted_data[0][0] == target:
                    answer = sorted_data[0][1]
                else:
                    answer = sorted_data[1][1]
                break
        else:
            answer = median[1]
            break

    return(answer)


if __name__ == "__main__":
    input_data = [10,3,5,2,9,4,12]
    print(binary_search_tree(5, input_data))