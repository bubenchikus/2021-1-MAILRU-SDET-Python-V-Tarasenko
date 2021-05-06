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


@dataclass
class Segment:
    name: str = None


class Builder:

    @staticmethod
    def create_campaign(name=None, slides_num=None, slides_urls=None, banners=None, ids_600=None, id_256=None):

        if name is None:
            name = fake.lexify(text='????????? ?????????')

        if slides_num is None:
            slides_num = len(slides_urls) - 1

        urls = {}
        for i in range(slides_num):
            urls[f"url_slide_{i+1}"] = {"id": slides_urls[i]}
            if i == slides_num - 1:
                urls[f"header_click"] = {"id": slides_urls[-1]}

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
            content[f"image_600x600_slide_{i+1}"] = {"id": choice(ids_600)}
            if i == slides_num - 1:
                content[f"icon_256x256"] = {"id": id_256}

        banners = [{"urls": urls, "textblocks": textblocks, "content": content, "name": ''}]

        print('BANNERS', banners)

        return Campaign(name=name, banners=banners)

    @staticmethod
    def generate_url():
        return 'https://' + fake.bothify(text='??????????????????.com/#####').lower()

    @staticmethod
    def create_segment(name=None):
        if name is None:
            name = fake.lexify(text='????????? ?????????')
        return Segment(name=name)
