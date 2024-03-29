age=int(input("tell me your age: "))

if age <18:
    print("you are young")
elif age<50:
    print("you are old") 
else:
    print("you are too old")

#first method is working but we must use "and" code i guess )

age=int(input("tell me your age: "))

if age>0 and age<18:
    print("you are young")
elif age>=18 and age <50:
    print("you are old") 
else:
    print("you are too old")
        
   


num=int(input("tell me number: "))

if num > 0:
    print("this number is positive")
elif num <0:
    print("number is negative")
else:
    print("number equals 0")        

