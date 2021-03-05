Input=[]
size=int(input("Enter the size of input: "))
print("Enter the elements of Input \n")
for i in range(0,size):
    element=int(input())
    Input.append(element)

res = Input[0]
for i in range(1,size):
    res=res ^ Input[i]


print(f'Output:{res}')    
