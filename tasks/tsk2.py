import requests
import json
# Your API key
api_key = '8de1ea5c-86d9-4212-baef-f31bdfb27918'

# The endpoint of the News API
url = 'http://eventregistry.org/api/v1/article/getArticles'

# The parameters for the request
params={
  "action": "getArticles",
  "keyword": "sport",
  "articlesPage":31,
  "articlesCount": 20,
  "articlesSortBy": "date",
  "articlesSortByAsc": False,
  "articlesArticleBodyLen": -1,
  "resultType": "articles",
  "dataType": [
    "news",
    "pr"
  ],
  "apiKey": "8de1ea5c-86d9-4212-baef-f31bdfb27918",
}

# Make the GET request
response = requests.get(url, params=params)
# print(response.__dict__)
data = response.json()
print(data)
# Check if the request was successful
if response.status_code == 200:
  
  for article in data["articles"]["results"]:
    # Extract the title, datetimepub, and url of each article
    title = article['title']
    datetimepub = article['dateTimePub']
    url = article['url']
    # Print the title, datetimepub, and url of each article
    print(f"'Title':{title} -'datatimepub': {datetimepub} - 'url':{url}")



   
   