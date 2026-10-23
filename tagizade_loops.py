# Easy
# Q1
for i in range (10,0,-1):
    print(i,"/n")
print("Liftoff!") 
# the results will not be side by side and will be down after previous one with /n then Liftoff will be printed


# Q2
child_tickets=0
adult_tickets=0
for i in range(1,6):
    age=int(input("Age of visitor:"))
    if age <18:
        child_tickets+=1
    else:
        adult_tickets+=1
print("Child tickets", child_tickets)
print("Adult tickets", adult_tickets) 
# in here we will see age visitor and count of tickets each category


# Q3
#    1 3 5 7 9

# Q4
sum=0
for i in range (1,6):
    price=int(input("Price of item:"))
    sum=sum+price
average=sum/5
print("Total:", sum)
print("Average:" , average)


# Q5
password=input("New password:")
while len(password)<8:
    print("Too short, try again")
print("Password accepted")


# Q6

# 70
# 40
# 10
# -20
# Done

# Q7
step_count=0
for i in range (1,7):
    step_count+=1200
    i=str(i)
    print("Day",i,step_count)

# Q8

for i in range(1,4):
    username=input("Username:")
    password=input("Password:")
    if username=="admin"and password=="1234":
        print("Welcome!")
        break #the loop has ended if it is correct
    else:
        if i==3:
            print("Account locked")
        else:
            print("Wrong username or password")

# Medium

# Q9
balance=500
while True:
    amount=float(input("amount:"))
    if amount==0:
        print("Goodbye")
        break
    elif amount<0:
        print("Invalid amount")
    elif amount>balance:
        print("Insufficient funds")
    else:
        balance=balance-amount
        print("Balance:",balance)

# Q10
# PIN: 1111
# Wrong PIN 2 attempts left
# PIN: 2222
# Wrong PIN 1 attempts left
# PIN: 1234
# Access granted


# Q11

sum=0
failed_count=0
passed_count=0
highest=-2
while True:
    grade=int (input("Grade:"))
    if grade==-1:
        break
    elif highest<grade:
        hihhest=grade
    elif grade>=51:
        passed_count+=1
        sum+=grade
    else:
        failed_count+=1
        sum+=grade
count=failed_count+passed_count
average=sum/count
print("Passed:",passed_count)
print("Failed:",failed_count)
print("Highest",highest)
print("Average",average)


# Q12

spaces=20
while True:
    command=input("Command:")
    if command == "stop":
        break
    elif command=="in":
        if spaces==0:
            print("Garage full")
        else:
            spaces-=1
            print("Free spaces",spaces)
    elif command=="out":
        if spaces== 20:
            print("Garage empty")
        else:
            spaces+=1
            print("Free spaces",spaces)
    else:
        print("Unknown command")


# Q13

hottest=-1
hot_days_count=0
for i in range (1,8):
    temp=int(input("Day"+str(i)+":"))
    if temp>30:
        hot_days_count+=1
    if hottest<temp:
        hottest=temp
        hottest_number=i
print("Hot days:",hot_days_count)
print("Hottest day:",hottest_number)


# Q14

# in this attempts will be zero again and again because it is in the loop, 
# write it above the while
password = "secret" 
attempts = 0 
while True: 
     entered = input("Password: ") 
     if entered == password: 
         print("Welcome")
         break
     attempts += 1 
     if attempts == 3: 
         print("Account locked") 
         break


# Q15

password=input("Password:")
digitcount=0
uppercase=0
lowercase=0
for i in password:
    if i.isdigit():
        digitcount+=1
    elif i.isupper():
        uppercase+=1
    elif i.islower():
        lowercase+=1
if len(password)<8:
    print("Weak password ,not enough long password")
elif digitcount==0:
    print("Weak password, no digits")
elif uppercase==0:
    print("Weak password, no uppercase letters")
elif lowercase==0:
    print("Weak password, no lowercase letters")
else:
    print("Strong password")

# Q16

balance=50
count=1
sum=0
while sum<1000:
    sum+=balance
    print("Month " + str(count) + ": " + str(sum))
    balance+=10
    count+=1
print("Goal reached in month"+ str(count-1))


# Q17
# first number which is greater than 100 and which is divided by 7 with zero remains also an odd number

# Hard
# Q18

balance=1000
pin="2580"
attempts=0
is_pin_true=1
while True: 
    entered = input("PIN: ") 
    if entered == pin: 
        is_pin_true=2
        break
    attempts += 1 
    if attempts == 3: 
        print("cart blocked") 
        break
if is_pin_true==2:
    while True:
        print("1-Check balance")
        print("2-Deposit ")
        print("3-Withdraw")
        print("4-Exit")
        choice=input("Choose one number of the aboves")
        if choice=="1":
            print("balance",balance)
        elif choice=="2":
            amount=float(input("amount:"))
            if amount <=0:
                print("rejected amount")
            else:
                balance+=amount
        elif choice=="3":
            amount=float(input("amount:"))
            if amount<=0 or amount>balance:
                print("rejected amount")
            else:
                balance-=amount
        elif choice=="4":
            print("Goodbye")
            break
        else:
            print("Invalid choice")


# Q19

water=1.50
total=0
while total<1.50:
    coin=float(input())
    if coin == 1:
        total+=coin
        total=round(total,2)
    elif coin==0.05:
        total+=coin
        total=round(total,2)
    elif coin==0.10:
        total+=coin
        total=round(total,2)
    elif coin==0.20:
        total+=coin
        total=round(total,2)
    elif coin==0.50:
        total+=coin
        total=round(total,2)
    else:
        print("inserted coin is not accepted")
if total>1.50:
    change=round(total-1.50,2)
print("here is ur water")
print("Change",change)


# Q20
count=0
for i in range (2,101):
    s=0
    for j in (1,i+1):
        if i%j==0:
            s=s+1
        if s==2:
            print(i,end=" ")
            count+=1
print("Total codes:", count)

# Q21
# 101 102
# 201 202
# 301 302


# Q22
for floor in range (1,6):
    if floor==4:
        continue
    for room in range(1,5):
        print("Floor"+str(floor)+":",floor*100+room,end=" ")
    print()

# Q23
minutes=480
count=0
sum=0
while sum<minutes:
    count+=1
    need_minutes=int(input("Customer"+str(count)+"needs (min):"))
    sum+=need_minutes
    if need_minutes==0:
        break
    if sum>minutes:
        print("sorry come back tomorrow")
# didnot finish 23 and 24 25 did not do this my questions: 23 24 25
    
    
    
    


          


    


    

    


    


