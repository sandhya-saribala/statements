#print second prime of the given number
num=int(input("enter a number:"))
count=0
check=num+1
while True:
    divisible=0
    for i in range (1,check+1):
        if check%i==0:
           divisible+=1
    if divisible==2:
        count+=1
        if count==2:
            print(check)
            break
    check+=1
#break the loop if condition matches with the given number
given_number=5
for i in range(1,11):
    if i==given_number:
        continue
    print(i)
#print numbers from 1 to 100 but it should not print multiples of 3
for i in range(1,101):
    if i%3==0:
      continue
    print(i)

