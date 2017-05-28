# Imports the files needed to crate my movie objects

import media
import fresh_tomatoes

# Following Are my favorite movie objects.

# Code for Lord of The rings object

lotr = media.Movie(
    'Lord of The Rings',
    'A quest to get rid of the ring to rule them all',
    'https://image.ibb.co/gccbWQ/index.jpg',
    'https://www.youtube.com/watch?v=V75dMMIW2B4',
    None)

# Code for batman: The Dark Knight object

batman = media.Movie(
    'Batman: The Dark Knight ',
    'A crazy man who wants the world to burn '
    'is after the batman.',
    'https://image.ibb.co/b9sod5/bat.jpg',
    'https://www.youtube.com/watch?v=EXeTwQWrcwY',
    None)

# Code for Star Wars Episode 4 object

star_wars = media.Movie(
    'Star Wars Episode IV A New Hope',
    'In a galaxy far far away a plan to stop '
    'an empire is underway',
    'https://image.ibb.co/c5BQQk/sw.jpg',
    'https://www.youtube.com/watch?v=9gvqpFbRKtQ',
    '2:20')

# Code for Half Baked object.

half_baked = media.Movie(
    'Half Baked',
    'A story of a group of stoners who try'
    ' to get their friend out the joint',
    'https://image.ibb.co/eGaVrQ/hb.jpg',
    'https://www.youtube.com/watch?v=-O4wMW1-tkY',
    None)

# Code for Jaws object.

jaws = media.Movie(
    'Jaws',
    'A story about a giant killer shark',
    'https://image.ibb.co/cFDGWQ/jaws.jpg',
    'https://www.youtube.com/watch?v=U1fu_sA7XhE',
    '1:45')

# Code for Joe Dirt. object

joe_dirt = media.Movie(
    'Joe dirt',
    'A Hillbilly tries to find his parents',
    'https://image.ibb.co/mjhX5k/joe.jpg',
    'https://www.youtube.com/watch?v=FpHIIE9Lois',
    None)

# Code for Fight Club object

fight_club = media.Movie(
    'Fight Club',
    'a weak regular man ends up finding himself'
    ' making a fight club',
    'https://image.ibb.co/jRnbWQ/fc.jpg',
    'https://www.youtube.com/watch?v=SUXWAEX2jlg',
    None)
#Code for forrest gump object
forrest_gump = media.Movie(
    'Forrest Gump',
    'An epic tale of a mans amazing journey '
    'trough life',
    'https://image.ibb.co/h63rWQ/fg.jpg',
    'https://www.youtube.com/watch?v=YNh9Es8Ut6U',
    None)

#Code for Kill Bill object
kill_bill = media.Movie(
    'Kill Bill: Volume 1',
    'A woman brtrayed seeks revenge',
    'https://image.ibb.co/dJUZJ5/kb.jpg',
    'https://www.youtube.com/watch?v=ot6C1ZKyiME',
    '2:30')

#Code for Pulp Fiction object
pulp = media.Movie(
    'Pulp Fiction',
    'Say what one more time motherfucker. Say what',
    'https://image.ibb.co/c26EJ5/pf.jpg',
    'https://www.youtube.com/watch?v=s7EdQ4FqbhY',
    None)

#Code for the Hobbit object
hobbit = media.Movie(
    'The hobbit',
    'A hobbit embarks on a journey of a lifetime',
    'https://image.ibb.co/m0q8d5/hobbit.jpg',
    'www.youtube.com/watch?v=4QZ4tdIPGJQ',
    None)

#Code for 300 object
three = media.Movie(
    '300',
    'Can a small band of spartan warriors fight'
    ' a persian army?',
    'https://image.ibb.co/hHqVrQ/300.jpg',
    'https://www.youtube.com/watch?v=UrIbxk7idYA',
    None)
# Array with movies

movies = [
    forrest_gump,
    star_wars,
    batman,
    lotr,
    joe_dirt,
    half_baked,
    fight_club,
    jaws,
    pulp,
    hobbit,
    three,
    kill_bill
    ]

fresh_tomatoes.open_movies_page(movies)
