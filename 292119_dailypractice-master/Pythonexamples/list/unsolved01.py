#Write a Python program to find the second smallest number in a list
a=[3,5,4,1,2]
a.sort(reverse=True)
a.pop(0)
print(a[0])