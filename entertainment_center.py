import time
import fresh_tomatoes # To able to open a webpage on browser
import media


# Create the movie instances

DAVID_AND_GOLIATH =media.Movie(
                       "DAVID AND GOLIATH",
                       "The story of how Goliath or Gath a giant Philistine " 
                       "warrior was defeated by the young David",
                       "https://upload.wikimedia.org/wikipedia/en/2/25/David_and_Goliath_1960.jpg", # noqa
                       "https://www.youtube.com/watch?v=Vvnwq4p_E9c")


Anne_Frank = media.Movie(
                     "Anne Frank",
                     "The story of a young Jewish victim of the Holocaust",
                     "https://upload.wikimedia.org/wikipedia/en/0/05/Anne_Frank_The_Whole_Story_cover.jpg", # noqa
                     "https://www.youtube.com/watch?v=2jqgT2Lxs5Q")



Twelve_Years_a_Slave = media.Movie(
                     "12 Years a Slave",
                     "The stories of the years before the Civil War,of " 
                     "Solomon Northup who was kidnapped and sold into slavery",
                     "http://ecx.images-amazon.com/images/I/41C3lyI9YCL._SX200_QL80_.jpg", # noqa
                     "https://www.youtube.com/watch?v=OwYd9luIT1k")


HELEN_KELLER = media.Movie(
                     "HELEN KELLER THE STORY OF MY LIFE",
                     "The story of Helen Adams Keller the first deafblind "
                     "person to earn a bachelor of arts degree",
                     "http://270c81.medialib.glogster.com/media/0a/0a03c97a2c35c038dd763c30786cf91b40391e45c6b05155d2a0015a3b118259/helen-keller313x395.gif", # noqa
                     "https://www.youtube.com/watch?v=-3kqkHT3HzM")




The_Last_Train_to_Auschwitz = media.Movie(
                     "The Last Train to Auschwitz",
                     "The stories of several Jews as they sit in crowded "
                     "cattle cars en route to death camps",
                     "https://s.s-bol.com/imgbase0/imagebase3/large/FC/7/1/0/5/9200000045845017.jpg", # noqa
                     "https://www.youtube.com/watch?v=VgnqgF3XGUk")



Joshua_and_the_Battle_of_Jericho = media.Movie(
                     "Joshua and the Battle of Jericho",
                     "The story of how a warrior and his armies "
                     "mysteriously conquered the city of Jericho "
                     "in the ancient times",
                     "http://betterbibleteachers.com/wp-content/uploads/2015/11/Joshua-Jericho.jpg", # noqa
                     "https://www.youtube.com/watch?v=aFysYErsgGA")








# Define an array of all your movie instances
movies = [DAVID_AND_GOLIATH,
          Anne_Frank,
          Twelve_Years_a_Slave,
          HELEN_KELLER,
          The_Last_Train_to_Auschwitz ,
          Joshua_and_the_Battle_of_Jericho ]
        
fresh_tomatoes.open_movies_page(movies)
