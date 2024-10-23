
import os
import requests
from download_images import download_image
def fetch_spacex_last_launch():
    image_url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    download_image(image_url, "hubble.jpeg", "images" )

    parems = {"id":"5eb87d47ffd86e000604b38a"}
    respons = requests.get("https://api.spacexdata.com/v5/launches/", params=parems)
    image_links = respons.json()[19]["links"]["flickr"]["original"]

    for idx, image_url in enumerate(image_links):
        download_image(image_url, f"spacex_image_{idx + 1}.jpg", "images" )
if __name__ == '__main__':
    fetch_spacex_last_launch()