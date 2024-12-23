"""
Take a student's marks as input. If the marks are more than 50, check if they are
greater than 90. If so, print "Excellent". If between 51 and 90, print "Good".
Otherwise, print "Fail".
"""
marks_data = float(input("Enter the student's marks: "))
if marks_data > 50:
    if marks_data > 90:
        print("Excellent")
    else:
        print("Good")
else:
    print("Fail")