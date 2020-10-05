from youtube_api import YouTubeDataAPI
import os

api_key = os.environ['YOUTUBE_API_SECRET_KEY']
yt = YouTubeDataAPI(api_key)

search_results = yt.search('python tutorial videos')

for search_result in search_results:
    print("----------------------------------")
    print(search_result['video_title'])
    print(search_result['video_description'])
    print("https://www.youtube.com/watch?v=" + search_result['video_id'])