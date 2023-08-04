def run01():
    thelist= ["banana", "apple"]
    print(thelist)

def run02():
    a = input("what is your age?:")
    if a == "10":
        print("your age is 10.")
    elif a == "9":
        print("your age is 9.")
    else:
        print("your age is not 10.")

def run03():
    a,b = 1,0
    while a <= 10:
        b += a
        print(b)
        a += 1

def run04():
    a = "Nichakorn"
    b = 1
    for c in a:
        print("\nlistitem",b,"=",c)
        b += 1

def run05():
    for a in range(1,22,2):
        if a % 2 == 0:
            print(a,"is even number")
        else:
            print(a, "is odd number")

def run06():
    score = input("what is your score?:")
    score = int(score)
    if score >= 80 and score <= 100:
        print("score =", score, "grade is a")
    elif score >= 70 and score <= 79:
        print("score =", score, "grade is b")
    elif score >= 60 and score <= 69:
        print("score=", score, "grade is c")
    else:
        print("score =", score, "grade is d")
    print(type(score))