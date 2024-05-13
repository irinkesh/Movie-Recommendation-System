import pickle

# Load data from the pickle file
with open('movie_list.pkl', 'rb') as f:
    data = pickle.load(f)

# Print the loaded data
print(data['title'].values)
url = "https://api.themoviedb.org/3/movie/{}?api_key=f8aea47494322294432476b722c91798&language=en-US".format(movie_id)