#****Input and Output
#****Output
#****Data Type
#1.int (จำนวนเต็ม) -> 5,10 %d
#2.string (Text) -> "Hello World" %s
#3.float (ทศนิยม) -> 5.5,1.3 %f

#****Input
def ex01():
    print(type("15"))    #Command is used to check the data type
def ex02():              #****String can connected together with sign "+"
    print("15" + "2")    #example print("15" + "2") the out come will be "152"
def ex03():              #**** use sign "*" with string => it means การทำซ้ำ
    print("15" * 3)      #example print("15" * 3) the outcome will be 151515

#Output
def ex04():
    a = input()          #When you click run, nothing will be happen except you can just typing anything. But nothing will be happen.

def ex05():
    a = input("What is your name: ")         #In the parentisis you can type for telling the user what do you want them to do
    print(a)            #When you fill the data, the result will be shown.

def P01():
    a = int(input("What is your number: "))         #In the parentisis you can type for telling the user what do you want them to do
    if a == "1":
        print("number is 1")
    print(type(a))            #When you fill the data, the result will be shown.

def ex06():
    a = input()
    print(type(a))      #The result will always be string forever.

#****How to change the data type
# a = B(input())  => When B is the datatype that we want to change
def ex07():
    a = int(input())
    print(type(a))

def ex08():
    a = int(input())
    b = int(input())
    print(a + b)

def ex09():
    a = "Hello"
    print("%s" % a)  #=> s means string
                     # %s means เราจะเอาตัวแปรที่เป็นstringมาแทนที่นะ แล้วตามด้วย % แล้วก็ตามด้วยตัวแปรที่เราต้องการจะเอามาแทน
                     # print("%s" % a) = print("Hello")
def ex10():
    print("%s, %s %s" % ("Hello", "Python", "is easy"))
def ex11():
    a = 5
    print("a is %d" % a)  # %d means integer or number
def ex12():
    a = 5
    print("a is %f" % a)  # %f means float (ทศนิยม)
def ex13():
    a = 5
    print("a is %.2f" % a)  # ใช้ในกรณีที่เราต้องการทศนิยมแค่ 2 ตำแหน่ง
def ex14():   # want to see the result a = 5 and b = 10
    a = 5
    b = 10
    print("a = %d and b = %d" % (a,b))
def ex15():  #For calculating the cost
    cost = float(input("Cost: "))
    profit = int(input("Profit: "))
    cal = (cost / (100 - profit)) * 100
    print("You should sell %.2f Bath" % cal)
def ex16():
    a = str(input("Your Name: "))
    print("Hello %s" % a)
    b = input("what is your number: ")
    print("Number is", b)

#About Error
'''Syntax Error => grammar or patern Wrong
   EOF = end of file (the last (line of the file or code <I'm not sure>) that you write the code is wrong of systax or structure)'''
#Variables
'''ถ้าค่าของตัวแปรเท่ากันสามารถประกาศไปทีเดียวเลยก็ได้ เช่น
   a = b = c = 3
   print(a)
   print(b)
   print(c)
   The result will be:
   3
   3
   3'''
def ex17():
    price = float(input("Price: "))
    discount_percent = int(input("Discount(%): "))
    discount_baht = discount_percent / 100 * price
    payment = price - discount_baht
    print("Discount(baht): %d" % discount_baht)
    print("Payment: %d" % payment)
def ex18():                        #Set Example
    a = {"dog", "cat", "hamster"}
    b = {"bird", "dog", "zebra"}
    c = a.intersection(b)
    print(c)
#Data Type: Dictionary
def ex19():                  #Dictionary Example
    person = {
        "name": "Mark",            #"key": "value"
        "old": 18,
    "favorite": "cartoon"
    }
    print(person["favorite"])
def ex20():
     a = 10 < 3               #Boolean Example

#Math
def ex21():
    print(min(1,3,5,10))
    print(max(2,4,5))
    print(abs(-41))
    print(pow(4,3)) #4ยกกำลัง3
    #อันไหนที่มี "math.___" ให้ใช้command "import math" ขึ้นก่อน
    import math
    print(math.sqrt(16))
    print(math.ceil(4.3))    #พิมพ์ไรมาก็ปัดขึ้นตลอด
    print(math.floor(4.3))   #พิมพ์ไรมาก็ปัดลงตลอด
    print(math.pi)           #หาค่าpi

#Booleans(TRUE and FALSE)
def ex22():
    print(15 > 2)           #The answer will be TRUE
    print(15 == 2)          #The answer will be FALSE
    print(not(15 == 2))     #The answer will be TRUE (because false and false = TRUE)
    print(type(True))       #The result will be 'bool' ('bool' is booleans)
    print(bool(""))         #print(bool(_)) => ใช้สำหรับเชคค่าว่าเป็นจริงหรือเป็นเท็จ(อะไรที่เป็น0จะเป็นเท็จหมด and (""))
    print(bool(0))
    print(bool(200))
    print(bool(" "))
    print(bool("Hello"))

#If...else
def ex23():
    n = int(input())
    if n % 2 == 0:
        print("%d is even" % n)
    else:
        print("%d is odd" % n)
def ex24():
    salary = int(input("salary: "))
    if salary >= 15000:
        if salary < 70000:
            print("Silver")
        elif salary < 10000:
            print("Golden")
        elif salary >= 100000:
            print("Platinum")
    else:
        print("No\nrequire salary is at least 15000")
def ex25():
    m = int(input("Month: "))
    d = int(input("Day: "))
    if m % 3 == 0:
        if d < 21:
            if m == 1 or m == 2 or m == 3:
                print("Winter")
            elif m == 4 or m == 5 or m == 6:
                print("Spring")
            elif m == 7 or m == 8 or m == 9:
                print("Summer")
            elif m == 10 or m == 11 or m == 12:
                print("Fall")
        else:
            if m == 1 or m == 2 or m == 3:
                print("Spring")
            elif m == 4 or m == 5 or m == 6:
                print("Summer")
            elif m == 7 or m == 8 or m == 9:
                print("Fall")
            elif m == 10 or m == 11 or m == 12:
                print("Winter")
    else:
        if m == 1 or m == 2 or m == 3:
            print("Winter")
        elif m == 4 or m == 5 or m == 6:
            print("Spring")
        elif m == 7 or m == 8 or m == 9:
            print("Summer")
        elif m == 10 or m == 11 or m == 12:
            print("Fall")

#While loop
def ex26():           #0-10
    i = 0
    while i <= 10:
        print(i)
        i += 1
def ex27():           #0-10 except5
    i = 0
    while i <= 10:
        if i == 5:
            i += 1
            continue   #continueตัวนี้คือการข้ามการทำงานของลูปในรอบนั้นซึ่งก็คือ5
        print(i)
        i += 1
#while true/infinite loop/ ลูปที่ไม่สิ้นสุด
def ex28():
    while True:
        n = int(input())
        if n == -1:
            break
#รับค่าจำนวนเต็มแล้วหาค่าเฟคทอเรี่ยลของจำนวนนั้น
def ex29():
    n = int(input())
    i = n
    summ = 1
    while i >= 1:
        summ *= i
        i -= 1
    print(summ)

#รับค่ามา5ค่าแล้วหาผลรวม
def ex30():
    i = 1
    summ = 0
    while i <= 5:
        n = int(input())
        summ += n
        i += 1
    print(summ)

#Nested While => loopซ้อนloop =>จะทำลู)ในให้เสร็จแล้วค่อยไปทำลูปนอก
def ex31():
    i =1
    while i <= 5:
        print("round: %d" % i)
        j = 1
        while j <= 3:
            print(j)
            j += 1
        i += 1
#Random number game
def ex32():
    import random
    tarket = random.randint(0,10)
    count = 0
    while True:
        n = int(input("Enter a number between 0-10: "))
        count += 1
        if n < tarket:
            print("The number is too low")
        elif n > tarket:
            print("The number is too high")
        else:
            print("----------You Win----------")
            break
    print("You try %d times" % count)

#loop for
def ex33():
    for i in range(6):     # => for i in range (0,6,1) / เวลากำหนดตัวหยุดให้บวกหนี่งเสมอ
        print(i)
def ex34():
    i = 0                      #This line is so useless in for loop because the value of i is determined in the "for i in range___" line
    for i in range(1,10,2):
        print(i)
def ex35():
    for i in range(10,-1,-1):
        print(i)

#String
def ex36():
    print("\"OMG\"")
    print('"OMG"')
    print("\"I'm Mark\"")
    print('"I\'m Mark"')
def ex37():
    a = """Hello
I'm Mark
    Nice to meet you"""
    print(a)
def ex38():
    a = "Hello World"
    print(a[-2])
    print(a[9])
def ex39():
    a = "python programming"
    print(a[0:6:1])
    print(a[:6])      #เหมือนกับprint(a[0:6:1])
    print(a[:6:2])    # => print(a[0:6:2])
    print(a[7:18])    #เหมือนกับprintprint(a[7:])
    print(a[7:])      #เริ่มที่7จนถึงสิ้นสุด
    print(a[7:18:2])
    print(a[7::2])    #เหมือนกับprint(a[7:18:2])
    print(a[-11:-4])
    print(a[:])
    print(a[::2])
def ex40():
    if "3" in "12345":
        print("yes")
def ex41():
    if "c" not in "hello":
        print("yes")
def ex42():
    for x in "Hello":
        print(x)
def ex43():
    a = "Nichakorn"
    for x in a:
        print(x, end="")
def ex44():
    a = "hello"
    print(len(a))
def ex45():
    a = "hello"
    print(a[len(a) - 1])
    print(a[-1])
    print(a[4])
def ex46():
    a = "Hello"
    for i in range(len(a)):
        print(a[i])



#Linked List
#create Node
class Student:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    def display(self):
        return self.name + ' ' + self.surname
def P02():
    nichakorn = Student('Nichakorn','Napat')
    print(nichakorn.display())
