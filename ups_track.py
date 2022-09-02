from flask import render_template

from application import app
from models.track import Track


@app.route('/')
def index():
    tracks = Track.query
    return render_template('track_table.html', users=tracks)


if __name__ == '__main__':
    app.run(port=7002)
