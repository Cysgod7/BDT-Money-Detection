import os
count = 880

for i in os.listdir():
    os.rename(i,str(count)+ '.'+ i.split('.')[-1])
    count+=1