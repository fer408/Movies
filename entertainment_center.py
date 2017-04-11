#Imports the files needed to crate my movie objects
import media
import fresh_tomatoes

#Following Are my favorite movies.

#Code for Lord of The rings
lotr = media.Movie("Lord of The Rings",
					"A quest to get rid of the ring to rule them all",
					"https://en.wikipedia.org/wiki/The_Lord_of_the_Rings_(film_series)",
					"https://www.youtube.com/watch?v=V75dMMIW2B4")

#Code for batman: The Dark Knight
batman = media.Movie("Batman: The Dark Knight ",
					 "A crazy man who wants the world to burn is after the batman. Why so serios?",
					 "https://en.wikipedia.org/wiki/The_Dark_Knight_(film)#/media/File:Dark_Knight.jpg",
					 "https://www.youtube.com/watch?v=EXeTwQWrcwY")
#Code for Star Wars Episode 4
star_wars = media.Movie("Star Wars Episode IV A New Hope",
						"In a galaxy far far away a plan to stop a weapon of catrastophic proportions is underway",
						"https://en.wikipedia.org/wiki/Star_Wars_(film)#/media/File:StarWarsMoviePoster1977.jpg",
						"https://www.youtube.com/watch?v=9gvqpFbRKtQ")
#Code for Half Baked.
half_baked = media.Movie("Half Baked",
                         "A story of a group of stoners who try to get their friend out the joint",
                         "https://en.wikipedia.org/wiki/Half_Baked#/media/File:Half-baked-dvd-cover.jpg",
                         "https://www.youtube.com/watch?v=-O4wMW1-tkY")
#Code for Jaws.
jaws = media.Movie("Jaws",
                   "A story about a giant killer shark",
                   "https://en.wikipedia.org/wiki/Jaws_(film)#/media/File:JAWS_Movie_poster.jpg",
                   "https://www.youtube.com/watch?v=U1fu_sA7XhE")
#Code for Joe Dirt.
joe_dirt = media.Movie("Joe dirt",
                       "A Hillbilly tries to find his parents but ends up finding family in other places",
                       "https://en.wikipedia.org/wiki/Joe_Dirt#/media/File:Joe_dirt.jpg",
                       "https://www.youtube.com/watch?v=FpHIIE9Lois")

#Code for Fight Club
fight_club = media.Movie("Fight Club",
                         "a weak regular man ends up finding himself trough beating up his buddies in a secret club",
                         "https://en.wikipedia.org/wiki/Fight_Club#/media/File:Fight_Club_poster.jpg",
						 "https://www.youtube.com/watch?v=SUXWAEX2jlg")

forrest_gump = media.Movie("Forrest Gump",
                           "An epic tale of a mans amazing journey trough life",
                           "https://en.wikipedia.org/wiki/Forrest_Gump#/media/File:Forrest_Gump_poster.jpg",
							"https://www.youtube.com/watch?v=YNh9Es8Ut6U")

#Array with movies 
movies = [forrest_gump,star_wars,batman,lotr,joe_dirt,half_baked,fight_club,jaws]


fresh_tomatoes.open_movies_page(movies)