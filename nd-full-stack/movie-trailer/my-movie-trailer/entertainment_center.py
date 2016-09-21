import fresh_tomatoes
import media


the_matrix = media.Movie("The Matrix",
                          "Is this the real life? Is this just fantasy?",
                          "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                          "https://www.youtube.com/watch?v=m8e-FF8MsqU")

the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                          ("A man is falsely imprisoned for the murder of his"
                          "wife"),
                          "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                          "https://www.youtube.com/watch?v=6hB3S9bIaco")

pulp_fiction = media.Movie("Pulp Fiction",
                          ("An inter-twining tale of theft, drugs and amazing"
                          "dialogue!"),
                          "https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
                          "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

back_to_the_future = media.Movie("Back to the Future",
                          ("A teenager travels back to 1955 with the help of"
                          "an eccentric physicist"),
                          "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
                          "https://www.youtube.com/watch?v=qvsgGtivCgs")

finding_nemo = media.Movie("Finding Nemo",
                          ("A fish loses his son and goes out into the big,"
                          "wide ocean to look for him"),
                          "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
                          "https://www.youtube.com/watch?v=2zLkasScy7A")

forest_gump = media.Movie("Forest Gump",
                          "A simple man has a grand adventure!",
                          "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                          "https://www.youtube.com/watch?v=eYSnxZKTZzU")


movies = [the_shawshank_redemption, back_to_the_future, pulp_fiction,
          finding_nemo, forest_gump, the_matrix]

fresh_tomatoes.open_movies_page(movies)
