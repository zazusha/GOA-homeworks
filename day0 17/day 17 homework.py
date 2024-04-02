# homework: 1) შექმენით ლისტი სადაც ჩამოწერილიქნება თამაშის სახელები
#  და შემდგომ თამაშებს ვანაცვლებთ სოლოლერნით , w3 , codewars - ებით 
# და ასეშემდეგ.


# games=["god of war","league of legends",'valorant',]

# games[1]="sololearn"
# games[0]="w3"
# games[2]='codewars'

# print(games)

# 2)შექმენით 5 ინფუთი და ამ ინფუთებით შეადგინეთ სია, შემდეგ გამოიტანეთ ამ 
# სიიდან ლუწი რიცხვები, ისე რომ ლოგიკამ ყველა შემთხვევაში იმუშაოს


num1=int(input("tell me number: "))
num2=int(input("tell me second number : "))
num3=int(input("tell me third number: "))
num4=int(input("tell me  forth number: "))
num5=int(input("tell me fifth number: "))

lst=[num1,num2,num3,num4,num5]

print(lst)

if num1 % 2==0:
    print(num1)
if num2 % 2==0:
    print(num2) 
if num3 % 2==0:
    print(num3)
if num4 % 2==0:
    print(num4)    
if num5 % 2==0:
    print(num5)



