# import spacy
import spacy

# import warning to fix W008 problem
import warnings

warnings.filterwarnings("ignore", message=r"\[W008\]", category=UserWarning)

# use 'en_core_web_md'
nlp = spacy.load('en_core_web_md')

# user input form the task assignment
user_input = "“Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a  planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"

# open movies file
with open("movies.txt", "r") as movie:
    movie_data = []  # empty  list for movie data
    score_data = []  # empty list for score
    movie_name_list = []  # empty  list for movie name
    for i in movie:
        movie_data = i.split(':')  # separate name and description
        movie_name_list.append(movie_data[0])  # store name in movie_name_list
        token = nlp(movie_data[1])  # nlp
        score = 0  # for each movie, the start score is zero
        for token_ in user_input.split(' '):  # compare every word of user input
            token_ = nlp(token_)
            score += token.similarity(token_)  # add score at total score
        score_data.append(score)  # add score to score list

    # print(score_data)
    print(f"The score list : {score_data}")  # score list
    print(f"The highest score movie is : {movie_name_list[score_data.index(max(score_data))]}")  # result
