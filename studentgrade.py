studentName = input("What's your name : ")
studentScore = int(input("what's your score?"))
if studentScore >= 90:
    grade = "A"
elif studentScore >= 80:
    grade = "B" 
elif studentScore >= 70:
    grade = "C"  
elif studentScore >= 60:
    grade = "D"   
else: grade = "F"   

print(f"{studentName}'s  grade is {grade}") 