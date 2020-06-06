class Stack():
    def __init__(self):
        self.stack = []

    def returnCurrentValue(self):
        return self.stack[-1]

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        element = ""
        if self.empty() == False:
            element = self.stack.pop()
        return element

    def size(self):
        return len(self.stack)

    def empty(self):
        # print("length ", len(self.queue))
        return len(self.stack) == 0


def fish_attack(A, B):

    n = len(A)
    fish_queue_1 = Stack()
    fish_queue_0 = []
   
    for i in range(0,n):
        if B[i] == 1:
            fish_queue_1.push(A[i])
        elif B[i] == 0:
            while fish_queue_1.empty()  == False:
                if fish_queue_1.returnCurrentValue() > A[i]:
                    break
                else:
                    fish_queue_1.pop()
            
            if fish_queue_1.empty()  == True:
                fish_queue_0.append(A[i])

    return fish_queue_1.size() + len(fish_queue_0)


"""
A = [0, 1]
B = [1, 1]
result = fish_attack(A, B)
print("result is ", result)
"""

A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
result = fish_attack(A, B)
print("Result is ", result)

