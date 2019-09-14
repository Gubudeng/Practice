# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(self.name.title() + " is now sitting.")
#
#     def roll_over(self):
#         print(self.name.title() +" rolled over!")
#
# my_dog = Dog('willie', 6)
#
# print(my_dog.name.title())
# my_dog.sit()
# my_dog.roll_over()
# class Restaurant():
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.name = restaurant_name
#         self.type = cuisine_type
#         self.number_served = 0
#
#     def decribe_restaurant(self):
#         print(self.name +self.type)
#
#     def open_restaurant(self):
#         print("The reastaurant is opening!")
#
#     def read_number(self):
#         print("有"+ str(self.number_served) + "人在餐厅就餐")
#
#     def set_number_served(self,number_served):
#         self.number_served = number_served
#
#     def increment_number_served(self,increment_number):
#         self.number_served += increment_number
#
#
# restaurant = Restaurant('A','B')
# restaurant.decribe_restaurant()
# restaurant.open_restaurant()
# restaurant.read_number()
# restaurant.set_number_served(25)
# restaurant.read_number()
# restaurant.increment_number_served(50)
# restaurant.read_number()

class User():

    def  __init__(self,first_name , last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        print("User: "+ self.first_name.titile() + self.last_name.title())

    def greet_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print("Hello! "+ full_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('john','lee')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privilege()

class Privilege():

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(self.privileges)

admin = Admin('john','little')
admin.privileges.show_privileges()

