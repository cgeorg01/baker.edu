#Get user input
year_input = input("Enter a year (1962 to 2014): ")
year = int()

#Approximate value of a Ferrari 250 GTO
value_list = [18500, 6000, 12000, 48000, 200000, 650000, 35000000, 52000000]
value = int()

#Test if input is a number
if year_input.isdigit():
    year = int(year_input) #Convert to integer
    if year < 1962 or year > 2014:  #Test if valid year entered
        print("Invalid year")
        exit()
else:
    print("Invalid year")
    exit()

if year <= 1962: #Test if year is 1962-1964
    value = 0
elif year <= 1968: #Test if year is 1965-1968
    value = 1
elif year <= 1971: #Test if year is 1969-1971
    value = 2
elif year <= 1975: #Test if year is 1972-1975
    value = 3
elif year <= 1980: #Test if year is 1976-1980
    value = 4
elif year <= 1985: #Test if year is 1981-1985
    value = 5
elif year <= 2012: #Test if year is 1986-2012
    value = 6
elif year <= 2014: #Test if year is 2013-2014
    value = 7

#Print value
if value > -1:
    print('In', year, 'the approximate value of a Ferrari 250 GTO was', f'${value_list[value]:,}')