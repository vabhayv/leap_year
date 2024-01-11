input("Wanna check Which year has 366 days instead of 365\nTap Enter To Continue\n")
year = int(input("Write down the Year you wanna check\n"))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"Yes {year} is a Leap Year so there are 366 days")
    else:
      print(f"No {year} is not leap year so there are 365 days only")
  else:
    print(f"Yes {year} is a Leap Year so there are 366 days")
else:
  print(f"No {year} is not leap year so there are 365 days only")