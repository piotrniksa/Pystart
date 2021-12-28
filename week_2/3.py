names = ['Marta', 'Piotr', 'Oliwier', 'Janusz', 'Bernadeta']
shortest_name = None
longest_name = None

for name in names:
    if shortest_name is None or len(name) < len(shortest_name):
        shortest_name = name

for name in names:
    if longest_name is None or len(name) > len(longest_name):
        longest_name = name

print(f'Najkrótsze imię z listy to {shortest_name}')
print(f'Najdłuższe imię z listy to {longest_name}')
