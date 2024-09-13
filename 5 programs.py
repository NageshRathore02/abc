'''
import random
target = random.randint(1,100)

while True:
    guess_no = int(input("Guess a num :: "))

    if target == guess_no :
        print("correct guess")
        break
    elif target > guess_no :
        print("guess bigger num")
    elif target < guess_no :
        print("guess smaller num")
    else:
        print("invalid choice")
print("game over")
'''
'''
li = ["r","a","d","a","r"]
copy_list = li.copy()
li.reverse()
if li == copy_list:
   print("palindrome")
else:
   print(" not palindrome")
'''
'''
str = input("enter a string :: ").lower()
vowels = "aeiou"
vowel = 0
consonant = 0
for char in str:
    if char in vowels:
        vowel += 1
    else:
        consonant += 1
print("num of vowels",vowel)
print("num of consonants",consonant)
'''
'''
def converter(usd_value):
    inr_value = usd_value * 83.96
    inr_value=round(inr_value,3)
    print(usd_value,"usd value",inr_value,"inr value")
converter(76)
'''
'''
n = int(input("enter a num"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)
'''
'''
a = 0 
b = 1

for i in range(10):
    print(a)
    # a=a+b
    b=b+a
    a=b-a
    '''
'''
import string
str = input("enter a string :: ").lower()
a = string.ascii_lowercase
letter = 0
for char in str:
    if char in a:
        letter += 1
print("num of character",letter)
'''
'''
input_string = input("Enter a string: ")
letter = input("Enter the letter to count: ")

if len(letter) != 1:
    print("Please enter a single letter.")
else:
    count = input_string.count(letter) 
    print(f"The letter '{letter}' occurs {count} time(s) in the string.")

'''
'''
num = int(input("Enter a num: "))
fact = 1
if(num == 0 or num == 1):
    print("1")
else:
    for i in range(2,num+1):
        fact *= i
    print("factorial ofnum is",fact)
'''
'''
for i in range(0,5):
    for j in range(0,i+1):
        print(j,end=" ")    
    print()
'''
'''
x = "this is"
y = 'this is'
print(id(x))
print(id(y))
'''
"""
num = int(input("enter a num"))
if (num%3==0 and num%5==0):
    print("fizzbuzz")
    print("fizz")
    print("buzz")
elif(num%3==0):
    print("fizz")
elif(num%5==0):
    print("buzz")
else:
    print("nothing")
"""
'''
a = int(input("enter a side of triangle"))
b = int(input("enter a side of triangle"))
c = int(input("enter a side of triangle"))
if(a==b and b==c):
    print("equilateral")
elif(a==b and b!=c):
    print("isosceles")
else:
    print("scalene")
'''
'''
a = int(input("enter a num"))
b = int(input("enter a num"))
if(a>=20 or a>=30):
    print("zero")
elif(b>=20 or b>=30):
    print("zero")
else:
    print(a*b)
'''
'''
a = int(input("enter a num"))
b = int(input("enter a num"))
c = int(input("enter a num"))
if(a>b and a>c):
    print("first num is greatest",a)
elif(b>a and b>c):
    print("second num is greatest",b)
elif(c>a and c>b):
    print("third num is greatest",c)
elif(a==b and b!=c):
    print("a and b are greatest")
elif(c==b and c!=a):
    print("c and b are greatest")
elif(a==c and c!=b):
    print("a and c are greatest")
else:
    print("all are equal")
'''
'''
age = int(input("enter age : "))
if(age>12 and age<20):
    print("teenager")
elif(age>19 and age< 50):
    print("adult")
elif(age<13 and age>1):
    print("child")
elif(age>49):
    print("old")
else:
    print("new born baby")
'''
'''
unit = int(input("enter unit"))
if(unit>0 and unit <= 100):
    print("your bill is zero")
elif(unit>100 and unit<=200):
    print((unit-100)*5)
elif(unit>200):
    print(((unit-200)*10)+500)
else:
    print("your meter is damaged")
'''
'''
age = int(input("enter your age"))
if age >= 18 :
    print("u r eligible to vote")
else:
    print("not eligible to vote")
'''
'''
num = int(input("enter num"))
if num%2==0:
    print(num,"is even")
else:
    print(num,"is odd")
'''
'''
num = int(input("enter num"))
if num==0:
    print("num is zero")
elif num%7==0:
    print(num,"is divisible by 7")
else:
    print(num,"is not divisible by 7")
'''
'''
num = int(input("enter num"))
if num%5==0:
    print("hello")
else:
    print("bye")
'''
'''
num = int(input("enter num"))
print(num%10)
'''
'''
num = int(input("enter num"))
ld = num%10
if ld%3==0:
    print("last digit is divisible by 3")
else:
    print("last digit is not divisible by 3")
'''
'''
num = int(input("enter num"))
if num>90:
    print("A")
elif num>80 and num<=90:
    print("B")
elif num>60 and num<=80:
    print("C")
else:
    print("D")
'''
'''
price = int(input("enter price if bike"))
if price>100000:
    print(((price*15)/100)+price)
elif price<=100000 and price>50000:
    print((price/10)+price)
else:
    print((price/20)+price)
'''
'''
year = int(input("enter year"))
if year%100==0:
    if year%400==0:
        print("leap year")
    else:
        print("not leap year")
else:
    if year%4==0:
        print("leap year")
    else:
        print("not leap year")
'''
'''
num=int(input("enter num"))
if num==0:
    print("not valid")
elif num%7==1:
    print("sunday")
elif num%7==2:
    print("monday")
elif num%7==3:
    print("tuesday")
elif num%7==4:
    print("wednesday")
elif num%7==5:
    print("thrusday")
elif num%7==6:
    print("friday")
elif num%7==0:
    print("saturday")
else:
    print("exception case")
'''
'''

num=int(input("enter num"))
if num==1:
    print("january")
elif num==2:
    print("february")
elif num%7==3:
    print("march")
elif num==4:
    print("april")
elif num==5:
    print("may")
elif num==6:
    print("june")
elif num==7:
    print("july")
elif num==8:
    print("august")
elif num==9:
    print("september")
elif num==10:
    print("october")
elif num==11:
    print("november")
elif num==12:
    print("december")
else:
    print("invalid choice")
'''
'''
name = "rahul"
i = 3
for i in range(5):
    print(i)
    print(i+1)
    print(name[i])
'''
'''
import string
n = 5
st = string.ascii_uppercase()
for i in range(n):
    if i == 0 or i== n-1:
        for j in range(1,n+1):
            print(st[j] * n)
    else:
        print("*" +" " * (n-2)+"*")
    '''
'''
a = 10
b = 20
a,b= b,a
print(a)
print(b)
'''
# a="Mangom"
# print(a.capitalize())
# print(a.casefold())

# print(a.count("m"))
# print(a.endswith("om"))
# print(a.find("n"))
# print(a.index("g"))
# print(a.lower())
# print(a.replace("m","n"))

# st = "this is my island istanbul"
# c = st.count("is")
# idx = -1
# while c>0:
#     idx = st.find("is",idx+1)
#     print(idx)
#     c -= 1

# a = "this is island istanbul"
# word = "is"
# fr= 0
# for i in range(len(a)-len(word)):
#     if a[i:len(word)+i] == word :
#         print(i)
#         fr+=1
# print(fr)


#diff b/w deep copy and shallow copy


# project voting system

# li = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in range(len(li)+1):
#     sum += i
    
# print(sum)


# li = [1,2,3,4,5,6,7,8,9,10]
# mul = 1
# for i in range(1,len(li)+1):
#     mul *= i
    
# print(mul)


# li = [11,2,33,24,5]
# l = li[0]
# for i in li:
#     if i > l:
#         l = i  
# print(l)


# li = [11,2,33,24,5]
# l = li[0]
# for i in li:
#     if i < l:
#         l = i  
# print(l)

# li= ['abc', 'xyz', 'aba', '1221']
# for item in li:
#     if len(item)>2:
#         if item[0]==item[-1]:
#             print(item) 



# import os
# names = ['A','B']
# numbers = [1,2]
# while True:
#     os.system('cls')
#     choice = input("Enter \n1 for store new contact \n2 for search contact \n3 for update contact \n4 for delete contact \n5 for show all contacts")
    
#     if choice =='1':
#         names.append(input("Enter Name:: ").upper())
#         numbers.append(int(input("Enter Num:: ")))
#         print(names)
#         print(numbers)
        
#     elif choice == '2':
#         name = input("Enter Name").upper()
#         if name in names:
#             name = numbers[names.index(name)]
#             print("Numbers",name)
    
#     elif choice == '3':
#         name = input("Enter Name").upper()
#         if name in names:
#             num = numbers[names.index(name)]
#             print("Numbers",num)
            
#             new_num = int(input("Enter New Num:: "))
#             numbers[names.index(name)] = new_num
#             print("New Number",numbers[names.index(name)])
            
#     elif choice == '4':
        
#         choice1 = input("Enter \nA for delete from name\nB for delete from number").upper()
#         if choice1=="A":
#             name = input("Enter Name").upper()
#             if name in names:
#                 num = numbers[names.index(name)]
#                 names.remove(name)
#                 numbers.remove(num)
#                 print("Contact Deleted Successfully")
#             else:
#                 print("Name Not Found")
        
#         elif choice1=="B":
#             num = int(input("Enter Num:: "))
#             if num in numbers:
#                 name = names[numbers.index(num)]
#                 names.remove(name)
#                 numbers.remove(num)
#                 print("Contact Deleted Successfully")
#             else:
#                 print("Number not found")
#         else:
#             print("Invalid choice")
#     elif choice=='5':
#         for name,numbers in zip(names, numbers):
#             print(f"{names},{numbers}")


# print(ord('Z'))


              
        
# sent = 'this is my pen this is your pen'

# fr = {}
# for i in sent:
#     if i not in fr.keys():
#         fr[i]= 1
#     else:
#         fr[i] +=1
    
# print(fr)  



# def printId(n,a,p,ad):
#     print("name : ",n.title())
#     print("age : ",round(float(a),0))
#     print("post : " ,p.title())
#     print("address : ",ad.title())
    
# printId("nagesh",21,"intern","ujn")

# def areaOfRectangle(l,b):
#     return l*b

# print(areaOfRectangle(2,3))

# def find_max(a,b,c):
#     if a>b and a>c:
#         print(a)
#     elif b>a and b>c:
#         print(b)
#     else:
#         print(c)
        
# find_max(125425264646046,125425464646046,125425364646046)
        

# import random
# target = ["rock" ,"paper","scissor"]

# while True:
#     comp = random.choice(target)
#     guess = input("Enter your choice").lower()
#     if comp == guess:
#         print("Tie")
#     elif comp=='rock' and guess == 'paper' :
#         print("You Win")
#     elif comp=='paper' and guess == 'rock' :
#         print("You Loss")
#     elif comp=='rock' and guess == 'scissor' :
#         print("You Loss")
#     elif comp=='scissor' and guess == 'rock' :
#         print("You Win")
#     elif comp=='paper' and guess == 'scissor' :
#         print("You Win")
#     elif comp=='scissor' and guess == 'paper' :
#         print("You Loss")
#     else:
#         print("Invalid Choice ")
    
    
# def func(**a):
#     print("name: " , a["name"])
#     print("class: " ,a["std"])

# func(clg="sandipani", name="nagesh", std = "btech")

# def func(a):
#     if int(str(a**0.5).split(".")[-1]) ==0:
#         return a

# li = [1,2,3,4,5,6,7,8]
# c = list(filter(func,li))
# print(c)

# ints = input("enter no seprated by ,")
# print(list(map(int,ints.split(","))))
  
# ints = input("enter no seprated by ,: ")
# print(list(map(lambda x :[int(x)],ints.split(","))))

# s = "Shalini"
# li = []
# list2 =[]
# final_list = []

# for i in s:
#     li.append(bin(ord(i))[2:])
# for item in li:
#     list2.append(str(item)[::-1])
# for j in list2:
#     sum=0
#     for i in range(0,len(j)):
#         sum += int(j[i])*(2**i)
#     final_list.append(sum)
# print(final_list)
        
# print(eval(input("enter expreession")))  #calc in one line



    
    
    
    

    

        
        
        