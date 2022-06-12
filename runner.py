from classes.store import Store

store= Store("Blockbuster")

def menu(store_name):
    while True:
        mode = input("\n== Welcome to Code Platoon Video! ==\n\n1. View store video inventory\n2. View customer rented videos\n3. Add new customer\n4. Rent video\n5. Return video\n6. Exit\n")

        if mode == '1':
            store.list_videos()

        elif mode == '2':
            store.list_customers()
            customer_id = input('\nEnter customer id:')
            x=next((store.find_video_by_id(customer_id) for customer in store.curr_customers if customer.id == customer_id),('\n -- No account matches that id --'))
            print(x)
            
        elif mode == '3':
            customer_data= store.get_data()
            if customer_data =='bad info':
                menu(store)
            store.add_customer(customer_data)

        elif mode == '4':
            store.list_videos()
            video_to_rent= input('\nEnter the title of the movie you wish to rent: \n')
            store.list_customers()
            customer_id= input('\nEnter customer id: \n')
            x= next(( store.rent_video(video,customer_id) for video in store.curr_inventory if video.title.lower() == video_to_rent.lower()), "\n-- We do not have any titles by that name, please recheck spelling.--")
            print(x)

        elif mode == '5':
            store.list_videos()
            video_to_rent= input('\nEnter the title of the movie you wish to return: \n')
            store.list_customers()
            customer_id= input('\nEnter customer id: \n')
            x= next(( store.return_video(video,customer_id) for video in store.curr_inventory if video.title.lower() == video_to_rent.lower()), "\n-- We do not have any titles by that name, please recheck spelling.--")
            print(x)

        elif mode == '6':
            print("\n -- Good Bye! --\n")
            break

menu(store)