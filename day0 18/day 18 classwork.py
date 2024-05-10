# num=[1,2,3,4,5,6,7,8,9,10,11,12]
# even=num[1::2]
# print(even)

# num1=[1,2,3,4,5,6,7,8,9,10]

# even=num1[1:10:2]
# print(even)


# დავალება: შექმენით პროგრამაც, სადაც გექნებათ ორი სია. პირველში 1-იდან 10-ის ჩათვლით დაამატეთ ლუწი რიცხვები, ხოლო მეორეში კენტები. გამოიყენეთ for ციკლი და append ფუნქცია


# შექმენით პროგრამა, სადაც მოხმარებელს შეეკითხებით ხუთ რიცხვს. ლუწები ერთ სიაში, ხოლო კენტები მეორეში დაამატეთ

even_numbers=[]
odd_numbers=[]

for i in range(1,5):
    print(int(input("tell me  numbers: ")))
    if i % 2==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print(even_numbers)
print(odd_numbers)            


# შექმენით პროგრამა სადაც გექნებათ ორი სია. პირველ სიაში 10-იდან 20-ის ჩათვლით ლუწი რიცხვები, ხოლო მეორეში კენტები დაამატეთ. საბოლოოდ გამოიტანეთ ამ სიების სხვაობა


# even_numbers=[]
# odd_numbers=[]

# for i in range(10,20+1):
#     if i % 2==0:
#         even_numbers.append(i)
#     else:
#         odd_numbers.append(i)

# print(even_numbers)
# print(odd_numbers)            
