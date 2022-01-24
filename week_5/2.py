from datetime import date

today = date.today()
birthday = date(today.year, 1, 13)

if birthday > today:
    diff = birthday - today
    print(f'Data Twoich następnych urodzin to {birthday.strftime("%d.%m.%Y")}. Do urodzin pozostało {diff.days} dni.')
else:
    n_birthday = date(today.year + 1, 1, 13)
    diff = n_birthday - today
    print(f'Data Twoich następnych urodzin to {n_birthday.strftime("%d.%m.%Y")}. Do urodzin pozostało {diff.days} dni.')
