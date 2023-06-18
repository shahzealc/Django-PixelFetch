from django.shortcuts import redirect, render
import requests
import json
import urllib.request
import pathlib
import random
import cv2
from pyzbar.pyzbar import decode

# Create your views here.


def homepage(request):
    response = requests.get(
        "https://api.unsplash.com/search/photos?page=1&per_page=30&query=random&client_id=mafc50Q51X-JOJeX2SXR7_RwMPjMBmQcx94QP9vXADY").json()
    response_info = response['results']
    ID = []
    img_link = []
    likes = []
    user = []
    for temp in response_info:
        ID.append(temp['id'])
        img_link.append(temp['urls']['small'])
        likes.append(temp['likes'])
        user.append(temp['user']['username'])
        temp_list = [ID, img_link, likes, user]
    random_wallpaper_data = zip(ID, img_link, likes, user)

    response = requests.get(
        "https://api.unsplash.com/search/photos?page=2&per_page=30&query=random&client_id=mafc50Q51X-JOJeX2SXR7_RwMPjMBmQcx94QP9vXADY").json()
    response_info = response['results']
    ID = []
    img_link = []
    likes = []
    user = []
    for temp in response_info:
        ID.append(temp['id'])
        img_link.append(temp['urls']['small'])
        likes.append(temp['likes'])
        user.append(temp['user']['username'])
        temp_list = [ID, img_link, likes, user]
    random_wallpaper_data1 = zip(ID, img_link, likes, user)

    response = requests.get(
        "https://api.unsplash.com/search/photos?page=3&per_page=30&query=random&client_id=mafc50Q51X-JOJeX2SXR7_RwMPjMBmQcx94QP9vXADY").json()
    response_info = response['results']
    ID = []
    img_link = []
    likes = []
    user = []
    for temp in response_info:
        ID.append(temp['id'])
        img_link.append(temp['urls']['small'])
        likes.append(temp['likes'])
        user.append(temp['user']['username'])
        temp_list = [ID, img_link, likes, user]
    random_wallpaper_data2 = zip(ID, img_link, likes, user)

    return render(request, 'index.html', {'random_wallpaper_data': random_wallpaper_data, 'random_wallpaper_data1': random_wallpaper_data1, 'random_wallpaper_data2': random_wallpaper_data2})

def req_wall(request):
    if request.POST.get('query'):
        query = request.POST.get('query')
    else:
        query = request.GET.get('query')

    url = "https://api.unsplash.com/search/photos?page=1&per_page=30&query={}&client_id=mafc50Q51X-JOJeX2SXR7_RwMPjMBmQcx94QP9vXADY".format(query)
    response = requests.get(url).json()
    response_info = response['results']
    ID = []
    img_link = []
    likes = []
    user = []
    for temp in response_info:
        ID.append(temp['id'])
        img_link.append(temp['urls']['small'])
        likes.append(temp['likes'])
        user.append(temp['user']['username'])
        temp_list = [ID, img_link, likes, user]
    random_wallpaper_data = zip(ID, img_link, likes, user)

    url = "https://api.unsplash.com/search/photos?page=2&per_page=30&query={}&client_id=mafc50Q51X-JOJeX2SXR7_RwMPjMBmQcx94QP9vXADY".format(query)
    response = requests.get(url).json()
    response_info = response['results']
    ID = []
    img_link = []
    likes = []
    user = []
    for temp in response_info:
        ID.append(temp['id'])
        img_link.append(temp['urls']['small'])
        likes.append(temp['likes'])
        user.append(temp['user']['username'])
        temp_list = [ID, img_link, likes, user]
    random_wallpaper_data1 = zip(ID, img_link, likes, user)

    url = "https://api.unsplash.com/search/photos?page=3&per_page=30&query={}&client_id=mafc50Q51X-JOJeX2SXR7_RwMPjMBmQcx94QP9vXADY".format(query)
    response = requests.get(url).json()
    response_info = response['results']
    ID = []
    img_link = []
    likes = []
    user = []
    for temp in response_info:
        ID.append(temp['id'])
        img_link.append(temp['urls']['small'])
        likes.append(temp['likes'])
        user.append(temp['user']['username'])
        temp_list = [ID, img_link, likes, user]
    random_wallpaper_data2 = zip(ID, img_link, likes, user)

    return render(request, 'request_wallpaper.html', {'random_wallpaper_data': random_wallpaper_data, 'random_wallpaper_data1': random_wallpaper_data1, 'random_wallpaper_data2': random_wallpaper_data2,'query':query.capitalize()})

def about(request):
    return render(request,'about.html')

def detail(request):
    wallpaper_id = request.GET.get('id')
    url = "https://api.unsplash.com/photos/{}?client_id=mafc50Q51X-JOJeX2SXR7_RwMPjMBmQcx94QP9vXADY".format(wallpaper_id)
    response = requests.get(url).json()
    # response_info = response['results']
  
    img_link = response['urls']['full']
    likes = response['likes']
    user = response['user']['username'].capitalize()
    title = response['description']
    description= response['alt_description'].capitalize()
    full = response['urls']['full']
    regular = response['urls']['regular']
    small = response['urls']['small']
    # tags = [tag["title"].capitalize() for tag in response["tags"]]
    
    tags =[]
    count=0
    for tag in response["tags"]:
        if count<7:
            tags.append(tag["title"].capitalize() )
        else:   
            break
        count = count+1

    return render(request,'details.html',{'id':wallpaper_id,'img_link':img_link,'likes':likes,'user':user,'title':title,'description':description,'full':full,'regular':regular,'small':small,'tags':tags})

# download Wallpaper code
def download(request):
    url = request.GET.get('url')
    rand = random.randint(10000,99999)
    urllib.request.urlretrieve(url,pathlib.Path.home() / "Downloads\PixelFetch{0}.jpg".format(rand))
    return redirect(request.META.get('HTTP_REFERER'))


def scan_barcode(request):
    if request.method == 'POST':
        # Initialize the video capture device
        video_capture = cv2.VideoCapture(0)
        barcode_detected = False

        while True:
            # Read a frame from the video capture
            ret, frame = video_capture.read()

            # Convert the frame to grayscale for barcode detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Decode barcodes from the grayscale frame
            decoded_data = decode(gray)

            # Process the decoded barcode data
            if decoded_data:
                barcode_data = decoded_data[0].data.decode('utf-8')
                barcode_detected = True
                # Process the barcode data
                # ...

            # Display the captured frame
            cv2.imshow('Barcode Scanner', frame)

            # Exit the loop when barcode is detected or 'q' is pressed
            if barcode_detected or cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the video capture device and close windows
        print(barcode_data)
        video_capture.release()
        cv2.destroyAllWindows()

    return render(request, 'scan.html')