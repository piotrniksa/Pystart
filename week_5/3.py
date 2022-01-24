from datetime import datetime, timedelta

start_date = input('Podaj datę rozpoczęcia pracy dd.mm.rrrr: ')
start_date = datetime.strptime(start_date, '%d.%m.%Y')

end_date = input('Podaj datę zakończenia pracy dd.mm.rrrr: ')
end_date = datetime.strptime(end_date, '%d.%m.%Y')

project_day = start_date

diff = end_date - start_date
day_ern = float(input('Podaj Twoją dniówkę: '))

for _ in range(0, diff.days + 1 ):
    print(f'Pracujesz w {project_day.strftime("%A, %d.%m.%Y")}')
    project_day += timedelta(days=1)

earn = int(diff.days) * int(day_ern)
print(f'W tym okresie zarobiłeś: {earn}')
