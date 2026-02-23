import time
alarm_time = input("Set Alarm (HH:MM): ")

while True:
    current_time = time.strftime("%H:%M")
    
    if current_time == alarm_time:
        print("Wake up kijana mdogo!")
        break

    time.sleep(1)  