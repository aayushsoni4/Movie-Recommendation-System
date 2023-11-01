import requests
from bs4 import BeautifulSoup

def findYTtrailer(query):
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