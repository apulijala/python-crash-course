def max_product(A):
    A.sort()
    n = len(A) -3 
    # Set the maximum to the least possible value. 
    maximum = -10000
    i = 0
    while i <= n:
        triplet_product = A[i] * A[i+1] * A[i + 2]
        if triplet_product > maximum:
            maximum = triplet_product
        i =  i + 1
    
    return maximum



def max_product_negative(A):
    # gather all negavtive integers here. 
    positve_max = -100000
    negative_max = -100000

    negative_a = []
    positive_a = []
    
    for i in A:
        if i < 0:
            negative_a.append(i)
            # A.remove(i) # This is causing problems.
        else:
            positive_a.append(i)

    
    # Sort both the arrays. 
    negative_a.sort()
    positive_a.sort()
    print(positive_a)
    print(negative_a)
    pos_length = len(positive_a)
    neg_length = len(negative_a)
    # print(A)
    # print(negative_a)


    if pos_length >= 3:
        positve_max = positive_a[pos_length-3]*positive_a[pos_length-2]*positive_a[pos_length-1]
        if neg_length >= 2:
            negative_max = negative_a[0]*negative_a[1]*positive_a[pos_length-1]
    elif pos_length == 2: # There must be atleast one -ve integer.
        positve_max = positive_a[pos_length-2]*positive_a[pos_length-1]
        if neg_length >= 2:
            negative_max = negative_a[0]*negative_a[1]*positive_a[pos_length-1]
        # Positives need to be combined with at least one enegave. 
        positve_max = positve_max*negative_a[neg_length-1]
    elif pos_length == 1:
        return positive_a[0]*negative_a[0]*negative_a[1]
    elif pos_length == 0:
        return negative_a[pos_length-3]*negative_a[pos_length-2]*negative_a[pos_length-1]
    
    if positve_max > negative_max:
            return positve_max
    else:
            return negative_max
    


   