#workout schedule dd

required_pushups=40
required_lift=30



pushups=int(input("how many pushups have you done?: "))
lift=int(input("how many did you lift: "))
#and 
print(lift==required_lift and pushups == required_pushups)
print(lift<required_lift and pushups > required_pushups)
print(lift>required_lift and pushups < required_pushups)
print(lift>required_lift and pushups > required_pushups)
print(lift<required_lift and pushups < required_pushups)
#or 
print(lift==required_lift or pushups ==required_pushups)
print(lift<required_lift or pushups <required_pushups)
print(lift>required_lift or pushups >required_pushups)
print(lift>required_lift or pushups <required_pushups)
print(lift<required_lift or pushups >required_pushups)

#we must ask how much they weight andhow tall are they and 
#see if it is True or false
required_weight=50
required_height=170

weight=int(input("how much do you weight?: "))
height=int(input("how tall are you?: "))

#and 
print(weight==required_weight and height == required_height)
print(weight>required_weight and height > required_height)
print(weight<required_weight and height < required_height)
print(weight>required_weight and height < required_height)
print(weight<required_weight and height > required_height)
#or
print(weight==required_weight or height == required_height)
print(weight>required_weight or height > required_height)
print(weight<required_weight or height < required_height)
print(weight>required_weight or height < required_height)
print(weight<required_weight or height > required_height)



