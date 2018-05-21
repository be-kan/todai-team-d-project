from flask import Flask, render_template, request
import urllib
import json

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hikakin')
def kikakin():
    return render_template('hikakin.html')


@app.route('/youtube_sample')
def youtube_sample():
    youtube_url = 'https://www.googleapis.com/youtube/v3/channels?'
    youtube_key = app.config['YOUTUBE_KEY']

    param = {
        'part': 'statistics',
        'id': 'UCZf__ehlCEBPop-_sldpBUQ',
        'key': youtube_key
    }

    paramStr = urllib.parse.urlencode(param)

    with urllib.request.urlopen(youtube_url + paramStr) as res:
        data = json.loads(res.read().decode("utf-8"))

    print(data)

    subsc = int(data['items'][0]['statistics']['subscriberCount'])
    num_video = int(data['items'][0]['statistics']['videoCount'])
    num_view = int(data['items'][0]['statistics']['viewCount'])

    return render_template('sample_be-kan.html', subsc=subsc, num_video=num_video, num_view=num_view)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
