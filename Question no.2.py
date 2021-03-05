num1=[]
num2=[]
size1=int(input("Enter the size of num1 = "))
print("\n Enter the elements of num1 \n")
for i in range(0,size1):
    element_of1=int(input())
    num1.append(element_of1)

size2=int(input("\n Enter the size of num2 = "))
print("Enter the elements of num2 \n ")
for i in range(0,size2):
    element_of2=int(input())
    num2.append(element_of2)
Output=list(set(num1) & set(num2))
print(f'Output :{Output}')

