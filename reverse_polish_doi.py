import stack_que_doi_2 as d_stack

def reverse_polish(stack_class):
    print("inputしてくれ")

    while(1):
        input_data = input()
        if input_data == "+":
            a = stack_class.stack_pop()
            b = stack_class.stack_pop()
            stack_class.stack_push(a+b)
        elif input_data == "*":
            a = stack_class.stack_pop()
            b = stack_class.stack_pop()
            stack_class.stack_push(a*b)
        elif input_data == "=":
            return(stack_class.stack_pop())
        else:
            stack_class.stack_push(int(input_data))


if __name__ == "__main__":
    stack_class = d_stack.stack(10)
    rslt = reverse_polish(stack_class)

    print(rslt)