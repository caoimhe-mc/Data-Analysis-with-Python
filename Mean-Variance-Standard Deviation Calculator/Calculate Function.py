import numpy as np
def calculate(list):
    #error checking to ensure list is correct length
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    else:
        b = np.reshape(list, (3,3)) #produce 3x3 matrix
        answer = {} #create empty dictionary
        answer['mean'] = [b.mean(axis=0).tolist(), b.mean(axis=1).tolist(), b.mean().tolist()]
        answer['variance'] = [b.var(axis=0).tolist(), b.var(axis=1).tolist(), b.var().tolist()]
        answer['standard deviation'] = [b.std(axis=0).tolist(), b.std(axis=1).tolist(), b.std().tolist()]
        answer['max'] = [b.max(axis=0).tolist(), b.max(axis=1).tolist(), b.max().tolist()] 
        answer['min'] = [b.min(axis=0).tolist(), b.min(axis=1).tolist(), b.min().tolist()] 
        answer['sum'] = [b.sum(axis=0).tolist(), b.sum(axis=1).tolist(), b.sum().tolist()] 

    return answer
 
#test function
a = [0,1,2,3,4,5,6,7,8]
b = [9,1,5,3,3,3,2,9,0]
c = [2,6,2,8,4,0,1,]
print(calculate(b))
