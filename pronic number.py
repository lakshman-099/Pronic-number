import math
def findPronic(x):
    i=0
    while(i<=(int)(math.sqrt(x))):
        
        if(x==i*(i+1)):
            return True
        i=i+1
    
    return False
    
i=0
while(i<=200):
    if findPronic(i):
        print (i)
    i=i+1
