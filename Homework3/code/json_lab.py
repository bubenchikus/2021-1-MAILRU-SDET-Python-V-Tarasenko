import os
import json
from utilities.builder import Builder


def form_path(name):
    path = os.path.abspath(__file__)
    path = os.path.join(path, '../..', 'code/', name)
    path = os.path.abspath(path)
    return path


def extract_json(path):
    with open(path, 'r+') as f:
        data = json.load(f)
    return data


def configure_and_return_campaign_json(slides_urls, ids_600, id_256):
    path = form_path('campaign.json')
    data = extract_json(path)

    campaign = Builder.create_campaign(slides_urls=slides_urls, ids_600=ids_600, id_256=id_256)
    data['name'] = campaign.name
    data['banners'] = campaign.banners

    return json.dumps(data)


def generate_url():
    return Builder.generate_url()


def configure_and_return_segment_json():
    path = form_path('segment.json')
    data = extract_json(path)

    segment = Builder.create_segment()
    data['name'] = segment.name

    return json.dumps(data)
