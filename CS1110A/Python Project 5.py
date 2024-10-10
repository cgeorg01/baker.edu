#Create Automobile class.
class Automobile:

    #Initialize objects for Automobile class.
    def __init__(self):
        self.make = ''
        self.model = ''
        self.color = ''
        self.year = 0
        self.mileage = 0

    #Add a vehicle.
    def add_vehicle(self):
        self.make = input('Enter Make: ')
        self.model = input('Enter Model: ')
        self.color = input('Enter Color: ')
        self.year = int(input('Enter Year: '))
        self.mileage = int(input('Enter Mileage: '))

    def pre_loaded(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

def main():
    vehicle_list = []
    vehicle = Automobile()
    vehicle.pre_loaded('Ford', 'Edge', 'Black', 2017, 93333)
    vehicle_list.append(vehicle)

    vehicle = Automobile()
    vehicle.pre_loaded('Honda', 'Civic', 'Blue', 2019, 42362)
    vehicle_list.append(vehicle)

    vehicle = Automobile()
    vehicle.pre_loaded('Acura', 'MDX', 'White', 2016, 100000)
    vehicle_list.append(vehicle)

    user = 'y'

    while user == 'y':

        print('Enter 1 to Add a new vehicle\n'
              'Enter 2 to Remove a vehicle\n'
              'Enter 3 to View list of vehicle\n'
              'Enter 4 to Exit\n')

        task = input('What would you like to do? ')

        #Add a new vehicle.
        if task == '1':
            vehicle = Automobile()
            vehicle.add_vehicle()
            vehicle_list.append(vehicle)
            print(vehicle.year, vehicle.make, vehicle.model, 'has been added to the list\n')

        #Remove a vehicle.
        elif task == '2':
            #Print message if vehicle list is empty.
            if vehicle_list is None or len(vehicle_list) == 0:
                print('There is no vehicle.\n')
            #If vehicle list is not empty
            else:
                i = 0
                print('Select vehicle to remove')
                #Print list of vehicles available to be deleted
                for vehicle in vehicle_list:
                    print('Enter', str(i), 'to remove', vehicle.year, vehicle.make, vehicle.model, vehicle.color, vehicle.mileage)
                    i += 1

            delete_vehicle = input('Enter number: ')

            #Test user input is digit
            if delete_vehicle.isdigit():
                int_del_vehicle = int(delete_vehicle)
                #Delete vehicle from list
                if 0 <= int_del_vehicle <= len(vehicle_list)-1:
                    vehicle_list.pop(int_del_vehicle)
                    print('Vehicle has been removed.\n')
                else:
                    print('Vehicle does not exist.\n')
            else:
                print('Vehicle does not exist.\n')

        #Display list of vehicles in a table.
        elif task == '3':
            #Table header
            print(f'{"Make":16}{"Model":16}{"Color":16}{"Year":8}{"Mileage":10}')
            print('-' * 66)

            i = 0
            #Table rows
            for vehicle in vehicle_list:
                print(f'{vehicle.make:16}{vehicle.model:16}{vehicle.color:16}{vehicle.year:<8}{vehicle.mileage:<10}')
                i += 1

            print()

        #Exit
        elif task == '4':
            user = 'n'

if __name__ == "__main__":
    main()