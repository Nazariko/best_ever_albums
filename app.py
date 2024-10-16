from flask import Flask , render_template , request , redirect, url_for
import db_tools

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
    artists = db_tools.get_artists())

@app.route('/artist/<int:pk>')
def artist_detail(pk):
    artist, albums = db_tools.get_artist(pk=pk)
    return render_template('artist_detail.html',
    artist=artist,
    albums=albums)

@app.route('/genre/<int:pk>')
def genre_details(pk):
    genre , artist = db_tools.get_genre(pk=pk)
    return render_template('genre_details.html',
                           genre=genre,
                           artists=artist)

@app.route('/add/album' ,methods=['POST'])
def add_album():
  artist_id = request.form.get('artist_id')
  name = request.form.get('name')
  year = request.form.get('year')
  charts = request.form.get('charts')
  print('!!!' ,(artist_id , name , year , charts))

  return redirect(url_for('artist_detail' , pk=1))

if __name__ == '__main__':
    app.run(debug=True , port=5000)