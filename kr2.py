from datetime import datetime, timedelta

datediap = input().split()
x = int(input())
a = []
delta_time = timedelta(days=1)
start = datediap[0]
finish = datediap[1]
while start < finish:
    if start.date % x != 0 and start.weekday() != 1:
        a.append(start)
    start = start + delta_time
if len(a) >= 3:
    for i in range(3):
        print(a[i])
else:
    print('CANCEL CARNIVAL')