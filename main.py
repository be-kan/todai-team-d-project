from flask import Flask, render_template, request
import urllib
import json
from requests_oauthlib import OAuth1Session


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
    channel_url = 'https://www.googleapis.com/youtube/v3/channels?'
    play_list_url = 'https://www.googleapis.com/youtube/v3/playlistItems?'
    channel_id = 'UCZf__ehlCEBPop-_sldpBUQ'
    youtube_key = app.config['YOUTUBE_KEY']

    channel_param = {
        'part': 'contentDetails',
        'id': channel_id,
        'key': youtube_key
    }

    paramStr = urllib.parse.urlencode(channel_param)
    with urllib.request.urlopen(channel_url + paramStr) as res:
        channel_data = json.loads(res.read().decode("utf-8"))

    play_list_id = channel_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    play_list_param = {
        'part': 'snippet',
        'playlistId': play_list_id,
        'maxResults': 50,
        'key': youtube_key
    }

    paramStr = urllib.parse.urlencode(play_list_param)
    with urllib.request.urlopen(play_list_url + paramStr) as res:
        play_list_data = json.loads(res.read().decode("utf-8"))

    return render_template('sample_be-kan.html', data=play_list_data)


@app.route('/twitter_sample')
def twitter_sample():
    twitter = OAuth1Session(app.config['API_KEY'],
                            app.config['API_SECRET'],
                            app.config['ACCESS_TOKEN'],
                            app.config['ACCESS_TOKEN_SECRET'])

    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

    params ={
                'count' : 100,
                'screen_name':'hikakin'
            }
    req = twitter.get(url, params = params)
    timeline = json.loads(req.text)

    tweet_text = []
    tweet_time = []
    for tweet in timeline:
        tweet_text.append(tweet["text"])
        tweet_time.append(tweet["created_at"])

    return render_template('sample_nakatomotoi.html', tweet_text=tweet_text, tweet_time=tweet_time)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
