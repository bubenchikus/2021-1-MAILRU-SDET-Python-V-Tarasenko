import pytest

from test_api.base import ApiBase


@pytest.mark.API
class TestApi(ApiBase):

    def test_create_campaign(self, auto_create_campaign):
        camp_id = self.api_client.current_campaign_id
        assert camp_id in self.api_client.get_campaigns_ids()
        self.api_client.delete_campaign()
        assert camp_id not in self.api_client.get_campaigns_ids()

    def test_create_segment(self, auto_create_segment):
        segm_id = self.api_client.current_segment_id
        assert segm_id in self.api_client.get_segments_ids()
        self.api_client.delete_segment()
        assert segm_id not in self.api_client.get_segments_ids()
