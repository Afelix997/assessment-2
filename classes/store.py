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
            print(f'{i+1}. Title: {video.title} ------ Video id:{video.id}')

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

    def rent_video(cls,video_title,customer_id):
        