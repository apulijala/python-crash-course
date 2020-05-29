def solution(N):
    flag = True
    bin_str = get_binary_string_from_num(N)
    print("binary string", bin_str)
    start = 0
    maxlen = 0
    while flag:
        try:
            start = bin_str.index("1", start)
            tosearch = start  + 1
            nextone = bin_str.index("1",tosearch)
            length = (nextone - start) - 1
            print(f"start={start}",f"nextone={nextone}", f"length={length}" )
            # start = nextone +1
            start = nextone 
            if length > maxlen:
                maxlen = length
        except ValueError as ve:
            flag = False
    return maxlen
        

    

def get_binary_string_from_num(N):
    q = N
    (q,r) = divmod(q,2)
    binstr = ""
    binstr = str(r) + binstr
    while q != 0:
        (q,r) = divmod(q,2)
        binstr = str(r) + binstr
    return binstr
