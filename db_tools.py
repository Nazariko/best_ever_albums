import sqlite3

def get_artists():
    query ='''
    SELECT artists.id ,artists.name as artist_name,
    genres.name as genre_name, artists.img ,
    genres.id as genre_id,
    SUM(albums.charts) as total_charts
    FROM artists
    INNER JOIN genres
    ON genres.id==artists.genre_id
    INNER JOIN albums
    ON albums.artist_id == artists.id
    GROUP BY artists.id
    ORDER BY total_charts DESC;
    '''
    with sqlite3.connect('bestalbums.sqlite3') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        data = cursor.execute(query).fetchall()
        return [dict(row) for row in data]


def get_artist(pk):
    query1 ='''
    SELECT artists.id ,artists.name,
    genres.name as genre_name, artists.img ,
    genres.id as genre_id
    FROM artists
    INNER JOIN genres
    ON genres.id==artists.genre_id
	WHERE artists.id=?;
    '''
    query2='''
    SELECT * 
    FROM albums 
    WHERE albums.artist_id = ? 
    ORDER BY albums.year;
    '''
    with sqlite3.connect('bestalbums.sqlite3') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        data1 = cursor.execute(query1 , (pk,)).fetchone()
        data2 =cursor.execute(query2 , (pk,)).fetchall()
        return dict(data1) , [dict(row) for row in data2]

def get_genre(pk):
    query1 ='''
    SELECT * 
    FROM genres
    WHERE genres.id==?;
    '''
    query2='''
    SELECT *
    From artists
    WHERE artists.genre_id == ?
    ORDER BY artists.name;
    '''
    with sqlite3.connect('bestalbums.sqlite3') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        data1 = cursor.execute(query1 , (pk,)).fetchone()
        data2 =cursor.execute(query2 , (pk,)).fetchall()
        return dict(data1) , [dict(row) for row in data2]

def insert_album(pk):
    query1 ='''
    INSERT INTO albums
    (name, artist_id,year,charts)
    VALUES
    (?,?,?,?);
    '''
    with sqlite3.connect('bestalbums.sqlite3') as connection:
        cursor = connection.cursor()
        cursor.execute(query1,(name, artist_id,year,charts))
        connection.commit()

if __name__ == '__main__':
    print(get_artist(pk=7))
    print(get_genre(pk=4))