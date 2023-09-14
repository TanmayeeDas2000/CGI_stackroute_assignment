
# question 1
# intersection two list
def intersection(x, y):
    z = [value for value in x if value in y]
    return z

x = [1, 5, 3, 7, 2]
y = [6, 3, 7, 9, 8, 2]
print(intersection(x, y))



('''
# question 2
# count the words in string

x = input(" enter the string : ")
words = len(x.split())
print(" no of words are : ", words)
 ''')

('''
# question 3
# reverse a string
x = input("enter a string")
rev = x[::-1]
print("reverse is : ", rev)
 ''')

('''
# question 4
# largest element in the array
x = [12, 22, 10, 45]
x.sort()
print("largest element is : ", x[-1])
 ''')

('''
# question 5
# prime no
x = int(input("enter a no to check prime or not : "))
if x > 1:
    for i in range(2,x):
        if x % i == 0:
            print(x, " is not a prime no")
            break
        else:
            print(x, "this is prime")
            break
else:
    print(x, " is not a prime no")
 ''')

('''
# question 6
# merge two list
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
z = x+y
print("merged list : ", z)
 ''')