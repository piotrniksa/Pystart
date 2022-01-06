num_list = []
num_1 = -1000000000000

while len(num_list) < 4:
    num = int(input('Podaj 4 liczby gdzie każda kolejna będzie większa od poprzedniej: '))
    if num > num_1:
        num_list.append(num)
    else:
        break
    num_1 = num

print(sum(num_list) / len(num_list))
