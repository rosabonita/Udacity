import media, fresh_tomatoes

star_wars_iv = media.Movie("Star Wars IV: A New Hope",
                           "A Princess stands against evil",
                           "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                           "https://youtu.be/vP_1T4ilm8M")

star_wars_v = media.Movie("Star Wars IV: Empire Strikes Back",
                          "A Princess wages war against tyranny",
                          "http://whatanerdgirlsays.com/wp-content/uploads/2013/06/url-6.jpeg?w=194",
                          "https://youtu.be/-LuGkTtITQE")

star_wars_vii = media.Movie("Star Wars VI: The Force Awakens",
                            "A scavenger salvages the rebellion",
                            "http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2015/10/star-wars-force-awakens-official-poster.jpg",
                            "https://youtu.be/sGbxmsDFVnE")

hobbit = media.Movie("The Hobbit: An Unexpected Journey",
                     "Not all who wander are lost",
                     "http://goodfilmguide.co.uk/wp-content/uploads/2012/09/Hobbit-Bilbo-Poster.jpg",
                     "https://youtu.be/5xpcwquIpRQ")

brave = media.Movie("Brave",
                    "A girl defies tradition to follow her heart",
                    "http://www.freemovieposters.net/posters/brave_2012_5791_poster.jpg",
                    "https://youtu.be/TEHWDA_6e3M")

land_before_time = media.Movie("The Land Before Time",
                               "Little lost dinosaurs find home and eachother",
                               "http://www.impawards.com/1988/posters/land_before_time.jpg",
                               "https://youtu.be/lpnwK2NGxIo")
                            
movies = [star_wars_iv, star_wars_v, star_wars_vii, hobbit, brave, land_before_time]

fresh_tomatoes.open_movies_page(movies)

