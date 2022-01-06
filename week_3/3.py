years_of_experience = float(input('Podaj staż pracy w latach: '))
hours_of_work = int(input('Podaj ilość przepracowanych godzin: '))
items_sold = int(input('Podaj ilość sprzedanych towarów: '))
salary = 2000

experience_bonus = 0.1 if years_of_experience > 2 else 0.02
sales_bonus = 0.25 if items_sold > 30 else 0
hours_of_work_bonus = 0.08 if hours_of_work > 160 and years_of_experience > 1 else 0.02

salary_with_bonuses = salary + experience_bonus * salary + sales_bonus * salary + hours_of_work_bonus * salary

print(f'Wynagrodzenie z dodatkami wynosi: {salary_with_bonuses}')
