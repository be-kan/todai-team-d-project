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

@app.route('/twitter_sample')
def twitter_sample():
    import json
    from requests_oauthlib import OAuth1Session
    twitter = OAuth1Session(API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

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
