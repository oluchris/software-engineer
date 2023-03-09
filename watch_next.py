import spacy 

# Using advanced language model
nlp = spacy.load('en_core_web_md')

# Variable stores movie description
movie_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."


# Returns the next movie a user will likely watch 
def next_movie(descr):
    movies = []

    # Reads details from the txt
    movie_file = open("movies.txt", "r", encoding="utf-8")

    for data in movie_file:
        data = data.strip("\n").split(" :")

        # Compares the similarity of the movie_description and the description from movies.txt.
        token = nlp(descr)
        token_ = nlp(data[1])

        # Stores the similarity index and and movie name
        movie_titles = [token.similarity(token_), data[0]]
        
        # Appends the similarity index and and movie name to the list movies
        movies.append(movie_titles)

    # Sorts movies based on the similarity index scores from lowest to highest    
    movies.sort()

    movie_file.close() # Close file

    # Return the movie title with the highest similarity index scores
    return movies[len(movies)-1][1]


# Stores the movie title with the highest similarity index scores
similar_title = next_movie(movie_description)

# Prints the movie title with the highest similarity index scores
print(f"The title of the most similar movie is {similar_title}")