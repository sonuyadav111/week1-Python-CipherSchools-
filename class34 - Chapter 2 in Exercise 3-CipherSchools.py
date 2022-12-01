name, char= input("Enter comma seprated Name and Character :- ").split(",")
print(f"length of your name is {len(name)}")
print(f"character count: {name.lower().count(char.lower())}")