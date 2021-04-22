#Write Python code that asks a user how many pizza slices they want.
#The pizzeria charges Rs 123.00 a slice
#if user order even number of slices, price per slice is Rs 120.00
#Print the total price depending on how many slices user orders.
no_of_slices=int(input("Enter no of slices:"))
if(no_of_slices%2==0):
    print(no_of_slices*120)
else:
    print(no_of_slices*123)