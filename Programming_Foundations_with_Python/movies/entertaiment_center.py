import media
import my_movies

toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'https://upload.wikimedia.org/wikipedia/uk/c/cd/Toy_story_1995_poster_ukr.jpg',
                        'https://www.youtube.com/watch?v=rMlMEfBJM08')

avatar = media.Movie('Avatar',
                     'A marine on an alien planet',
                     'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=4HFlPcX2HFo')

moulin_rouge = media.Movie('Moulin Rouge',
                           'The story of a young English poet/writer, Christian, who falls in love with the star of the Moulin Rouge, cabaret actress and courtesan Satine.',
                           'https://upload.wikimedia.org/wikipedia/en/9/9f/Moulin_rouge_poster.jpg',
                           'https://www.youtube.com/watch?v=-fCeivh5v0w')

school_of_rock = media.Movie('School of Rock',
                             'Using rock music to learn',
                             'https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
                             'https://www.youtube.com/watch?v=XCwy6lW5Ixc')

ratatouille = media.Movie('Ratatouille',
                          'A rat is a chef in Paris',
                          'https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg',
                          'https://www.youtube.com/watch?v=qWSRuZvKg_I')

midnight_in_paris = media.Movie('Midnight in Paris',
                                'Going back in time to meet authors',
                                'https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg',
                                'https://www.youtube.com/watch?v=BYRWfS2s2v4')

amelie = media.Movie('Amelie',
                     'The story of a shy waitress who decides to change the lives of those around her for the better, while struggling with her own isolation',
                     'https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg',
                     'https://www.youtube.com/watch?v=HUECWi5pX7o')
                     
movies = [toy_story, avatar, moulin_rouge, school_of_rock, ratatouille, midnight_in_paris, amelie]

my_movies.open_movies_page(movies)
