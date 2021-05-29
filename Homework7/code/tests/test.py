from client import Client
from mock.flask_mock import USER_DATA
from utils.builder import generate_human_data, return_human_data_without_name


class TestClientToMock(Client):

    def test_add(self):

        human = generate_human_data()

        resp = self.post_request(human)
        assert '201 CREATED' in resp[0]

        assert USER_DATA[human['name']]['surname'] == human['surname']
        assert USER_DATA[human['name']]['age'] == human['age']

    def test_get(self):

        human = generate_human_data()
        USER_DATA[human['name']] = return_human_data_without_name(human)

        resp = self.get_request(human['name'])

        assert '200 OK' in resp[0]

        assert resp[6]['surname'] == human['surname']
        assert resp[6]['age'] == human['age']

    def test_change(self):

        human = generate_human_data()
        USER_DATA[human['name']] = return_human_data_without_name(human)

        new_data = generate_human_data(name=human['name'])
        resp = self.put_request(new_data)

        assert '200 OK' in resp[0]

        assert USER_DATA[human['name']]['surname'] == new_data['surname']
        assert USER_DATA[human['name']]['age'] == new_data['age']

    def test_delete(self):

        human = generate_human_data()
        USER_DATA[human['name']] = return_human_data_without_name(human)

        resp = self.delete_request(human['name'])

        assert '200 OK' in resp[0]

        assert USER_DATA.get(human['name']) is None
