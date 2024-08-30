# ---> Python Conditions and If statements
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

# If statement, without indentation (will raise an error)

marks = int(input("Enter Student Marks : "));

if(marks >= 90 and marks <=100) : 
    grade = "A";
elif(marks >= 80 and marks <90) :
    grade = "B";
elif(marks >= 70 and marks <80) :
    grade = "C";
elif(marks >= 60 and marks <70) :
    grade = "D";
elif(marks >= 0 and marks <60) :
    grade = "F";
else :
    grade = "Wrong Input!!!\nEnter Marks Again";

print("Grade Of The Student : ", grade);