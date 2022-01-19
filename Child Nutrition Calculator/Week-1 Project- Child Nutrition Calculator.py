#!/usr/bin/env python
# coding: utf-8

# # <font color='green'><center>Child Nutrition Calculator</center></font>

# ### Child's Details:
# - Name
# - Age
# - Gender
# - Weight
# - Height

# #### Enter Details of child:

# In[25]:


# Enter Name
name = input("Enter name: ")
# Enter Age
age = int(input("Enter age: "))
# Enter Gender
gender = input("Enter gender- M/F: ")
# Enter Weight
weight = float(input("Enter weight in Kgs: "))
# Enter Height
height = float(input("Enter height in meters: "))


# #### Enter daily food intake by child:

# In[26]:


milk = int(input("Enter milk intake of child in a day in grams: "))
egg = int(input("Enter egg intake of child in a day in grams: "))
rice = int(input("Enter rice intake of child in a day in grams: "))
lentils = int(input("Enter lentils/pulses intake of child in a day in grams: "))
veggies = int(input("Enter vegetables/fruits intake of child in a day in grams: "))
meat = int(input("Enter meat intake of child in a day in grams: "))


# ### Calories/Gram for different food:
# - Milk: 100 cal/ 100g 
# - Egg: 155 cal/ 100g 
# - Rice: 130 cal/ 100g 
# - Lentils: 113 cal/ 100g 
# - Vegetable: 85 cal/100g 
# - Meat: 143 cal/ 100g

# ### Daily Calorie Intake based on Age-group:
# - Age b/w 0-2 years: 800 calories
# - Age b/w 2-4 years: 1400 calories
# - Age b/w 4-8 years: 1800 calories

# In[27]:


# Calulating Calories consumed by child in a day:
calorie = (milk/100)*100 + (egg/100)*155 + (rice/100)*130 + (lentils/100)*113 + (veggies/100)*85 + (meat/100)*143
if age in range(0,3):
    if calorie in range(800,1400):
        nourishment = "nourished"
    else:
        nourishment = "under-nourished"
if age in range(2,5):
    if calorie in range(1400,1800):
        nourishment = "nourished"
    else:
        nourishment = "under-nourished"
if age in range(4,9):
    if calorie >= 1800:
        nourishment = "nourished"
    else:
        nourishment = "under-nourished"


# In[28]:


# Calulating BMI of child:
bmi = (weight)/(height**2)
if bmi<16:
    category = "Severely Underweight"
elif bmi>=16 and bmi<18:
    category = "Underweight"
elif bmi>=18 and bmi<25:
    category = "Healthy"
elif bmi>=25 and bmi<30:
    category = "Overweight"
else:
    category = "Obese"


# ## <font color='red'><center>BMI Categories </center></font>
# <style>
# table {
#   font-family: arial, sans-serif;
#   border-collapse: collapse;
#   width: 200%;
# }
# 
# td, th {
#   border: 1px solid #dddddd;
#   text-align: left;
#   padding: 10px;
# }
# 
# tr:nth-child(even) {
#   background-color: #D6EEEE;
# }
# </style>
# <table>
#   <tr>
#     <th>BMI</th>
#     <th>BMI Categories</th>
#   </tr>
#   <tr>
#     <td>&#60; 16</td>
#     <td>Severely Underweight</td>
#   </tr>
#   <tr>
#     <td>&ge; 16 and &#60; 18</td>
#     <td>Underweight</td>
#   </tr>
#   <tr>
#     <td>&ge; 18 and &#60; 25</td>
#     <td>Healthy</td>
#   </tr>
#   <tr>
#     <td>&ge; 25 and &#60; 30</td>
#     <td>Overweight</td>
#   </tr>
#   <tr>
#     <td>&ge; 30</td>
#     <td>Obese</td>
#   </tr>
# </table>

# ## <font color='blue'> Results:</font>

# In[29]:


if(gender=='M'):
    print("BMI of ",name," is ",bmi," and he is ",category)
    print("The daily calorie consumption of ",name," is ",calorie," and he is",nourishment)
else:
    print("BMI of ",name," is ",bmi," and she is ",category)
    print("The daily calorie consumption of ",name," is ",calorie," and she is",nourishment)

