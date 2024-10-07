# Convert temperature input to floating point number or quit program.
def convert_float(x):
    # Quit program.
    if x.lower() == 'quit':
        return exit()
    # Convert to floating point number.
    else:
        # Handle exception.
        try:
            temp_float = float(x)
            return temp_float
        except ValueError:
            raise ValueError('Input Exception! Please enter a valid temperature.')

# Convert temperature to Fahrenheit.
def conv_to_f(celsius):
    f = (9 / 5) * celsius + 32
    return f

# Convert temperature to Celsius.
def conv_to_c(fahrenheit):
    c = (5 / 9) * (fahrenheit - 32)
    return c

def main():
    # Loop program until user input quit.
    while True:
        # Handle exception.
        try:
            # Get temperature.
            user_temperature = convert_float(input('Enter temperature or quit to exit program: '))

            i = 0

            # Loop until user enters correct unit of measurement.
            while i == 0:
                # Get unit of measurement.
                unit_measurement = input('Enter unit of measure (C or F): ').capitalize()

                # Convert Celsius to Fahrenheit.
                if unit_measurement.capitalize() == 'C':
                    i = 1   # end loop
                    f = conv_to_f(user_temperature)
                    print(f'{user_temperature} Celsius is {f:.2f} Fahrenheit\n')
                # Convert Fahrenheit to Celsius.
                elif unit_measurement.capitalize() == 'F':
                    i = 1   # end loop
                    c = conv_to_c(user_temperature)
                    print(f'{user_temperature} Fahrenheit is {c:.2f} Celsius\n')
                else:
                    print('Invalid unit of measurement!\n')

        except ValueError as e:
            print(e, '\n')

if __name__ == "__main__":
    main()
