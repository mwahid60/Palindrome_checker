#Palindrome
x = input('type word :')

def Palindrome(x):
    return x == x[::-1]

pal = Palindrome(x)

if pal:
    print(x, 'is a Palindrome')
else :
    print(x, 'is not a Palindrome')
