from bottle import route, run, template, static_file, request, response, redirect
import os
import json
import feedparser
import datetime

feed_jpost = feedparser.parse("https://www.jpost.com/Rss/RssFeedsHeadlines.aspx")
feed_geek = feedparser.parse("https://feeds.howtogeek.com/HowToGeek")
feed_nba = feedparser.parse("https://www.espn.com/espn/rss/nba/news")

jpost_stories = feed_jpost["entries"]
geek_stories = feed_geek["entries"]
nba_stories = feed_nba["entries"]

@route('/nba')
def nba():
    return json.dumps(nba_stories)

@route('/geek')
def geek():
    return json.dumps(geek_stories)

@route('/jpost')
def jpost():
    return json.dumps(jpost_stories)

@route('/')
def index():
    response.set_cookie("update",str(datetime.datetime.now()))
    return template(os.path.dirname(__file__) + "/index.html")

@route('/<filename:re:.*\.css>')
def styles(filename):
    return static_file(filename, root="")

@route('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root="")

@route('/<filename:re:.*\.(jpg|jpeg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root="")

def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()