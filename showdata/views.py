from django.shortcuts import render
import requests
import bs4
def home(request):
    return render(request,'home.html',{})

def iascurrentaffair(request):
    k = requests.get("https://iasbaba.com/current-affairs-for-ias-upsc-exams/")
    source = bs4.BeautifulSoup(k.content, "lxml")
    li=[]
    for i in source.find_all('p'):
        a_tag = i.find('a', attrs={"target": "_blank"})
        try:
            if 'daily-current-affairs' in str(a_tag['href']):
                sho=[]
                sho.append(a_tag['href'])
                sho.append(a_tag.string)
                li.append(sho)
        except:
            pass
    return render(request,'iasaffair.html',{"all":li,"title":"IASbabaCurrentAffair"})

def insightcurrentaffair(request):
    k = requests.get("http://www.insightsonindia.com/current-affairs/")
    source = bs4.BeautifulSoup(k.content, "lxml")
    links = source.find('div', attrs={"class": "themeform"})
    li=[]
    for i in links.find_all('li'):
        try:
            link = i.find('a')
            sho = []
            sho.append(link.attrs['href'])
            sho.append(link.string)
            li.append(sho)
        except:
            pass
    return render(request, 'iasaffair.html', {"all":li,"title":"InsighCurrentAffair"})

def topperstrategy(request):
    k = requests.get("http://www.insightsonindia.com/")
    source = bs4.BeautifulSoup(k.content, "lxml")
    all_post = source.find_all('div', attrs={"id": "alxposts-12"})
    li=[]
    for i in all_post:
        for j in i.find_all('a'):
            try:
                sho = []
                sho.append(j['href'])
                sho.append(j['title'])
                li.append(sho)
            except:
                pass
    return render(request, 'iasaffair.html', {"all":li})

def insigthquiz(request):
    k = requests.get("http://www.insightsonindia.com/insights-current-affairs-questions-2016/")
    source = bs4.BeautifulSoup(k.content, "lxml")
    li=[]
    for i in source.find_all('li'):
        sho=[]
        link=i.find('a')
        try:
            if "insights-current-affairs" in str(link.attrs.get('href')) or "insights-static-quiz" in str(link.attrs.get('href')):
                if not "#comment" in str(link.attrs.get('href')):
                    sho.append(link.attrs.get('href'))
                    print(link.text)
                    sho.append(link.text)
                    li.append(sho)
        except:
            pass
    return render(request, 'iasaffair.html', {"all":li})

def iasquiz(request):
    k = requests.get("https://iasbaba.com/daily-current-affairs-quiz/")
    source = bs4.BeautifulSoup(k.content, "lxml")
    li=[]
    for i in source.find_all('td'):
        try:
            link=i.find('a')
            sho = []
            sho.append(link.attrs.get('href'))
            try:
                sho.append(link.attrs.get('title'))
            except:
                sho.append(link.text)
            li.append(sho)
        except:
            pass

    return render(request,'iasaffair.html',{"all":li[::-1]})