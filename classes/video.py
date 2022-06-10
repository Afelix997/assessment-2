import csv
import os.path

class Video:
    def __init__(self,id,title,rating,release_year,copies_available):
        self.id=id
        self.title=title
        self.rating=rating
        self.release_year=release_year
        self.copies_available= int(copies_available)
    
    def __str__(self):
        return f'\n{self.vid_title.upper()}\n---------------\nVideo ID: {self.vid_id}\tRating: {self.vid_rating}\tRealease Year:{self.rel_year}\n Copies Available To Rent: {self.copies_avail}'
   
    @classmethod
    def all_videos(cls):
        videos = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                videos.append(Video(**dict(row)))

        return videos
    def rent_video(self):
        if self.copies_available == 0:
            return ('No copies available')
        self.copies_available -= 1