import pandas as pd 
import numpy as np 


df1=pd.read_csv('./TMDB/credit.csv')
df2=pd.read_csv('./TMDB/movie.csv')
df1.columns = ['id','tittle','cast','crew']
df2= df2.merge(df1,on='id')
df2['overview'].head(5)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')
df2['overview'] = df2['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(df2['overview'])


from sklearn.metrics.pairwise import linear_kernel


cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df2.index, index=df2['title']).drop_duplicates()


def get_recommendations(title, cosine_sim=cosine_sim):

    
        

        idx = indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [i[0] for i in sim_scores]

        
        result = df2['title'].iloc[movie_indices]
        resultArray = result.to_numpy()

        return resultArray
    


# if 'The Avengers' in df2.values:
#     print("Present")
# else:
#     print("Not Present")




# rec = get_recommendations('The Dark Knight Rises')
# print(rec)

