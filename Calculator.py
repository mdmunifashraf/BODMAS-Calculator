#12+13/14*24-23/12
exp=input("Enter the expression")
exp=exp+'!'
op=['/','*','+','-']
num=0
numbers=[]
operators=[]
for i in exp:
    if not i.isdigit():
        numbers.append(num)
        num=0
        operators.append(i)
    else:
        num=num*10+int(i)
operators.pop()

print(numbers)
print(operators)

k=0
for i in operators:
    if i=='/':
        numbers[k]= numbers[k]/numbers[k+1]
        numbers.pop(k+1)
        k=k-1
    elif(i=='*'):
        numbers[k]= numbers[k]*numbers[k+1]
        numbers.pop(k+1)
        k=k-1
    k=k+1

for i in operators:
    if i=='/' or i=='*':
        operators.remove(i)


k=0
for i in operators:
    if i=='+':
        numbers[k]= numbers[k]+numbers[k+1]
        numbers.pop(k+1)
        k=k-1
    elif i=='-':
        numbers[k]= numbers[k]-numbers[k+1]
        numbers.pop(k+1)
        k=k-1
    k=k+1
print(numbers[0])






