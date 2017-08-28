# -*- coding: UTF-8 -*-
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts=0

    def describe_user(self):
        message= "name is "+ self.first_name + " " + self.last_name
        return message

    def greet_user(self):
        mes= "hello " + self.first_name
        return mes

    def increment_login_attempts(self):
        self.login_attempts +=1
        return self.login_attempts

    def rest_login_attempts(self):
        self.login_attempts=0
        return self.login_attempts

class Privileges():
    def __init__(self):
        self.privileges =["can add post","can delete post","can ban user"]

    def show_privileges(self):
         print (self.privileges)


class Admin(User):
    def __init__(self,first,last):
        super().__init__(first,last)
        self.privileges= Privileges()
    #     self.privileges=["can add post","can delete post","can ban user"]
    #
    # def show_privileges(self):
    #     print (self.privileges)

b= Admin("ron","li")

b.privileges.show_privileges()