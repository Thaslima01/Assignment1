x=int(input("enter the number"))
y=int(input("enter the number"))
i=x//10 #first digit of input x
j=x%10  #last digit of input x
a=y//10 #first digit of input y
b=y%10  #second digit of input y
sum=j*a+i*b
print(sum)
