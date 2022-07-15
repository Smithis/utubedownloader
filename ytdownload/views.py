from django.shortcuts import render
from django.http import request
from pytube import YouTube
import re

# Create your views here.
def index(request):
    url = request.GET.get('yturl')
    value = request.GET.get('tag')
    if value is not None:
        print(value)
    pattern = "(http(s|):\/\/|)(www.|)youtube.(com|nl)\/watch\?v\=([a-zA-Z0-9-_=]+)"
        
    if url is not None:       
        if (re.search(pattern, url)):
            urll = YouTube(url)
            image = urll.thumbnail_url
            st = urll.streams.all()
            stt = urll.streams.filter(type='audio',mime_type="audio/mp4")
            
            stream = []

            for i in st:
                stream.append(i.resolution)
            
            stream = list(dict.fromkeys(stream)) 
            print(stream, 2)
            send = {'url':url, 'img':image,'lis':stream, 'son':stt}
             
            return render(request, 'index.html', send)
        else:
            print('exit',0)    
    else:
        print('exit')
    
    return render(request, 'index.html')

def download(request):  
    jack = request.GET.get('tag')
    ab = request.GET.get('abr')
    url= request.GET.get('url')
    def onpro():
        print('dsndskkd')
    def com():
        print('exit')
    
    print(ab, jack)

    def onpro():
        print('resolutin')
    
    def com():
        print('auio')

    if ab is None:
        u = YouTube(url, on_progress_callback=onpro())
        u.streams.filter(res=jack).first().download()

    if jack is None:
        ur = YouTube(url, on_progress_callback=com())
        ur.streams.filter(abr=ab).first().download()




    return render(request, 'download.html')
