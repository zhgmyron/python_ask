# -*- coding: UTF-8 -*-
users=['Admin','ron','jim','tim','allen']
new_users=['admin','len','frank']
if users:
    for user in new_users:
        if user in users:
            print("already exist")
        else:
            users.append(user)
        # if user =='admin':
        #     print("Hello admin, would you like to see a status report?")
        # else:
        #     print("Hello"+user+"thank you for logging in again")
else:
    print("We need to find some users")
print (users)