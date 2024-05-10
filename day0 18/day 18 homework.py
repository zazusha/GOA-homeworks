# first work



numbers=[]

for i in range(5):
    sum=(int(input("tell me 5 number: ")))
    numbers.append(sum)
 
num=0
for sum in numbers:
    num=num+sum
print(num)


# second work

lst=[1,2,14,6,7,8,9,22,10]

biggest=lst[0]

for numbers in lst:
    if biggest < numbers:
        biggest=numbers
      
print(biggest)      

#third work


numbers=[]

for i in range(30,50+1):
    if i % 2 !=0:
        numbers.append(i)

print(len(numbers))        

#forth work

nums=[]

for i in range(12,50+1,4):
    nums.append(i)


reversed_lst=[]

for numbers in range(len(nums)-1,-1,-1):
    reversed_lst.append(nums[numbers])



print(nums)
print(reversed_lst)


# fifth work



numss=[]

for i in range(50,100):
      numss.append(i)


even_numbers=[]


for number in range(0,len(numss)):
      if numss[number] %2==0:
             even_numbers.append(str(numss[number])+"-"+str(number))
                
print(numss)
print(even_numbers)                