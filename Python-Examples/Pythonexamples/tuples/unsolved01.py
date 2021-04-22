#Write a Python program to find the repeated items of a tuple
tuplex = (1,2,3,4,4,1,3,5,6,7,8,9,9,0,1,0)
unique = []
for item in tuplex:
    if(tuplex.count(item)>1):
        if not item in unique:
            unique.append(item)
print(unique)       
         
