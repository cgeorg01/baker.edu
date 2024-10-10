# Quit program.
def end(q):
    if q.lower() == 'quit':
        return exit('Goodbye!')

def convert(temperature, measurement):
    # Convert temperature input to floating point number.
    try:
        temp_float = float(temperature)
    except ValueError:
        raise ValueError('Input Exception! Please enter a valid temperature.')

    # Convert temperature to Fahrenheit or Celsius.
    try:
        if measurement.capitalize() == 'C':
            f = (9 / 5) * temp_float + 32
            print(f'{temperature} Celsius is {f:.2f} Fahrenheit\n')
        elif measurement.capitalize() == 'F':
            c = (5 / 9) * (temp_float - 32)
            print(f'{temperature} Fahrenheit is {c:.2f} Celsius\n')
        else:
            raise ValueError('Input Exception! Please enter a valid unit of measure.')
    except ValueError as e:
        print(e, '\n')

def main():
    # Loop program until user input quit.
    while True:
        # Handle exception.
        try:
            # Get temperature.
            user_temperature = input('Enter temperature / Enter quit to exit: ')
            end(user_temperature)

            # Get unit of measurement.
            unit_measurement = input('Enter unit of measure (C = Celsius or F = Fahrenheit): ')

            #Convert temperature.
            convert(user_temperature, unit_measurement)

        except ValueError as e:
            print(e, '\n')

if __name__ == "__main__":
    main()
