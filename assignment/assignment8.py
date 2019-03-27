passw=input("Enter a password : ")
try:
    assert len(passw)>8,"Invalid password"
    print("You logged in")
except AssertionError as obj:
    print()