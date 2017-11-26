"""
Data file, contains constants as Python serialized data.
"""

from lib.media import Movie

MOVIES = [
    Movie(
        "The Lord of the Rings: The Fellowship of the Ring",
        "resources/images/lotr_1_movie_poster.jpg",
        "https://www.youtube.com/watch?v=Pki6jbSbXIY"
    ),
    Movie(
        "Princess Mononoke",
        "resources/images/princess_mononoke_movie_poster.jpg",
        "https://www.youtube.com/watch?v=4OiMOHRDs14"
    ),
    Movie(
        "Sword of the Stranger",
        "resources/images/sword_of_the_stranger_movie_poster.jpg",
        "https://www.youtube.com/watch?v=cyZLOYAbp4w"
    )
]
