import pandas as pd 
from sqlalchemy import create_engine

url1 = 'https://raw.githubusercontent.com/4GeeksAcademy/k-nearest-neighbors-project-tutorial/main/tmdb_5000_movies.csv'

url2 = 'https://raw.githubusercontent.com/4GeeksAcademy/k-nearest-neighbors-project-tutorial/main/tmdb_5000_credits.csv'
# your code here

movie_df = pd.read_csv(url1)
credits_df = pd.read_csv(url2)

#print(movie_df)
#print(credits_df)


#configuro la conexion de la Bdd
db_url = 'postgresql://gitpod@localhost:5432/movie_db'
eng = create_engine(db_url)

movie_df.to_sql('movies', eng, if_exists='replace', index=False)
credits_df.to_sql('credits', eng, if_exists='replace', index=False)

#Conexion a la Bdd 
with eng.connect() as connection:
    query = """
        CREATE TABLE unifica_movies AS
        SELECT 
            m.id AS movie_id,
            m.title,
            m.overview,
            m.genres,
            m.keywords,
            c.cast,
            c.crew
        FROM movies m 
        JOIN credicts c 
        ON m.title = c.title;
        """
    connection.execute(query)

dfUnificada = pd.read_sql_table('unified_movies', eng)

print(dfUnificada.columns)