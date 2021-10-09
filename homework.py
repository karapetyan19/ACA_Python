# Digit Sum 3
a=int(input())

print(a//100%10+a//10%10+a%10)



# Area of a right triangle
leg_1=int(input())
leg_2=int(input())

print(leg_1*leg_2/2)


# Arithmetic Progression 
a_1 = int(input())
a_2 = int(input())
n = int(input())

b = a_2 - a_1
print(a_1 + (n-1)*b)



# century from year
year=int(input())

print((year+99)//100)



# Two men

first_man_has_shot=int(input())
second_man_has_shot=int(input())

print(second_man_has_shot-1, first_man_has_shot-1)



# Knight’s Possible Moves
px=int(input())
py=int(input())

# It is guaranteed that
# for a given input cell all 8 moves exist.

print(px+2,py+1)
print(px+2,py-1)
print(px-2,py+1)
print(px-2,py-1)

print(px+1,py+2)
print(px+1,py-2)
print(px-1,py+2)
print(px-1,py-2)



