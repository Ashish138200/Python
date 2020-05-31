#REGEX
import re
phnNo = input()
email = input()
mo = re.compile(r'''
(\+91)? #country code
(\d{10})
''',re.VERBOSE)

mo1 = re.compile(r'''
(\w{1,10}(\.)?\w{0,10})  
(@)
(gmail|hotmail|rediff|gla)
(\.)?
([a-zA-z])?
(\.)
([a-zA-z])
''',re.VERBOSE|re.I)   # [a-zA-Z_.+]+
if mo.search(phnNo):
    print("You've entered a valid phone number")
else:
    print("Invalid phone number")
if mo1.search(email):
    print("You've entered a valid Email address")
else:
    print("Invalid Email Address")