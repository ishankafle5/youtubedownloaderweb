from django.http import FileResponse
import os
from django.shortcuts import render, redirect
from pytube import YouTube
from django.conf import settings
# from  import settings
# Create your views here.


def indexpage(request):
    return render(request, 'index.html')


# def get_default_browser_path():
#     app_data = os.getenv('LOCALAPPDATA')
#     browser_path = os.path.join(
#         app_data)

#     path = str(browser_path)
#     path = path.split('\\')
#     del path[-2:]

#     path.append('')
#     print(path)
#     # print(path)
#     # for i in range(len(path)):

#     #     newpath = path.remove()

#     # print(newpath)
#     return browser_path


def download_video(request):
    # Your existing code to fetch the video file
    pass


def downloaderfunc(request):
    link = request.POST.get('link')
    print(link)
    try:
        pass
    except:
        print("eer")
    index(request, link)

    # return redirect('http://192.168.1.72:5000/')


def downloader(request, link):

    link = "https://youtu.be/iuFo6Qg-P-4?list=RDiuFo6Qg-P-4"

    # print(youtube_1.title)
    loop = False
    while loop == False:
        try:
            youtube_1 = YouTube(link, use_oauth=True, allow_oauth_cache=False)
            loop = True

        except:
            loop = False

    a = str(youtube_1.title)
    try:
        videos = youtube_1.streams.filter(only_audio=True)

        vid = list(enumerate(videos))
        for i in vid:
            print(i)
        strm = int(input("E n t e r ::    "))

        videos[strm].download().title
        print('Successfully ')

    except:
        print("error")

    return


def index(request, link):
    print("This is index")
    # try:
    link = request.POST['link']
    video = YouTube(link)

    stream = video.streams.get_highest_resolution()

    stream.download()

    file_path = os.path.join(settings.MEDIA_ROOT, video.title + '.mp4')

    return FileResponse(file_path, content_type='video/mp4')

    video_file = 'ik.mp4'  # Get the video file

    # Open the file in binary mode
    # with open('ik.mp4', 'rb') as f:
    #     response = FileResponse(f)
    #     response['Content-Disposition'] = 'attachment; filename="video.mp4"'

    # return response

    return render(request, 'index.html', {'msg': 'Video downloaded'})
    # except:

    return render(request, 'index.html', {'msg': 'Video not downloaded'})

    # return render(request, 'index.html', {'msg':''})


# default_path = get_default_browser_path()
# print("Default browser path:", default_path)
