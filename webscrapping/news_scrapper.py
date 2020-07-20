from newscatcher import Newscatcher
from newscatcher import describe_url
from newscatcher import urls
import pandas as pd
#Used for getting available urls related to a topic
#science_urls = urls(topic='science',language='en')

#scrapping news articles
nc = Newscatcher(website='science20.com',topic='science')
results = nc.get_news()
articles = results['articles']

#Storing Information in a dictionary
data  = {}
data['title'] = []
data['summary'] = []
data['date_published'] = []
data['link'] = []
for article in articles:
    data['title'].append(article['title'])
    data['summary'].append(article['summary'])
    data['date_published'].append(article['published'])
    data['link'].append(article['id'])

df = pd.DataFrame(data = data)
df.to_csv('news_scrapped.csv',index=False)