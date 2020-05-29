import pandas as pd 
import numpy as np 
import pickle 

df1=pd.read_csv('./TMDB/credit.csv')
df2=pd.read_csv('./TMDB/movie.csv')


C= df2['vote_average'].mean()
m= df2['vote_count'].quantile(0.9)
def popular_movies():

    q_movies = df2.copy().loc[df2['vote_count'] >= m]
    q_movies.shape

    def weighted_rating(x, m=m, C=C):
        v = x['vote_count']
        R = x['vote_average']
        return (v/(v+m) * R) + (m/(m+v) * C)
    

    q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

    q_movies = q_movies.sort_values('score')

    #Print the top 10 movies
    q_movies[['title', 'vote_count', 'vote_average', 'score']].head(10)
    result = q_movies.loc[:,'title'].head(10)
    resultArray = result.to_numpy()

    return resultArray
  
popularMovies = popular_movies()


print(popularMovies)



