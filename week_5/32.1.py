from csv import reader, writer
result = []
with open('transakcje-1.csv') as input_file:
    content = reader(input_file, delimiter=',')
    next(content)
    for line in content:
        if int(line[-1]) > 0:
            result.append(line)

with open('przychody.csv', 'w') as output_file:
    content = writer(output_file, delimiter=',')
    for line in result:
        content.writerow(line)
