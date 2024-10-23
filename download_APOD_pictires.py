
import os
import requests
from download_images import download_image
def APOD():
    count = 31 
    params = {
        'count': count
    }

    respons = requests.get("https://api.nasa.gov/planetary/apod?api_key=ERJ8OA57KXWdqN5VMyOQoTa168Rpg2IO52tEHSRb", params=params)
    nasa_images_json = respons.json()

    for idx, image_json in enumerate(nasa_images_json):
        if image_json['url']:
            download_image(image_json['url'], f"NASA_{idx + 1}.jpg","images")
if __name__ == '__main__':
    APOD()