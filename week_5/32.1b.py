summary = 0
with open('przychody.csv') as input_file:
    for line in input_file:
        line_arr = line.strip().split(',')
        created_at, title, value = line_arr
        summary += int(value)

print(summary)