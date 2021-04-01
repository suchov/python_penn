# jsut a place to validate some python functions, validations ...

user_accounts = {'Bob': 'brandon123ABC', 'Brandon': 'brandon123ABCD'}

# print(user_accounts.get('Bob') is not None)

password = 'sd896ssfJJH'

if (any(x.isupper() for x in password) and any(x.islower() for x in password) 
    and any(x.isdigit() for x in password) and len(password) >= 8):
    print("Trooooper")

print(user_accounts['Bobb'])