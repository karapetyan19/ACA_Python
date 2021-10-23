# The Goldbach Conjecture
import math

def number_is_prime(a):
    if a == 1:
        return False
    b = round(math.sqrt(a))
    for i in range(2,b+1):
        if a % i == 0:
            return False
    else:
        return True
    
def goldbach_conjecture(n):
    for i in range(2, n//2+1):
        if number_is_prime(i) and number_is_prime(n-i):
            return i, n-i
    


n = int(input())
print(goldbach_conjecture(n))


# Palindrome numbers
def number_is_palindrome(n):
    digits = list(str(n))
    for i in range(len(digits)//2):
        if digits[i] != digits[len(digits)-i-1]:
            return False
    else:
        return True

    
a=int(input())
b=int(input())
for n in range(a,b):
    if number_is_palindrome(n):
        print(n)

        
        
# Suffix Sums
def suffix_sums(acc):
    sequence = []
    for i in range(len(acc)):
        sequence.append(sum(acc[i:]))
    return sequence
    
    
acc = [float(i) for i in input().split(" ")]
suffix_sums(acc)



# Cyclic shift
def cyclic_shift(sequence, k):
    k = k% len(sequence)
    return sequence[-k:]+sequence[:-k]
        
    
    
n = int(input())
k = int(input())
sequence = [int(input()) for _ in range(n)]
print(cyclic_shift(sequence, k))



# tree
def tree(n):
    for i in range(1,n+1,2):
        j = (n-i)//2
        print(" "*j, "*"*i)
    
    

n= int(input())
A = tree(n)


