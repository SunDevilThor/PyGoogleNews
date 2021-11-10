# PyGoogleNews 
# https://github.com/kotartemiy/pygooglenews

from pygooglenews import GoogleNews

gn = GoogleNews()

def get_titles(search):
    stories = []
    search = gn.search(search)
    news_item = search['entries']

    for item in news_item:
        story = {
        'title': item.title,
        'link': item.link
        }

        stories.append(story)

    return stories


print(get_titles('webscraping'))


"""
top = gn.top_news()
business = gn.topic_headlines('business')
location = gn.geo_headlines('Santa Clarita')
"""

#print(search.keys())

# NOTES: 
# Dependencies: 
# pip3 install -U --no-deps "feedparser>=6.0.8"
# pip3 install -U --no-deps "dateparser>=1.0.0"
# pip3 install sgmllib3k
