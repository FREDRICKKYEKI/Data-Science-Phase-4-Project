"""
Contains movie recommendation functions
"""
import pandas as pd
import pickle as pkl
import random

# random.seed(555)


# Datasets
movies = "../../data/ml-latest-small/movies.csv"
links = "../../data/ml-latest-small/links.csv"
ratings = "../../data/ml-latest-small/ratings.csv"
tags = "../../data/ml-latest-small/tags.csv"

data = {"movies":None, "links": None, "ratings": None, "tags": None}

for key, _ in data.items():
    data[key] = pd.read_csv(f"data/ml-latest-small/{key}.csv")

knnrc_df = pd.read_pickle("functions/pickles/knn_pv")

with open("functions/pickles/recom_model", "rb") as f:
    model_knn = pkl.load(f)



new_indices = {value: index for index, value in enumerate(knnrc_df.index)}


movies_df = data["movies"]

links_df = data["links"]

merged_movies_links = movies_df.join(links_df.set_index("movieId"), on="movieId", how="inner")

indices = pd.Series(merged_movies_links.index, index=merged_movies_links['title']).drop_duplicates()

# Left outer join with ratings_df and specify suffixes
merged_data_ratings = merged_movies_links.join(data["ratings"].set_index("movieId"), on="movieId", how="left", lsuffix='_movies_links', rsuffix='_ratings')

# Left outer join with tags_df and specify suffixes
df = merged_data_ratings


def get_title(text, df=df):
    """Gets movie title matching `text`
    returns:
        title - title of movie matching the input
        genres - the movie's genres
    """
    mask = df['title'].str.contains(text, case=False, regex=False)
    title = df.loc[mask, 'title'].head(1).values[0] if any(mask) else None

    if not title:
        print(f"\n'{text}' does not match any movies. Please try again")
        return None, None

    return title, df.loc[mask].head(1)["genres"].values[0]

def give_rec(title, rec=10):
    """Get the index corresponding to title content based"""
    try:
        with open("functions/pickles/sig", "rb") as f:
            sig = pkl.load(f)
        # get title
        title, genres = get_title(title, merged_movies_links)

        # print the movie title matching the text
        if title:
            print(f"[CONTENT-BASED] Recommendation for {title}")
            print("Genres: ", genres)

        idx = indices[title]

        # Get the pairwsie similarity scores
        sig_scores = list(enumerate(sig[idx]))

        # Sort the movies
        sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

        sig_scores = sig_scores[1:rec]

        # Movie indices
        movie_indices = [i[0] for i in sig_scores]

        # Top 10 most similar movies
        return merged_movies_links.iloc[movie_indices].drop_duplicates()
    except Exception as _:
        print(_)
        return "⚠ Oops! Something went wrong!"


def knn_get_rec(title, rec=10, verbose=True):
    """Get recommendations for a movie using KNN
    """
    # create a return dataframe
    ret_df = pd.DataFrame()
    # initiate an empty list to fill the knn distances
    dists = []
    try:
        # get movie details and the pivot matrix index
        title, genres = get_title(title, df)
        idx = new_indices[title]

        # compute the knn distance and index
        distances, knn_indices = model_knn.kneighbors(knnrc_df.iloc[idx,:].values.reshape(1, -1), n_neighbors = rec)

        if title and verbose:
            print(f'[KNN] Recommendations for {title}:')
            print(f"Genres: {', '.join(genres.split('|'))}")

        for i in range(0, len(distances.flatten())):
            if i == 0:
                continue
            rec_movie = knnrc_df.index[knn_indices.flatten()[i]]
            movies_df = merged_movies_links
            mask = movies_df['title'].str.contains(rec_movie, case=False, regex=False)

            # fill in return dataframe
            ret_df = pd.concat([ret_df, movies_df[mask]])

            # fill in the knn distances in the df
            dists.append(distances.flatten()[i])

        ret_df["knn_distance"] = dists

        if len( list(ret_df["title"])) < 1:
            return give_rec(title, rec=rec)

        return ret_df.sample(frac=1)

    except Exception as _:
        print("⚠ Oops! Something went wrong!", _)
        return  give_rec(title, rec=rec)


def unpersonalized_recomm(count=10):
    """Returns a randomlist of highly ranked movies movies"""
    unique_genres = list(set(df['genres'].str.split('|', expand=True).stack()))

    recomms = pd.DataFrame()
    for genre in unique_genres:
        # select top 5 of each genre
        mask = df["genres"].str.contains(genre, regex=False, case=False)
        top_5 = df[mask].sort_values(by="rating", ascending=False).head()
        top_5["year_of_release"] = top_5["title"].map(lambda x: x[-5:].strip(")"))
        recomms = pd.concat([recomms, top_5])

    # return shuffled
    print("[UNPERSONALIZED]")
    return recomms.sample(frac=1).drop_duplicates().head(count)

def top_ten_highly_rated(uid, rec=10):
    """returns a list of movies highly rated by a user"""
    mask = data["ratings"]['userId'] == uid
    user_movies = data["ratings"][mask].sort_values(by=['rating'], ascending=False).head(rec)
    user_movies = pd.merge(data["movies"], user_movies, how="inner", on="movieId")

    if len(user_movies) < 1:
        raise ValueError(f"User denoted by id: '{uid}' does not exist!")



def final_recommender(uid=None, rec=10):
    """Get recommendations for a movie using KNN
    params:
    =======
    uid - user id
    rec - recommendation movie count
    """
    if not uid:
        return unpersonalized_recomm(rec)
    # create a return dataframe
    ret_df = pd.DataFrame()
    # initiate an empty list to fill the knn distances
    try:
        # get top 10 movies
        top_user_movies = top_ten_highly_rated(uid, rec)

        for i in range(rec):
            # random title from top 10 movies highly ranked by user
            random_title = top_user_movies[random.randint(0, 5)]

            # get the full title
            title, _ = get_title(random_title, df)

            # get recommendation of random title
            movie_rec = knn_get_rec(title, rec, verbose=False)

            # if not dataframe continue
            if type(movie_rec) is str:
                continue
            # sort by distance (ascending)
            ret_df = movie_rec.sort_values(by="knn_distance")

            # fill in the return df
            ret_df = pd.concat([ret_df, ret_df.head()])

            # drop dups
            ret_df = ret_df.drop_duplicates()

        print(f"Recommendation for user id: {uid}")


        return ret_df

    except Exception as _:
        print(_)
        return "⚠ Oops! Something went wrong!"
