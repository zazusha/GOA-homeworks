
# first work

# lst=[1,2,3,4,5,6,7,8]

# multiplication=lst[0]

# for number in lst:
#     multiplication=multiplication*number

# print(multiplication)    

#second work

# lst=[1,-1,2,3,4,5,-9,8,6,-7]

# negative_numbers=lst[0]

# for i in lst:
#     negative_numbers < 0
#     lst.append(i)

# print(lst)       
 

# es ver gavige



number=[]

for number in range(6):
    print(int(input('please tell me 5 number: ')))

sashualo=0

for i in number:
     i=(i+sashualo) % 3
    number.append(i)

print(sashualo)