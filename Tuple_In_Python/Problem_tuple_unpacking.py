# Convert days into years,months and remaining day.
#input: 4320
# output: 11 10 5
def convert_days(days):
    years = days // 365
    months = (days - years * 365) // 30
    remaining_days = days - years * 365 - months *30
    return years, months, remaining_days
result = convert_days(4320)
print(result)
years,months,days=result
print(years,months,days)