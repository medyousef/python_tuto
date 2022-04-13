#variables
print(8)
print(5)
print(5)
a=5*2
b=4
c=15
print(a)
temperature=40
counter = 0
user_age=10
print(type(counter))

#define a function
def triple_number(number):
    return number*3
def print_triple_number(number):
    print (triple_number(number))
b=triple_number(a)+triple_number(b)
print(b)
print_triple_number(c)

#concatinate two upper case strings
string_1="Hello"
string_2="world"
def concat(str_1,str_2):
    print(str_1.upper()+" "+str_2.upper())
concat(string_1,string_2)

# condition
temperature =18
feeling = "warm"

if temperature > 20  or feeling =="warm":
    print("it's warm")
elif temperature >= 10 :
    print("less than 20")
else:
    print("not warm")
#validte user inupt and loops
""" my_input=int(input("get number between 1 and 100: "))
while my_input <1 or my_input>100:
    print("user gave wrong number: ",my_input)
    my_input=int(input("get number between 1 and 100: "))

print("the triple of that: ",triple_number(my_input))
 """
for  i in range(0,10):
    print("smth",i)

#lists
number_list = [3,.5,9,10]
number_list.append(34)

#print(number_list)
new_list=[]
for number in number_list:
    print("the number is", number)
    new_list.append(number*2)
print("the new list is: ",new_list)

#exrecice find the max value in list
list_ele=[3,5,9,12,24,2,7]
max_val=list_ele[0]
for x in range(0,len(list_ele)):
    if max_val<=list_ele[x]:
        max_val=list_ele[x]
print("the maximaum value is: ",max_val)
#modules
import time

time.sleep(3)
print("hello after 3 sec")

