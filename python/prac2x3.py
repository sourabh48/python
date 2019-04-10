a = int(input("Enter marks 1: "))
b = int(input("Enter marks 2: "))
c = int(input("Enter marks 3: "))
avg = (a+b+c)/3

if avg >= 60 :
    print ("A Grade")
elif avg >= 50 and avg <= 59 :
    print ("B Grade")
elif avg >= 40 and avg <= 49 :
    print ("D Grade")
elif avg < 40 :
    print ("Fail!")
