#!/usr/bin/env python
# coding: utf-8

# # Food Ordering App
# 
# Have to design a Food Ordering app for a restaurant.
# 
# The application will have a log-in for admin and users.
# 
# 
# Admin will have the following functionalities:
# 
# Add new food items. Food Item will have the following details:
# FoodID //It should be generated automatically by the application.
# Name
# Quantity. For eg, 100ml, 250gm, 4pieces etc
# Price
# Discount
# Stock. Amount left in stock in the restaurant.
# Edit food items using FoodID.
# View the list of all food items.
# Remove a food item from the menu using FoodID.
# 
# 
# The user will have the following functionalities:
# 
# Register on the application. Following to be entered for registration:
# Full Name
# Phone Number
# Email
# Address
# Password
# Log in to the application
# The user will see 3 options:
# Place New Order
# Order History
# Update Profile
# Place New Order: The user can place a new order at the restaurant.
# Show list of food. The list item should as follows:
# 1. Tandoori Chicken (4 pieces) [INR 240]
# 2. Vegan Burger (1 Piece) [INR 320]
# 3. Truffle Cake (500gm) [INR 900]
# Users should be able to select food by entering an array of numbers. For example, if the user wants to order Vegan Burger and Truffle Cake they should enter [2, 3]
# Once the items are selected user should see the list of all the items selected. The user will also get an option to place an order.
# Order History should show a list of all the previous orders
# Update Profile: the user should be able to update their profile.

# In[1]:


# The application will have a log-in for admin.

print("\n Admin user id & password")
class Admin_login(): 
    def signup(self,admin_name,password):
        self.admin_name = admin_name
        self.password = password
        return "singup succeed"
        
    def login(self,admin_name,password):
        if self.admin_name == admin_name and self.password==password:
            return "logged in"
            
        else: 
            return "Wrong ID & Password"

A1 =  Admin_login()
print(A1.signup('Dimple','Dimple1111'))
print(A1.login('Dimple','Dimple1111'))
print(A1.login('Dimple','Dimple111'))
print(A1.login('D','Dimple'))

# Add new food items. Food Item will have the following details:-
# FoodID //It should be generated automatically by the application.
print("\n Add new food items. Food Item will have the following details:-")
Nonvegfoods=[{'name':'Tandoori Chicken','price':240,'qut':'4 pieces','dis': '5 per'},{'name':'Vegan Burger','price':320,'qut':'1 pieces','dis': '5 per'}]

for i in Nonvegfoods:
    print(f"{Nonvegfoods.index(i)+1}. {i['name']} ({i['qut']}) [INR {i['price']}] {i['dis']}")

Vegfoods = [{'name':'Paneer angara','price':250,'gm':'250gm','dis': '10 per'},{'name':'Truffle Cake','price':900,'gm':'500gm','dis':'10 per'}]

for i in Vegfoods:
    print(f"{Vegfoods.index(i)+3}. {i['name']} ({i['gm']}) [INR {i['price']}] {i['dis']}")
SoftDrink = [{'name':'Thums up','price':65,'ml':'100ml','dis': 'No discount'},{'name':'Coca cola','price':60,'ml':'100ml','dis': 'No discount'}]

for i in SoftDrink:
    print(f"{SoftDrink.index(i)+5}. {i['name']} ({i['ml']}) [INR {i['price']}] {i['dis']}")

# Stock
print("\n Stock :-")
Stock = 100

if Stock >=100 :
    print("\n stock available")
        
else:
    print("\n Out of stock")
  
# Amount left in stock in the restaurant.
print("\n Amount left in stock in the restaurant :- ")
Stock_sale = 70

if Stock_sale  <=50:
    print("\n 50 stock available ")
elif Stock_sale >=70:
    print("\n 30 stock available ")
else:
    print("\n out of stock ")
    
    
#  Other method to add items. # Add new food items. Food Item will have the following details:-
print("\n Another method to add items. # Add new food items. Food Item will have the following details:- ")
class Food_items():
    
    def __init__(self,id,name,price,Quantity,Discount):
        self.id = id
        self.name = name
        self.price = price
        self.Quantity=Quantity
        self.Discount=Discount
        
F1= Food_items(1,'Paneer Angara','250rs','250gm','5% Dis')
F2= Food_items(2,'Veg Handi','159rs','250gm','5% Dis')
F3= Food_items(3,'Chicken leg piece ','500rs','4 piece','10% Dis')
F4= Food_items(4,'Fish piece ','450rs','4 piece','10% Dis')
F5= Food_items(5,'Coca-cola','60rs','100 ml','No discount')
F6= Food_items(6,'Thums up','65rs','100 gm','No discount')

print(F1.id,F1.name,F1.price,F1.Quantity,F1.Discount)
print(F2.id,F2.name,F2.price,F2.Quantity,F2.Discount)
print(F3.id,F3.name,F3.price,F3.Quantity,F3.Discount)
print(F4.id,F4.name,F4.price,F4.Quantity,F4.Discount)
print(F5.id,F5.name,F5.price,F5.Quantity,F5.Discount)
print(F6.id,F6.name,F6.price,F6.Quantity,F6.Discount)

# Edit food items using FoodID.
print("\n Edit food items using FoodID. :- ")
if F1.id == 3:
    print("\n Truffle Cake 500gm) [INR 900] 10 per n/")
else : 
    print("\n Chicken leg piece  500rs 4 piece 10% Dis ")

# View the list of all food items
print("\n View the list of all food items :- ")
dict1 = {'name':'tandoori chicken', 'name1':'tandoori roti','name2':'paneer angara','name3':'Veg handi','name4':'Thums up','name5':'Coca cola'}

list = list(dict1.items())
print(list)

# Remove a food item from the menu using FoodID.
print("\n Remove a food item from the menu using FoodID.:-  ")
if F1.id == 1:

    print("\n Tandoori Chicken (4 pieces) [INR 240] 5 per")
else :
    print("\n 2 Vegan Burger (1 pieces) [INR 320] 5 per")

# The user will have the following functionalities:
print("\n The user will have the following functionalities:-  ")
class User():    
    
    def __init__(self,Full_Name,Phone_Number,Email,Address,password):
        
        self.Full_Name = Full_Name
        self.Phone_Number = Phone_Number
        self.Email = Email
        self.Address = Address
        self.password = password
Us = User('Safak Shaikh',7383370686,'dimpleadagar123@gmail.com','Ahmedabad-Gujarat','Safak123')
print(Us.Full_Name)
print(Us.Phone_Number)
print(Us.Email)
print(Us.Address)
print(Us.password)

print("\n The user login id & password:-  ")
class User_login(): 
    def signup(self,username,password):
        self.username = username
        self.password = password
        return "singup succeed"
    
    def login(self,username,password):
        if self.username == username and self.password==password:
            return "logged in"
        else:
            return "Username and password is incorrect"
        
U1 =  User_login()
print(U1.signup('Safak','Safak123'))
print("register sucessful")
print(U1.login('Safak','Safak123'))
print(U1.login('Safak','Safak12'))
print(U1.login('S','Safak'))

# Place New Order: The user can place a new order at the restaurant.
# Show list of food. The list item should as follows:
# 1. Tandoori Chicken (4 pieces) [INR 240]
# 2. Vegan Burger (1 Piece) [INR 320]
# 3. Truffle Cake (500gm) [INR 900]

print("\n Place New Order: The user can place a new order at the restaurant.:-  ")

class place_order(Food_items):
    
    def __init__ (self):
        
        if place_order == Food_items :
            return (Food_items)
        else:
            print("1. Tandoori Chicken (4 pieces) [INR 240] 5 per")
            print("2. Vegan Burger (1 pieces) [INR 320] 5 per")
            print("3. Truffle Cake (500gm) [INR 900] 10 per")
f11 = place_order()


# Order History should show a list of all the previous orders
print("\n Order History should show a list of all the previous orders :-  ")
class order_history(Food_items):
    
    def __init__ (self):
        
        if order_history == Food_items :
            return (Food_items)
        else:
            print("2. Vegan Burger (1 pieces) [INR 320] 5 per")
            print("3. Truffle Cake (500gm) [INR 900] 10 per")
f3 = order_history()


# Update Profile: the user should be able to update their profile.
print("\n Update Profile: the user should be able to update their profile :-  ")
class User_update_profile (User):    
    
    def __init__(self):
        
        self.Full_Name = Full_Name
        self.Phone_Number = Phone_Number
        self.Email = Email
        self.Address = Address
        self.password = password
U1 = User('Safak Shaikh',7383370686,'dimpleadagar123@gmail.com','Ahmedabad-Gujarat','Safak123')
print = input('Enter your name : ')

print = input('Enter mobiled no. : ')

print = input('Enter Email id: ')

print = input('Enter address : ')

print = input('Enter password : ')

print = input("updated sucessfully")

print = input ("Thank you for your time.")
print = input ("Please Visit Again.")


# In[ ]:




