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
    # channel_url = 'https://www.googleapis.com/youtube/v3/channels?'
    # play_list_url = 'https://www.googleapis.com/youtube/v3/playlistItems?'
    # channel_id = 'UCZf__ehlCEBPop-_sldpBUQ'
    # youtube_key = app.config['YOUTUBE_KEY']
    #
    # channel_param = {
    #     'part': 'contentDetails',
    #     'id': channel_id,
    #     'key': youtube_key
    # }
    #
    # paramStr = urllib.parse.urlencode(channel_param)
    # with urllib.request.urlopen(channel_url + paramStr) as res:
    #     channel_data = json.loads(res.read().decode("utf-8"))
    #
    # play_list_id = channel_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    #
    # play_list_param = {
    #     'part': 'snippet',
    #     'playlistId': play_list_id,
    #     'maxResults': 50,
    #     'key': youtube_key
    # }
    #
    # paramStr = urllib.parse.urlencode(play_list_param)
    # with urllib.request.urlopen(play_list_url + paramStr) as res:
    #     play_list_data = json.loads(res.read().decode("utf-8"))

    recent_ranking = {
      '1': {
        'image_url': 'http://i.ytimg.com/vi/WJzSBLCaKc8/hqdefault.jpg',  # OK
        'view_count': 68158348,
        'date': '2015/08/14'
      },
      '2': {
        'image_url': 'http://i.ytimg.com/vi/fWIR4T1Y48E/hqdefault.jpg',  # OK
        'view_count': 20112729,
        'date': '2016/01/15'
      },
      '3': {
        'image_url': 'http://i.ytimg.com/vi/x0WIWGAreS4/hqdefault.jpg',  # OK
        'view_count': 19702799,
        'date': '2015/02/13'
      },
      '4': {
        'image_url': 'http://i.ytimg.com/vi/O4vG1_Sa9VE/hqdefault.jpg',  # OK
        'view_count': 18213009,
        'date': '2014/11/08'
      },
      '5': {
        'image_url': 'http://i.ytimg.com/vi/pni05ZkWioQ/hqdefault.jpg',  # OK
        'view_count': 16804364,
        'date': '2013/11/09'
      },
      '6': {
        'image_url': 'http://i.ytimg.com/vi/oQSoETD63io/hqdefault.jpg',  # OK
        'view_count': 16197952,
        'date': '2014/04/26'
      },
      '7': {
        'image_url': 'http://i.ytimg.com/vi/UmgiPORUg5g/hqdefault.jpg',  # OK
        'view_count': 16090236,
        'date': '2017/06/04'
      },
      '8': {
        'image_url': 'http://i.ytimg.com/vi/DHa-dcNP00M/hqdefault.jpg',  # OK
        'view_count': 15561651,
        'date': '2014/07/19'
      },
      '9': {
        'image_url': 'http://i.ytimg.com/vi/l59ozZ8PzqU/hqdefault.jpg',  # OK
        'view_count': 14992612,
        'date': '2015/10/26'
      },
      '10': {
        'image_url': 'http://i.ytimg.com/vi/C4rOeTU0Vt4/hqdefault.jpg',  # OK
        'view_count': 14756540,
        'date': '2013/07/25'
      },
      '11': {
        'image_url': 'http://i.ytimg.com/vi/C3uJ-p0Olww/hqdefault.jpg',  # OK
        'view_count': 14148196,
        'date': '2015/09/11'
      },
      '12': {
        'image_url': 'http://i.ytimg.com/vi/Fze4EAhW2w0/hqdefault.jpg',  # OK
        'view_count': 14143857,
        'date': '2015/03/22'
      },
      '13': {
        'image_url': 'http://i.ytimg.com/vi/JGG09Oow8EE/hqdefault.jpg',  # OK
        'view_count': 13766063,
        'date': '2015/02/20'
      },
      '14': {
        'image_url': 'http://i.ytimg.com/vi/VLGeisJwXQ0/hqdefault.jpg',  # OK
        'view_count': 13745224,
        'date': '2015/04/08'
      },
      '15': {
        'image_url': 'http://i.ytimg.com/vi/ow9QW8vot2M/hqdefault.jpg',  # OK
        'view_count': 13428395,
        'date': '2014/06/27'
      },
      '16': {
        'image_url': 'http://i.ytimg.com/vi/HggbvHbIvlY/hqdefault.jpg',  # OK
        'view_count': 13306027,
        'date': '2014/08/07'
      },
      '17': {
        'image_url': 'http://i.ytimg.com/vi/R708o7d2uUg/hqdefault.jpg',  # OK
        'view_count': 13289503,
        'date': '2013/01/06'
      },
      '18': {
        'image_url': 'http://i.ytimg.com/vi/4DmWPUhZ8lM/hqdefault.jpg',  # OK
        'view_count': 12854020,
        'date': '2014/10/06'
      }
    }

    old_ranking = {
      '1': {
        'image_url': 'http://i.ytimg.com/vi/LE-JN7_rxtE/hqdefault.jpg',  # OK
        'view_count': 42782625,
        'date': '2010/06/17'
      },
      '2': {
        'image_url': 'http://i.ytimg.com/vi/COoKRYk-HWU/hqdefault.jpg',  # OK
        'view_count': 25683642,
        'date': '2012/06/22'
      },
      '3': {
        'image_url': 'http://i.ytimg.com/vi/x5NRmFSTEgU/hqdefault.jpg',  # OK
        'view_count': 33828785,
        'date': '2012/05/09'
      },
      '4': {
        'image_url': 'http://i.ytimg.com/vi/oT4vLQZJHPY/hqdefault.jpg',  # OK
        'view_count': 12572477,
        'date': '2010/11/16'
      },
      '5': {
        'image_url': 'http://i.ytimg.com/vi/oGaLDnvvZyE/hqdefault.jpg',  # OK
        'view_count': 10901539,
        'date': '2010/08/05'
      }
    }

    return render_template('sample_be-kan.html', recent_ranking=recent_ranking, old_ranking=old_ranking)


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
