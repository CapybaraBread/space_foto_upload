import telegram
import random
import os
import time
from dotenv import load_dotenv


load_dotenv()


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
PUBLICATION_DELAY = int(os.getenv("PUBLICATION_DELAY", 14400))
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
IMAGES_FOLDER = "./images"

def send_random_image():
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    

    images = [f for f in os.listdir(IMAGES_FOLDER) if os.path.isfile(os.path.join(IMAGES_FOLDER, f))]
    

    random_image = random.choice(images)
    image_path = os.path.join(IMAGES_FOLDER, random_image)
    

    with open(image_path, 'rb') as image_file:
        bot.send_photo(chat_id=TELEGRAM_CHANNEL_ID, photo=image_file)
        print(f"Изображение '{random_image}' отправлено в канал.")

if __name__ == "__main__":
    while True:
        send_random_image()
        time.sleep(PUBLICATION_DELAY)