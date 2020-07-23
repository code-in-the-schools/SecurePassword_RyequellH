passcode = str(input("Enter a custom passcode:  "))




c = "Quell/1204"
found = False
while found == False:
  d = str(input("Please enter your 8-16 digit passcode"))
  if d==c:
    found = True
    print("access granted")
else:
  print("Wrong passcode")
v 


