import sys
import random
from pixivpy3 import ByPassSniApi
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .env file


sys.dont_write_bytecode = True

_REFRESH_TOKEN = os.getenv('PIXIV_REFRESH_TOKEN')

def mainFunct(tags):
    api = ByPassSniApi()
    api.require_appapi_hosts()
    api.set_additional_headers({
        'User-Agent': 'PixivAndroidApp/5.0.64 (Android 6.0)',
        'Accept-Language': 'en-US'
    })

    api.auth(refresh_token=_REFRESH_TOKEN)
    json_result = api.search_illust(tags, search_target='partial_match_for_tags')

    if not json_result.illusts:
        return None

    illust = random.choice(json_result.illusts)
    image_url = illust.image_urls.large
    image_id = illust.id
    title = illust.title

    # Tải ảnh về nếu chưa có
    file_path = f'img/{image_id}_p0_master1200.jpg'
    
    api.download(image_url, path='img/',name = f'{image_id}_p0_master1200.jpg ')

    return {
        'id': image_id,
        'title': title,
        'file_path': file_path
    }