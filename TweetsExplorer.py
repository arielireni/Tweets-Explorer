from tkinter import *
from tkinter import ttk
import tweepy as tw


class MyTweetsExplorer:
    def __init__(self, master):
        # main frame
        self.main_frame = Frame(master)
        self.main_frame.pack(fill=BOTH, expand=1)

        # canvas
        self.canvas = Canvas(self.main_frame)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # scrollbars
        self.y_scrollbar = ttk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.canvas.yview)
        self.y_scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.y_scrollbar.set)

        self.x_scrollbar = ttk.Scrollbar(self.main_frame, orient=HORIZONTAL, command=self.canvas.xview)
        self.x_scrollbar.pack(side=BOTTOM, fill=X)
        self.canvas.configure(xscrollcommand=self.x_scrollbar.set)

        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # create frames inside the canvas
        self.top_frame = Frame(self.canvas)
        self.bottom_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.top_frame, anchor="n")
        self.canvas.create_window((200, 300), window=self.bottom_frame, anchor="s")

        # add widgets to the top frame
        self.label_1 = Label(self.top_frame, text="Keywords", font=("gisha", 12), fg="blue")
        self.label_2 = Label(self.top_frame, text="Date since", font=("gisha", 12), fg="blue")
        self.label_3 = Label(self.top_frame, text="Number of tweets", font=("gisha", 12), fg="blue")

        self.entry_1 = Entry(self.top_frame)
        self.entry_2 = Entry(self.top_frame)
        self.entry_3 = Entry(self.top_frame)

        self.label_1.grid(row=0)
        self.label_2.grid(row=1)
        self.label_3.grid(row=2)

        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)
        self.entry_3.grid(row=2, column=1)

        self.search_button = Button(self.top_frame, text="Search", command=self.search, font=("gisha", 12), bg="blue", fg="white")
        self.search_button.grid(row=3, column=1)

    def search(self):

        consumer_key = 'PfpawUW289AetyAwhJunxF9Lt'
        consumer_secret = 'iVLOkiNuMU5vtHnELRGX8EN2gSkPHoHNNAheUfJ8f2lkd9nww2'
        access_token = '1303032794189361152-Ire5CfJXOn1GiZmyR3Vd5bLPlVTbp5'
        access_token_secret = 'OZKTOUnIM5i2iemy3YJlApR47JDJvglE83aGff3zklV2r'

        auth = tw.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tw.API(auth, wait_on_rate_limit=True)

        search_words = self.entry_1.get()
        date_since = self.entry_2.get()
        num_of_items = self.entry_3.get()
        search_without_retweets = search_words + " -filter:retweets"

        tweets = tw.Cursor(api.search, q=search_without_retweets, lang="en", since=date_since).items(int(num_of_items))

        # collect information into a list
        lst = [[tweet.user.screen_name, tweet.text] for tweet in tweets]
        Label(self.bottom_frame, text="Username", fg="white", bg="black", font=("gisha", 10)).grid(row=0, column=0)
        Label(self.bottom_frame, text="Text", fg="white", bg="black", font=("gisha", 10)).grid(row=0, column=1)

        for i in range(int(num_of_items)):
            for j in range(2):
                Label(self.bottom_frame, text=lst[i][j], fg="blue", bg="white", font=("gisha", 10)).grid(row=i + 1, column=j)


root = Tk()
root.title("Tweets Explorer")
root.geometry('700x500')
obj = MyTweetsExplorer(root)
root.mainloop()
