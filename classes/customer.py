import csv
import os.path

class Customer:
    def __init__(self,id,account_type,first_name,last_name,current_video_rentals=''):
        self.id=id
        self.account_type=account_type
        self.first_name=first_name
        self.last_name=last_name
        self.full_name= f'{first_name} {last_name}'
        self.current_video_rentals=current_video_rentals
        self.rent_limit= self.max_rent()

    def __str__(self):
        return f'\n{self.full_name} is currently renting:\n---------------\n{self.current_video_rentals.replace("/", " & ")}'

    @classmethod
    def all_customers(cls):
        customers = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customers.append(Customer(**dict(row)))

        return customers
    def max_rent(self):
        if self.account_type == 'sx' or self.account_type == 'sf': return 1
        elif self.account_type == 'px' or self.account_type == 'pf': return 3
    
    def new_rental(customer_id)
      
        