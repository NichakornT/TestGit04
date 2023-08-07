def N01():
    from PIL import Image
    im = Image.open("C:/Users/WiN 10 Pro/ImageDataStructure/barbatos.png")
    print(im)

def N02():
    from PIL import Image
    m1= Image.open("C:/Users/WiN 10 Pro/ImageDataStructure/barbatos.png")
    type(m1)
    print(type(m1))
    print(m1.size)   #size of picture width and lenght
#How to convert images to Numpy array
def N03():
    from PIL import Image
    from numpy import asarray
    im = Image.open("C:/Users/WiN 10 Pro/ImageDataStructure/barbatos.png")
    numpydata = asarray(im)
    print(numpydata)

def N04():
    mylist = "A           VEHG"
    print(len(mylist))
    print(mylist[0])
    print(mylist[15])

#FindMax CaseStudy
import random
from time import time

def find_max1():
    num = 2000000
    i = 0
    my_list = []

    while i < num:
        my_list.append(random.randint(0, 10))
        i += 1

    #print(my_list)

    # FIND_MAX1
    max1 = 0
    for x in my_list:
        if x > max1:
            max1 = x

    print('Max is ', max1)

def find_max2():
    num = 2000000
    i = 0
    my_list = []

    while i < num:
        my_list.append(random.randint(0, 10))
        i += 1

    #print(my_list)
    max2 = 0
    score_list = [10,9,8,7,6,5,4,3,2,1,0]
    for s in score_list:
        if my_list.count(s) > 0: # s is in the my_list or not
            max2 = s
            break
    print("(2)Max is ", max2)

def run():

    start_time = time()  # record the starting time
    find_max1()
    end_time = time()  # record the ending time
    elapsed_time = end_time - start_time
    print(elapsed_time)

    start_time2 = time()  # record the starting time
    find_max2()
    end_time2 = time()  # record the ending time
    elapsed_time2 = end_time2 - start_time2
    print(elapsed_time2)

def test01():
    mytext = "Python is the great language. I love Python"

    # ค้นหาตั้งแต่อักษรตัวที่ 5 ถึงตัวที่ 43
    x = mytext.count("Python", 5, 43)

    print(x)
    # x จะมีค่าเป็น 1 เพราะเจอคำว่า Python 1 ครั้ง

#link list
message2 = 'Sawasdee'

class Account:
    def __init__(self,account_name,opening_balance):
        self.account_name = account_name
        self.balance = opening_balance
    def display(self):
        #Balance Inquiry
        return self.account_name + ' ' + f"{self.balance:,.2f}"
    def setAccountName(self, new_name):
        self.account_name = new_name


def hello2():
    message = 'Hello2'
    print(message)
def hello():
    print('Hello World')
    s = 1
    print(message2)

    jane_account = Account('Jane',1200.00)

    print(jane_account.account_name)
    print(jane_account.display())

    jane_account.setAccountName('Jane2')
    print(jane_account.display())

def sum1(num):
   sum = 0
   # [1, 2 , 3, 4, 5]
   for x in range(1, num+1):
       sum += x
   return sum


def sum2(num):
   if num == 0:
       return 0
   elif num == 1:
       return 1
   else:
       return num + sum2(num - 1)
   # 5 + 4 + 3 + 2 + 1


def factorial(num):
   if num == 0:
       return 1
   elif num == 1:
       return 1
   else:
       return num * factorial(num - 1)
   # 5 * 4 * 3 * 2 * 1


def run():
   #print(sum2(10))
   print(factorial(7))


   score1 = 87
   score2 = 45
   score3 = 61
   average = (score1+score2+score3)/3


   mylist = [3, 7, 6, 9, 8, 3]


   mylist2 = []
   mylist2.append(3)
   mylist2.append(7)
   mylist2.append(6)


   C = 'c'
   mylist3 = ['A','B', C ]
   #String


   mystring = 'This is a book'


   print('Number of chars is ', len(mystring))
   print(len(mylist3))
#Example of using return
def plus( a ):
    return a + 1

class MyClass:
    def plus( b ):
        return b * 2

print( 'Function plus return '+str(plus( 10 )) )

myClass = MyClass
x = myClass.plus( 2 )
print( 'Method plus in class MyClass return '+str(x) )
###
#take user input
String = input('Enter the string :')
count = 0
#to check for less conditions
#keep string in lowercase
String = String.lower()
for i in String:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        #if True
        count+=1
#check if any vowel found
if count == 0:
    print('No vowels found')
else:
    print('Total vowels are :' + str(count))
##Prime number
print("input:")

# input creates a list of numbers divided by a space
n = list(map(int, input().split()))


def prime(x):  # False if x is not a prime number, True if x is a prime number
    for i in range(2, x):
        if abs(x) % i == 0:
            return False
        else:
            return True


def longest_decreasing_sequence(n):

    # lds[] is longest list of decreasing numbers; current[] is the current list of decreasing numbers in the cycle
    lds, current = [], [n[0]]
    for val in n[1:]:  # takes values from the list from item 1 to input list end
        if val < current[-1]:  # decreasing test
            current.append(val)  # add it to lds[] list

        else:
            if len(current) > len(lds):  # update lds[] if current[] has more items
                lds = current[:]

            elif len(current) == len(lds):  # if current[] has equal items compare sums
                if sum(current) > sum(lds):  # if sum of current[] > sum of lds[]
                    lds = current[:]  # update lds[] list

            else:
                lds
            # sets current to value where decreasing sequence test failed
            current = [val]

    if len(current) > len(lds):  # if current[] has more items, update lds[]
        lds = current[:]

    else:
        lds
    return lds


print("lds:", longest_decreasing_sequence(n))
print("length:", len(longest_decreasing_sequence(n)))
print("sum:", sum(longest_decreasing_sequence(n)))