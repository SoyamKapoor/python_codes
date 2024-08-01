import time
timestamp=time.strftime("%H:%M:%S") #This will give you H=Hour, M=Minute, S=Seconds
print("Current Time",timestamp)

timestamp_hour=int(time.strftime("%H"))
print("Hours:",timestamp_hour)

timestamp_minutes=int(time.strftime("%M"))
print("Minutes:",timestamp_minutes)

timestamp_seconds=int(time.strftime("%S"))
print("Seconds:",timestamp_seconds)

if(timestamp_hour>=5 and timestamp_hour<12):
    print("Good Morning sweetheart")
elif(timestamp_hour>=12 and timestamp_hour<18):
    print("Good Afternoon sweetheart")
elif(timestamp_hour>=18 and timestamp_hour<22):
    print("Good Evening sweetheart")
else:
    print("Good Night sweetheart")