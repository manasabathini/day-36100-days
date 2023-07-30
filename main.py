listOfNames = []

def printList():
  print()
  for name in listOfNames:
    print(name)
  print()

while True:
  firstName = input("What is your First name?: " ).strip().capitalize()
  lastName = input("What is your Last name?: ").strip().capitalize()
  name = f"{firstName} {lastName}"
  if name not in listOfNames:
    listOfNames.append(name)
  else:
    print("ERROR: Duplicate name")
  printList()
  