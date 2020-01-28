username = input("Enter your username : ")
password = input("Enter your password : ")
if username =="Priyesh" and password == "password":
  print("Entered the System")
elif username =="Priyesh":
  print("Password donot match")
elif password == "password":
  print("Username donot Exist")
elif username !="Priyesh" and password != "password":
  print("Invalid credentials")