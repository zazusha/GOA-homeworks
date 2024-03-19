#number detector

# number=int(input("tell me any kind of number: "))


# if number >0:
#     print("its spositive number")
# if number ==0:
#     print("number is equal to zero")    
# if number < 0:
#     print("number is negative")

#write algoritm where we give user 2 suggestion:


# print("chooce between kilometer-mile or mile-kilometer,type 1 or 2 to choose: ")
# km_ml=int(input())
# number=(int(input("now tell me number: ")))

# if km_ml!=1:
#    number=number * 1.609344
#    print(number)
# if km_ml !=2:
#     number=number / 1.609344
#     print(number)     
    

#register algorithm:


# print("for registration you need to: ")
# name=input("tell me your name: ")
# surname=input("tell me your surname: ")
# age=input("tell me your age: ")
# email=input("tell me your Email: ")


# print("conrgatulations!",name,surname,"you passed registration.your age is ",age,"and Email is",email)

# Arithmetic average

# num1=int(input("tell me number: "))
# num2=int(input("tell me number: "))
# num3=int(input("tell me number: "))

# result=(num1+num2+num3)/3

# print(result)

#text 5:

# number=int(input("tell me number between 1--9: "))


# for nubmer in range(1,50):
#     number=number*2
#     print(number)

#text 6:

# num1=int(input("tell me number: "))
# num2=int(input("tell me number: "))
# i=num2-num1  
# for i in range(num1,num2):
#     i=i*i*i
        
# print(i)    

# text 7:

# num=int(input("tell me number: "))

# x1=num
# x2=num*2
# x3=num*3
# x4=num*4
# x5=num*5
# x6=num*6
# x7=num*7
# x8=num*8
# x9=num*9
# x10=num*10

# print(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10)

# text8

# num1=int(input("tell me number: "))
# num2=int(input("tell me second number: "))
# choice=int(input("chooce between +,-,/,*  to choose type 1,2,3 or 4: "))

# if choice !=1:
#     plus=num1+num2
#     print(plus)
# if choice !=2:
#     minus=num1-num2
#     print(minus)
# if choice !=3:
#     division=num1//num2 
#     print(division)
# if choice !=4:
#     multiplication= num1*num2  
#     print(multiplication)         


# text 9

# str=input("tell me anything : ")
# repeat=int(input("how many time do you want to repeat? :"))

# for i in range(repeat):
#     print(str)

# text 10

# height=int(input("please tell me how tall are you: "))
# weight=int(input("please tell how much you weight: "))
# BMI=(height/weight*weight)*703
# print(BMI)


# text 11

# number=int(input("tell me any number between 1--5: "))

# if number in range(1,5):
#     print("valid input")
# else:
#     print("invalid input")    


#ეს დავალება გამომრჩა სადღაც 5 დავალებაა :

b=int(input("tell me any number: "))

for a in range(b):
    b=a,a+1
    print(b)