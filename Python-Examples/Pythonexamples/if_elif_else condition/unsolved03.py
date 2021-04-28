#Write a python program to check if the input number is
#- real number
#- float numner
#- string
#- complex number
#- Zero (0)
num=input("Enter the number:")
if(num=='0'):
    print("Zero")
elif(num.find('+')!=-1):
    print("complex")
elif(num.isalnum()==True):
    print("string")
elif(num.find('+')==-1):
    if(num.find('.')>=1):
        print("float")
    else:
        print("real")
else:
    print("None of wanted")
    

