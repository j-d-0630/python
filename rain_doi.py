import a0303_stack_que as d_stack


def area(stack_class, input_data):
    """
    面積算出
    """
    area = 0

    for i in range(0, len(input_data)):
        if input_data[i] == "\\":
            stack_class.push(i + 1)
        elif input_data[i] == "/":
            tmp = stack_class.pop()
            if tmp != None:
                area += ((i + 1) - tmp)
            else:
                pass
        elif input_data[i] == "_":
            pass
        else:
            pass

    return(area)

    
def region(stack_class, input_data):
    """
    regionを求める
    """
    tmp = []
    flg = 0

    for i in range(0, len(input_data)):
        if input_data[i] == "\\":
            stack_class.push("\\")
            flg = 1
        elif input_data[i] == "/":
            if flg == 1:
                stack_class.pop()
                if stack_class.stack_list[0] == None:
                    tmp.append(i)
                    flg = 0
        elif input_data[i] == "_":
            pass
        else:
            pass
    
    return(tmp)


def rslt(stack_class_reg, stack_class_ara, input_data):
    area_list = []
    region_list = region(stack_class_reg, input_data)
    
    for i in range(0, len(region_list)):
        area_tmp = area(stack_class_reg, input_data[:region_list[i] + 1])
        if len(area_list) == 0:
            area_list.append(area_tmp)
        else:
            area_tmp -= sum(area_list)
            area_list.append(area_tmp)

    return(area_list)


if __name__ == "__main__":
    stack_class_reg = d_stack.stack(20)
    stack_class_ara = d_stack.stack(20)

    input_data = ["\\", "\\", "\\", "/", "/", "/", "/", "\\", "/", "\\", "_", "/"]

    region_list = region(stack_class_reg, input_data)
    print("入力は{0}".format(input_data))
    print("区間の境界のindexは{0}".format(region_list))

    rslt = rslt(stack_class_reg, stack_class_ara, input_data)
    print("各領域の面積は{0}".format(rslt))