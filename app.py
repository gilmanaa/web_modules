from bottle import route, run, template, static_file, request, response, redirect
import os
import json
import feedparser

feed_jpost = feedparser.parse("https://www.jpost.com/Rss/RssFeedsHeadlines.aspx")
feed_wsj = feedparser.parse("http://online.wsj.com/xml/rss/3_7011.xml ")

jpost_stories = feed_jpost["entries"]

@route('/feed')
def news_stories():
    return json.dumps(jpost_stories)

@route('/')
def index():
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