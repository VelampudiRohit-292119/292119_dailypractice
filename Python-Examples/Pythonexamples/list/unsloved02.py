#Write a Python program to change the position of every n-th value with the (n+1)th in a list
def posi_swap(list):
    for i in range(0,len(list),2):
        list[i],list[i+1]=list[i+1],list[i]
    return list

list=[0,1,2,3,4,5]

print(posi_swap(list))