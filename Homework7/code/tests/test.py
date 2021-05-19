from client import Client
from mock.flask_mock import USER_DATA


class TestClientToMock(Client):

    def test_add(self):

        name = 'CustomName1'

        resp = self.post_request(name)

        assert USER_DATA.get(name) is not None
        assert '201 CREATED' in resp[0]

    def test_get(self):

        name = 'CustomName2'

        self.post_request(name)
        resp = self.get_request(name)

        assert '200 OK' in resp[0]

    def test_change(self):

        name = 'CustomName3'
        surname = 'CustomSurname'
        age = 55

        self.post_request(name)
        self.put_request(name, surname, age)
        resp = self.get_request(name)

        assert USER_DATA[name]['surname'] == surname and USER_DATA[name]['age'] == age
        assert surname in resp[6] and str(age) in resp[6]

    def test_delete(self):

        name = 'CustomName4'

        self.post_request(name)
        self.delete_request(name)
        resp = self.get_request(name)

        assert USER_DATA.get(name) is None
        assert '404 NOT FOUND' in resp[0]
