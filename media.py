import webbrowser

# Define the movie class
class Movie():
    """
    class Movie will allow us to create multiple instance of itself. In this
    particular project it will create instances like DAVID_AND_GOLIATH,
    Anne_Frank etc. This class Movie will remember the following data for all
    instances: title, storyline, poster_image, trailer_youtube.
    That means that if I say something like Anne_Frank.storyline the programme
    will print: The story of a young Jewish victim of the Holocaust.
    and if I said Anne_Frank.show_trailer() the programme will show Anne_Frank's
    youtube video.
    """
    # initialize a constructor to create space in memory for new instance
    def __init__(self,movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        The __init__ function is going to receive four arguments which it will pass
        the Movie variables below. This four arguments are:              
                     
        movie_title      -->  which is holds the title of the Movie e.g Anne_Frank Movie 
                              instace has its movie_title to be 'Anne Frank'.

        movie_storyline -->   which is holds the storyline of the Movie e.g Anne_Frank Movie 
                              instace has its movie_storyline to be 'The story of a 
                              young Jewish victim of the Holocaust'.


        poster_image     -->  which is holds the poster_image url link of the Movie e.g Anne_Frank Movie 
                              instace has its poster_image to be a url link which is
                              "https://upload.wikimedia.org/wikipedia/en/0/05/Anne_Frank_The_Whole_Story_cover.jpg".


        trailer_youtube  -->  which is holds the trailer_youtube url link of the Movie e.g Anne_Frank Movie 
                              instace has its trailer_youtube url link to be "https://www.youtube.com/watch?v=c25oZQrnXwc").

        """
        # initialize these instance variables below with the informations that init has received
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # define an instance method to call the webbroswer function
    def show_trailer(self):
        """
        This function as its name sugests will open a browser and play a movie.
        Remember to import the library 'webbrowser' in other use the webbrowser function below
        to open a browser.
        The link we want to open a brower is held by the variable 'trailer_youtube'.
        """
        webbrowser.open(self.trailer_youtube_url)

