from googleapiclient.discovery import build
from dotenv import load_dotenv 
from bs4 import BeautifulSoup
import requests
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


def findYTtrailerbs4(query):
    query = query.split(" ")
    query = '+'.join(query)
    search_url = f"https://www.youtube.com/results?search_query={query}"

    # Send an HTTP GET request to YouTube
    response = requests.get(search_url)

    if response.status_code == 200:
        # Parse the HTML response
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Convert the soup into a string
        soup = str(soup)
        
        # Find the index where 'href="/watch?v=' is present in the soup_str
        index = soup.find('watch?v=')
        video_url = "https://www.youtube.com"+soup[index-1:soup.find('\\',index+10)]
        return video_url