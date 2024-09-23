get_value = float()
user_values = []

#Get user input & put into container
i = 1
while i <= 5:
    get_value = float(input('Enter a grade:'))
    user_values.append(get_value)
    i += 1

max_number = float(user_values[0])
min_number = float(user_values[0])
total = float()
average = float()

# Get min & max values from container
count = 0
for v in user_values:
    count += 1
    if v > max_number:
        max_number = v
    elif v < min_number:
        min_number = v

    total += v

#Calculate average
average = total / count

print(f'Average: {average}')
print(f'Maximum: {max_number}')
print(f'Minimum: {min_number}')