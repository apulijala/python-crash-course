def solution(N):
    bin_str = get_binary_string_from_num(N)
    # print("binary string", bin_str)
    start = 0
    maxlen = 0
    while True:
        try:
            start = bin_str.index("1", start)
            # because of test cases i can do this
            # tosearch = start  + 1
            nextone = bin_str.index("1",start  + 1)
            length = (nextone - start) - 1
            if length > maxlen:
                maxlen = length
            # print(f"start={start}",f"nextone={nextone}", f"length={length}" )
            # start = nextone +1. this one took the nextone to next start off. 
            start = nextone 
        except ValueError as ve:
           break
    return maxlen
        

    

def get_binary_string_from_num(N):
    return bin(N)
    """
    q = N # This is imporant as it reduces.
    (q,r) = divmod(q,2)
    binstr = ""
    binstr = str(r) + binstr
    while q != 0:
        (q,r) = divmod(q,2)
        binstr = str(r) + binstr
    return binstr
    """
