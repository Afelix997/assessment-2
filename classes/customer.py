import csv
import os.path

class Customer:
    def __init__(self,id,account_type,first_name,last_name,current_video_rentals=''):
        self.id=id
        self.account_type=account_type
        self.first_name=first_name
        self.last_name=last_name
        self.full_name= f'{first_name} {last_name}'
        self.current_video_rentals= current_video_rentals.split('/')
        self.renting_amount= len(self.current_video_rentals)
        if self.current_video_rentals[0]=='':
            self.current_video_rentals=[]
            self.renting_amount=0
        self.rent_limit= self.max_rent()
        

    def __str__(self):
        return f'\n{self.full_name} is currently renting:\n---------------\n{self.current_video_rentals}'

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
    
    def new_rental(self,video):
        if self.renting_amount + 1 > self.rent_limit:
            return '\n -- Reached max rentals for this account type, please return a video to be able to get another. --'
        elif (self.account_type == 'pf' or self.account_type == 'sf') and video.rating=='R':
            return '\n -- Sorry this account type restricts rental of R rated films. --'
        elif video.copies_available == 0:
            return '\n -- Sorry no copies currently available for rent --'
        else:
            video.rent_video()
            self.current_video_rentals.append(video.title)
            self.renting_amount += 1
            return f'Successfully rented {video.title}. Enjoy!'

    def new_return(self,video):
        if video.title in self.current_video_rentals:
            video.return_video()
            self.current_video_rentals.remove(video.title)
            self.renting_amount -= 1
            return f'Successfully returned {video.title}. Thank You!'
        else:
            return f'\n -- Sorry {self.full_name} is not currently renting {video.title} --'
         