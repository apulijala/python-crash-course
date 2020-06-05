def brackets(nested_str):

    if nested_str == "":
        return 1

    my_stack = []
    str_hash = {
        '}' : '{',
        ']' : '[',
        ')' : '(' 
    }

    for i in range(0, len(nested_str)):
        if nested_str[i] == '{' or nested_str[i] == '[' or nested_str[i] == '(':
            my_stack.append(nested_str[i])
        else:
            str_at_i = nested_str[i]
            if len(my_stack) <=0:
                return 0
            popped_str = my_stack.pop()
            if str_hash[str_at_i] != popped_str:
                return 0
    
    if len(my_stack) == 0:
        return 1
    else:
        return 0


def brackets_only_one_type(nested_str):

    if nested_str == "":
        return 1

    my_stack = []
    str_hash = {
        ')' : '(' 
    }

    for i in range(0, len(nested_str)):
        if nested_str[i] == '{' or nested_str[i] == '[' or nested_str[i] == '(':
            my_stack.append(nested_str[i])
        else:
            str_at_i = nested_str[i]
            if len(my_stack) <=0:
                return 0
            popped_str = my_stack.pop()
            if str_hash[str_at_i] != popped_str:
                return 0
    
    if len(my_stack) == 0:
        return 1
    else:
        return 0