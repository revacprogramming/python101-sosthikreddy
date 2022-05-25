'''hrs = float(input("Enter Hours:"))

rt = float(input("enter the rate"))
if hrs<=40:
    print(hrs*rt)
else:
    m=hrs-40
    total=(40*rt)+(m*(rt*1.5))
    print(total)'''

score = float(input("Enter Score between 0.0 and 1.0: "))

if not(0.0 <= score <= 1.0):
    print("Invalid input!")
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:    
    print('F')