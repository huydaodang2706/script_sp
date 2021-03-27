from __future__ import unicode_literals
import os
import argparse
from youtube_transcript_api import YouTubeTranscriptApi

parser = argparse.ArgumentParser(description="crawlYoutube transcript flags")

parser.add_argument("--vid_id", "-id", type=str, help="Id of video to crawl")
parser.add_argument("--save_dir", "-s", type=str,
                    help="Directory to save crawled files")
parser.add_argument("--sublang", type=str, help="Subtitle language", default="vi")
parser.add_argument("--channel", "-c", type=str, help="Channel to crawl")
parser.add_argument("--vidnum", "-n", type=str, help="number of video to crawl", default="2")

args = parser.parse_args()

if not (args.playlist and args.save_dir and args.sublang and args.vidnum):
    raise ValueError("must specify --playlist and --save_dir")

if (args.playlist and args.channel):
    channel_dwn = True
else:
    channel_dwn = False

# print(args.playlist)
vidnum = int(args.vidnum)
if channel_dwn:
    for x in range(vidnum):
        index = x+1
        url = args.playlist + '&index=' + str(index) + '&ab_channel=' + args.channel
        srt = YouTubeTranscriptApi.get_transcript(url,languages=('vi',))
        filename = 'srt_file' + str(index) + '.txt'
        print(filename) 
        with open(filename,'w') as f:
            for i in srt:
                f.write(str(i))
        # with open('srt_file.txt','w') as f:
        #     for i in srt:
        #         f.write(str(i))
    
else:
    srt = YouTubeTranscriptApi.get_transcript(args.playlist,languages=('vi',))
    with open('srt_file.txt','w') as f:
        for i in srt:
            f.write(str(i))

# srt = YoutubeTranscriptApi.get_transcript('9NQcxue_yIk&ab_channel=YEAH1MUSIC')
# with open('srt_file.txt','w') as f:
#     for i in srt:
#         f.write(str(i))

# print(srt)
# print(srt[1])
# https://www.youtube.com/watch?v=0BKSwSz_NwQ&list=PLy_TpcUT2LZtUt-JOrXCqc8LTVRFz2n6I
# https://www.youtube.com/watch?v=0BKSwSz_NwQ&list=PLy_TpcUT2LZtUt-JOrXCqc8LTVRFz2n6I&ab_channel=%C4%90%C3%94NGT%C3%82YPROMOTIONOFFICIAL
# https://www.youtube.com/watch?v=0BKSwSz_NwQ&list=PLy_TpcUT2LZtUt-JOrXCqc8LTVRFz2n6I

# Can nhap vao id cua video
# B1: Nhap link cua video playlist, link channel

# B2: Nhap vao so luong video can download
# B3: Download transcript cho video

# https://www.youtube.com/watch?v=93xKEzoiL34&list=PLuYYxO0kXGgkDfJWx4Zan_bou-B5swL0Q
# https://www.youtube.com/watch?v=93xKEzoiL34&list=PLuYYxO0kXGgkDfJWx4Zan_bou-B5swL0Q&ab_channel=VETV7ESPORTS
# https://www.youtube.com/watch?v=-uhgZqRme4o&list=PLuYYxO0kXGgkDfJWx4Zan_bou-B5swL0Q&index=2&ab_channel=VETV7ESPORTS