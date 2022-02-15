import datetime
from playsound import playsound

hour = int(input("Enter hour: "))
min = int(input("Enter minutes: "))
ampm = input("am / pm: ")

if ampm=="pm":
    hour+=12

while True:
    if hour==datetime.datetime.now().hour and min==datetime.datetime.now().minute:
        print("Playing...")
        playsound("ironman.mp3")
        break
