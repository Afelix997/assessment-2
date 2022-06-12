from classes.video import Video
from classes.customer import Customer
class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.curr_inventory= Video.all_videos()
        self.curr_customers= Customer.all_customers()

    def list_videos(self):
        print('\n')
        for i, video in enumerate(self.curr_inventory):
            print(f'{i+1}. "{video.title}" Rated: {video.rating} --- {video.copies_available} available for rent')

    def list_customers(self):
        print('\n')
        for i, customer in enumerate(self.curr_customers):
            print(f'{i+1}. Name: {customer.full_name} --- id:{customer.id}')


    def find_video_by_id(self, customer_id):
        for customer in self.curr_customers:
            if customer.id == customer_id:
                return customer
                
    def add_customer(self,data):
        new_customer=Customer(**data)
        self.curr_customers.append(new_customer)

    def rent_video(self,video_title,customer_id):
        x=next((customer.new_rental(video_title) for customer in self.curr_customers if customer.id == customer_id),('\n -- No account matches that id --'))
        print(x)
        return ' '
        
    def return_video(self,video_title,customer_id):
        x=next((customer.new_return(video_title) for customer in self.curr_customers if customer.id == customer_id),('\n -- No account matches that id --'))
        print(x)
        return ' '

    def get_data(self):
        new_id = int(self.curr_customers[-1].id) + 1
        customer_data= {'id': str(new_id)}
        customer_data['first_name'] = input('Enter first name: \n')
        if customer_data['first_name'].isalpha() != True:
            print('\n -- First name must be letters only --')
            return 'bad info'
        customer_data['last_name']  = input('Enter last name: \n')
        if customer_data['last_name'].isalpha() != True:
            print('\n -- Last name be letters only --')
            return 'bad info'
        x=input('Enter account type:\n ("sx" = standard account, "px" = premium account, "sf" = standard family account, "pf" = premium family account) \n')
        if x == 'sx' or x == 'sf' or x == 'px' or x == 'pf':
            customer_data['account_type'] = x
        else:
            print('\n -- Account type did not match any options --')
            return 'bad info'
        return customer_data