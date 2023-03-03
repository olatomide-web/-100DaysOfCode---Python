age = int(input("what is your current age?\n"))

yearRemaining = 90 - age

days = yearRemaining * 365
weeks = yearRemaining * 52
months = yearRemaining * 12

message = f"you have {days} days, {weeks} weeks, {months} months left to live"
print(message)
