average=(90+85+70+75+80)/5
print(average)
if(average>90 and average<=100):
    print("A+")
elif(average>80 and average<=90):
    print("A")
elif(average>70 and average<=80):
    print("B")
elif(average>60 and average<=70):
    print("C")
elif(average>50 and average<=60):
    print("D")
elif(average<=50):
    print("F")
else:
    print("Error")
