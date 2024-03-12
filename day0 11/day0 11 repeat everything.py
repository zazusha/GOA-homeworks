#example 1
name="zaza"
surname="gugeshashvili"
age=19
height=175
weight="79kg"

print("ჩემი სახელი და გვარია",name,surname,"ვარ",age,"წლის სიმაღლე",height,'სანტიმეტრი და წონა',weight,"კილოგრამი")
#2 example
name="anzori"
surname="davidovi"
age=20
height=179
weight="100kg"

print("ჩემი სახელი და გვარია",name,surname,"ვარ",age,"წლის სიმაღლე",height,'სანტიმეტრი და წონა',weight,"კილოგრამი")


#next lesson
#example 1

phone="iphone"
price=1000

discount=20
Total_price1=price-price*discount/100
print("total price of",phone,"with discount is:",Total_price1)


#example 2

product="creatine"
price=100

discount=5
total_price=price-price*discount/100
print("total price of",product,"whith discount is:",total_price)

#next lesson input and output
#example 1

neme=input("type your name: ")
surname=input("type your surname: ")
email=input("type your email: ")
password=input("type password: ")


print("congratulations",name,surname,"you succesfully completed registration <3")
#example 2

push_ups=input("tell me how many push ups have you done?: ")
height=input("how many did you height?: ")

print("congratulations you succefuly done",push_ups,"push ups and lifted",height,'kg')

#lesson with math tasks
#example

num=input("tell me 1 number: ")
sum=input("tell me another number: ")

print((num)+(sum))
print((num)-(sum))
print((num)*(sum))
print((num)/(sum))
print((num)//(sum))
print((num)%(sum))
print((num)>(sum))
print((num)<(sum))
print((num)==(sum))
print(float(sum))
print(float(num))
print(float(num)+1)
print((sum)+ "8")
print(float(num)+9)
print((sum)+3.5)

#example 2


num=int(input("tell me 1 number: "))
sum=int(input("tell me another number: "))

print((num)+(sum))
print((num)-(sum))
print((num)*(sum))
print((num)/(sum))
print((num)//(sum))
print((num)%(sum))
print((num)>(sum))
print((num)<(sum))
print((num)==(sum))
print(float(sum))
print(float(num))
print(float(num)+1)
print((sum)+ "8")
print(float(num)+9)
print((sum)+3.5)

#lesson Excess, deficiency and equality--- and,ro lesson, true or false ect...


required_age=20
required_height=175



age=int(input("how old are you?: "))
height=int(input("how tall are you?: "))
#and 
print(height==required_height and age == required_age)
print(height<required_height and age > required_age)
print(height>required_height and age < required_age)
print(height>required_height and age > required_age)
print(height<required_height and age < required_age)
#or 
print(height==required_height or age ==required_age)
print(height<required_height or age <required_age)
print(height>required_height or age >required_age)
print(height>required_height or age <required_age)
print(height<required_height or age >required_age)

#example 2



required_weight=78
required_time=4

weight=int(input("how much do you weight?: "))
time=int(input("how many month are you going to gym?: "))

#and 
print(weight==required_weight and time ==required_time )
print(weight>required_weight and time > required_time)
print(weight<required_weight and time < required_time)
print(weight>required_weight and time < required_time)
print(weight<required_weight and time > required_time)
#or
print(weight==required_weight or time == required_time)
print(weight>required_weight or time > required_time)
print(weight<required_weight or time < required_time)
print(weight>required_weight or time < required_time)
print(weight<required_weight or time > required_time)

#if statement 
#example 1

i=0

if i in range(0,100):
    print(i)


