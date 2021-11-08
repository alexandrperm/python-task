A = [3,4,2,1,0,8,9,-1,100,0]
B = A[:]


min = A.pop()
max=min;
while A:
    a = A.pop()
    if a < min:
        min = a
        
    if a > max:
        max = a
    
        
print (min) 
print(B.index(min))

print (max) 
print(B.index(max)) 
