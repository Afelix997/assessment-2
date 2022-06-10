from classes.store import Store

store= Store("Blockbuster")

while True:
    mode = input("\n== Welcome to Code Platoon Video! ==\n\n1. View store video inventory\n2. View customer rented videos\n3. Add new customer\n4. Rent video\n5. Return video\n6. Exit\n")

    if mode == '1':
        store.list_videos()
    elif mode == '2':
        store.list_customers()
        customer_id = input('\nEnter customer id:')
        print(str(store.find_video_by_id(customer_id)))
    elif mode == '3':

        new_id = int(store.curr_customers[-1].id) + 1
        customer_data= {'id': str(new_id)}
        customer_data['account_type'] = input('Enter account type:\n ("sx" = standard account, "px" = premium account, "sf" = standard family account, "pf" = premium family account) \n')
        customer_data['first_name'] = input('Enter first name: \n')
        customer_data['last_name']  = input('Enter last name: \n')
        store.add_customer(customer_data)
    elif mode == '4':
        store.list_videos()
        video_to_rent= input('\nEnter the title of the movie you wish to rent: \n')
        store.list_customers()
        customer_id= input('\nEnter customer id: \n')
        store.rent_video(video_to_rent,customer_id)
    elif mode == '6':
        break

