import webbrowser#imports the library webbrowser 


class Movie():# This is where I make my Movie class

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self,movie_title,movie_storyline,poster_image,
		trailer_youtube):#These are the parameters that I pass the function
		self.title = movie_title#This gives my object the movie title
		self.storyline = movie_storyline#This gives my object the storyline
		self.poster_image_url = poster_image#This gives my image it's poster.
		self.trailer_youtube_url = trailer_youtube#This gives my object
		#it's trailer

	def show_trailer(self):#function used to view trailers
		webbrowser.open(self.trailer_youtube_url)#webbrowser connects to desired
		#youtube url


