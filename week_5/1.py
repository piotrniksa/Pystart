from datetime import date

today = date.today()
day = date(today.year, 11, 9)
formatted = day.strftime("%d.%m.%Y")
print(f"Moje urodziny w tym roku: {today}")
print(f"Moje urodziny w tym roku: {day}")
print(f"Moje urodziny w tym roku: {formatted}")
