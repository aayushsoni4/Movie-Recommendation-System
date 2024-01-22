from googleapiclient.discovery import build
from dotenv import load_dotenv 
import os

load_dotenv()
YT_API = os.environ['YT_API']
youtube = build('youtube', 'v3', developerKey=YT_API)

def findYTtrailer(movie_title):
    search_query = movie_title

    request = youtube.search().list(
        part="snippet",
        q=search_query,
        type="video",
        order="relevance",
        videoCategoryId="1"
    )

    response = request.execute()

    item = response['items'][0]
    video_id = item['id']['videoId']
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    return video_url