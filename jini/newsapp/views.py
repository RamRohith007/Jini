from django.shortcuts import render
import requests
import json
# Create your views here.

def home(request):
    country = request.POST.get('country',default='in')
    topic = request.POST.get('category',default='general')
    response = requests.get(f'https://newsapi.org/v2/top-headlines?country={country}&category={topic}&apiKey=228e489913a4481f8791d919d7908f1e')
    json_data = json.loads(response.text)
    articles = json_data['articles']
    news_data = []
    for article in articles:
        news_data.append({
            'title': article.get('title', ''),
            'description': article.get('description', ''),
            'url': article.get('url', ''),
            'urlToImage': article.get('urlToImage', ''),
            'publishedAt': article.get('publishedAt', '')
        })
    context = {'news_data': news_data,'current_country': country,'current_category': topic,}
    return render(request, 'newsapp/home.html', context)



    # for i in range(len(allarticles)):
    #     article = allarticles[i]
    #     print(f"{i+1}.◇ {article['title']}\n\n{article['description']}\n\nAuthor: {article['author']}\nPublished at: {allarticles[1]['publishedAt']}\nSource: {allarticles[1]['source']['name']}\nSource link: {allarticles[1]['url']}\n")

