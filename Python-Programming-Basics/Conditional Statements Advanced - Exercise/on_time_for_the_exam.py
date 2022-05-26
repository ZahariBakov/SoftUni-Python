exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes
difference = abs(exam_time - arrival_time)
difference_hour = difference // 60
difference_minutes = difference % 60

if arrival_time > exam_time:
    print("Late")
    if difference_hour > 0:
        print(f"{difference_hour}:{difference_minutes:02d} hours after the start")
    else:
        print(f"{difference_minutes} minutes after the start")
elif exam_time > arrival_time + 30:
    print("Early")
    if difference_hour > 0:
        print(f"{difference_hour}:{difference_minutes:02d} hours before the start")
    else:
        print(f"{difference_minutes} minutes before the start")
else:
    print("On time")
    if exam_time > arrival_time:
        print(f"{difference_minutes} minutes before the start")
