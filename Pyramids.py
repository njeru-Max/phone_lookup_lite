#1 normalpyramind
print("\nNormal Pyramid")
for i in range(5):
    x='*'
    x=x*(i+1)
    print(x)
    

#2 reverse pyramid
print("\nReverse Pyramid")
for i in range(5,0,-1):
    x='*'
    x=x*(i)
    print(x)
    
#3 full pyramid
print("\nFull Pyramid")
for i in range(5):
    x='*'
    x=x*(i+1)
    print(x.center(10))
    
#4 reverse full pyramid
print("\nReverse Full Pyramid")
for i in range(5,0,-1):
    x='*'
    x=x*(i)
    print(x.center(10))
    
#5 diamond shape
print("\nDiamond Shape")
for i in range(5):
    x='*'
    x=x*(i+1)
    print(x.center(10))  
    
#6 reverse diamond shape
for i in range(4,0,-1):
    x='*'
    x=x*(i)
    print(x.center(10))  
    
#7 hollow pyramid
print("\nHollow Pyramid")
for i in range(5):
    if i==0:
        x='*'
    elif i==4:
        x='*'*5
    else:
        x='*'+' '*(i-1)+'*'
    print(x.center(10))               