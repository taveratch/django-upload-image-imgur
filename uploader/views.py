# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests

from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        url = "https://api.imgur.com/3/image"
        files = { "image": myfile }
        body = { "album": "tC0ylGd" }
        headers = { "Authorization": "Bearer 170f2bf675de202ccb0b26bc25311d0f41a1d84e"}
        r = requests.post(url, files=files, headers=headers, data=body)
        if(r.status_code == requests.codes.ok):
            uploader_url = r.json()["data"]["link"]
            return render(request, 'uploader/index.html', { 'uploaded_file_url': uploader_url})
    return render(request, 'uploader/index.html')