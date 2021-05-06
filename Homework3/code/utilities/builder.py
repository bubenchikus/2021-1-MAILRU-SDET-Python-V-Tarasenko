from dataclasses import dataclass
from random import randint
from random import choice
import json

import faker


fake = faker.Faker()


@dataclass
class Campaign:
    slides_num: int = None
    name: str = None
    banners: list = None


class Builder:

    @staticmethod
    def create_campaign(name=None, link=None, slides_num=None, banners=None, url_ids=None, pic_ids_600=None, pic_ids_256=None):

        if name is None:
            name = fake.lexify(text='????????? ?????????')

        # if link is None:
        #     link = fake.bothify(text='https://' + '????????????????/???????/####')

        if slides_num is None:
            slides_num = randint(3, 6)
            slides_num = 3

        urls = {}
        for i in range(slides_num):
            urls[f"url_slide_{i+1}"] = {"id": choice(url_ids)}
            if i == slides_num - 1:
                urls[f"header_click"] = {"id": choice(url_ids)}

        textblocks = {}
        for i in range(slides_num):
            title = fake.lexify(text="?").upper() + fake.lexify(text="??????????????")
            textblocks[f"title_25_slide_{i+1}"] = {"text": title}
            text = fake.lexify(text="?").upper() + fake.lexify(text="??????????????")
            textblocks[f"text_32_slide_{i+1}"] = {"text": text}
            if i == slides_num - 1:
                textblocks["title_25"] = {"text": title}
                textblocks["text_50"] = {"text": text}
                textblocks["cta_sites_full"] = {"text": "visitSite"}

        content = {}
        for i in range(slides_num):
            content[f"image_600x600_slide_{i+1}"] = {"id": choice(pic_ids_600)}
            if i == slides_num - 1:
                content[f"icon_256x256"] = {"id": choice(pic_ids_256)}

        banners = [{"urls": urls, "textblocks": textblocks, "content": content, "name": ''}]

        return Campaign(name=name, banners=banners)
