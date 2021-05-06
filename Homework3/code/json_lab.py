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


def configure_and_return_campaign_json(url_ids, pic_ids_600, pic_ids_256):
    path = form_path('campaign.json')
    data = extract_json(path)

    campaign = Builder.create_campaign(url_ids=url_ids, pic_ids_600=pic_ids_600, pic_ids_256=pic_ids_256)
    data['name'] = campaign.name
    data['banners'] = campaign.banners

    return json.dumps(data)


def configure_and_return_segment_json():
    path = form_path('segment.json')
    data = extract_json(path)
    return json.dumps(data)
