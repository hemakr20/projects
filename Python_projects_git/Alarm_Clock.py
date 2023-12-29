import datetime
from playsound import playsound

hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))

am_pm = input("am/pm: ")

if am_pm == "pm":
    hour = hour + 12

while True:
    if hour == datetime.datetime.now().hour and minute == datetime.datetime.now().minute:
        print("Alarm is ON!")
        file_path = r"C:\\Users\\sathi\\PycharmProjects\\pythonProject1\\Alarm-Fast-High-Pitch-A3-Ring-Tone-www.fesliyanstudios.com.mp3"

        try:
            playsound(file_path)
        except Exception as e:
            print(f"Error: {e}")
        break



