import random
name = input('whats your name? ')
while True: 
 yes = input("roll a dice (yes/no) ")  
 if yes == "n": 
     print("goodbye " + name)
     break

 elif yes== 'y': 
    result = random.randint(1,6)
    print("you rolled : " , result)
