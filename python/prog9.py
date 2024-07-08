def convert_days(days):
    years = days // 365
    weeks = (days % 365) // 7
    days = (days % 365) % 7
    return years, weeks, days

total_days = 366

years, weeks, days = convert_days(total_days)
print(f"{total_days} days is equivalent to {years} years, {weeks} weeks, and {days} days.")
