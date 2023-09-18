TotalSeconds = int(input())

Hour = int(TotalSeconds/3600)
RemainingSecond = TotalSeconds % 3600
Minute = int(RemainingSecond/60)
Second = RemainingSecond % 60


print(f"{Hour}:{Minute}:{Second}")
