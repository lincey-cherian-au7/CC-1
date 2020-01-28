mark_1 = int(input("Enter the mark of subject_1: "))
mark_2 = int(input("Enter the mark of subject_2: "))
mark_3 = int(input("Enter the mark of subject_3: "))
mark_4 = int(input("Enter the mark of subject_4: "))
mark_5 = int(input("Enter the mark of subject_5: "))
percentage = (mark_1+mark_2+mark_3+mark_4+mark_5)/5
if percentage >=90:
  print("A grade")
elif 90>percentage>=70:
  print("B grade")
elif 70>percentage>=50:
  print("C grade")
elif 50>percentage>=30:
  print("D grade")
elif 30>percentage:
  print("E grade")
