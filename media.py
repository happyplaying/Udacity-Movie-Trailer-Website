import webbrowser

class Movie():
    def __init__(self, id, title, description, year, poster, trailer):
        """ 
        A movie class has the following four attributes
        title = movie's title, string
        year = movie's release year, interger
        poster = movie's poster URL, string
        trailer = movie's trailer, string
        """
        self.id = id
        self.title = title
        self.description = description
        self.year = year
        self.poster = poster
        self.trailer = trailer

    def show_trailer():
        # a function to show the play the movie's trailer
        webbrowser.open(self.trailer)
