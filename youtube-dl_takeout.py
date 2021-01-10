#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys, youtube_dl, csv

YOUTUBE_DL_DIR = sys.path[0]+'/'

def download_video(videoId):
    yvideo = ['https://www.youtube.com/watch?v='+videoId]
    ydl_opts = {'outtmpl': YOUTUBE_DL_DIR+'%(id)s %(title)s'}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(yvideo)


if __name__ == "__main__":
    with open('Liked videos.csv', newline='') as csvfile:
        takeoutreader = csv.reader(csvfile, delimiter=',')
        for i in range(5):
            next(takeoutreader)
        for row in takeoutreader:
            yt_id = row[0]
            download_video(yt_id)


# In[ ]:




