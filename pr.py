number=input("Enter any natural number other than 1: ")
prime=[]
num=int(number)
for i in range(2,num+1):
    if num%i==0:
        for j in range(2,int(i/2)+1):
            if i%j==0:
               prime.append(j)
print("The set of prime factors for the given number is: ")
print(prime)