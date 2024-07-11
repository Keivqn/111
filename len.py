def count(string):
    chrt={}
    
    for char in string:
        if char in chrt:
            chrt[char]+=1
        else:
            chrt[char]=1
    
    return chrt

x=input(str("please enter your sentence:"))

y=count(string=x)

print(y)
