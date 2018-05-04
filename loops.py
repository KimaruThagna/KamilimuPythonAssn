#Q1 ex 2.2
#Thagana K Mark
for i in range(10):
    print((1/(i+1)))

#Q2
num=input("Enter a number")
num=abs(int(num))
while(num!=0):
    print(num)
    num = num - 1

#Q3
exp=input("Enter exponent")
base=input("Enter base")
x=1
for _ in range (int(exp)):
    x=int(base)*int(x)

print(x)

#@Q4
number=input("Enter a value")
while((int(number)%2)!=0):
    print("Try again. The number is not divisible by 2")
    number = input("Enter a value")
if (int(number)%2)==0:
    print("Finally, a number dibisible by 2")