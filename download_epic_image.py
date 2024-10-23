import os
import requests
from download_images import download_image

def get_epic_image_links():
    api_key = "rWjmOn44xvfj4Thyl6md3Zbsm98m0z4QYhOFEs2Z"
    base_url = "https://api.nasa.gov/EPIC/api/natural"
    archive_url = "https://api.nasa.gov/EPIC/archive/natural"
    data = requests.get(f"{base_url}?api_key={api_key}").json()
    epic_url = [f"{archive_url}/{item['date'].split(' ')[0].replace('-', '/')}/png/{item['image']}.png?api_key={api_key}" for item in data]
    for idx, link in enumerate(epic_url):
        download_image(link, f"NASA_EPIC_{idx + 1}.png", "images")

if __name__ == '__main__':
    get_epic_image_links()