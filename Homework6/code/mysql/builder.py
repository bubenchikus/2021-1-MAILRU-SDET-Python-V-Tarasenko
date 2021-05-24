from mysql.models import NumberOfAllRequests, NumberOfRequestsByType, Top10OfMostFrequentRequests, \
    Top5OfBiggestRequestsWith4XXStatus, Top5OfUsersByQuantityWith5XXStatus
from log import analyzer


class MySQLBuilder:

    def __init__(self, client):
        self.client = client

    def create_number_of_all_requests_row(self):

        number_of_all_requests_row = NumberOfAllRequests(
            number_of_all_requests=analyzer.number_of_all_requests_result
        )

        self.client.session.add(number_of_all_requests_row)

        return number_of_all_requests_row

    def create_number_of_all_requests(self):

        self.create_number_of_all_requests_row()

    def create_number_of_requests_by_type_row(self, key):

        number_of_requests_by_type_row = NumberOfRequestsByType(
            request_type=key,
            number=int(analyzer.number_of_requests_by_type_result[key])
        )

        self.client.session.add(number_of_requests_by_type_row)

        return number_of_requests_by_type_row

    def create_number_of_requests_by_type(self):

        for key in list(analyzer.number_of_requests_by_type_result.keys()):
            self.create_number_of_requests_by_type_row(key)

    def create_top_10_of_most_frequent_requests_row(self, key):

        top_10_of_most_frequent_requests_row = Top10OfMostFrequentRequests(
            url=key,
            number=analyzer.top_10_of_most_frequent_requests_result[key]
        )

        self.client.session.add(top_10_of_most_frequent_requests_row)

        return top_10_of_most_frequent_requests_row

    def create_top_10_of_most_frequent_requests(self):

        for key in list(analyzer.top_10_of_most_frequent_requests_result.keys()):
            self.create_top_10_of_most_frequent_requests_row(key)

    def create_top_5_of_biggest_requests_with_4xx_status_row(self, row):

        top_5_of_biggest_requests_with_4xx_status_row = Top5OfBiggestRequestsWith4XXStatus(
            url=row[0],
            status=row[1],
            size=row[2],
            ip=row[3]
        )

        self.client.session.add(top_5_of_biggest_requests_with_4xx_status_row)

        return top_5_of_biggest_requests_with_4xx_status_row

    def create_top_5_of_biggest_requests_with_4xx_status(self):

        for row in analyzer.top_5_of_biggest_requests_with_4xx_status_result:
            self.create_top_5_of_biggest_requests_with_4xx_status_row(row)

    def create_top_5_of_users_by_quantity_with_5xx_status_row(self, key):

        top_5_of_users_by_quantity_with_5xx_status = Top5OfUsersByQuantityWith5XXStatus(
            ip=key[1],
            quantity=analyzer.top_5_of_users_by_quantity_with_5xx_status_result[key]
        )
        self.client.session.add(top_5_of_users_by_quantity_with_5xx_status)

        return top_5_of_users_by_quantity_with_5xx_status

    def create_top_5_of_users_by_quantity_with_5xx_status(self):

        for key in list(analyzer.top_5_of_users_by_quantity_with_5xx_status_result.keys()):
            self.create_top_5_of_users_by_quantity_with_5xx_status_row(key)

    def create_all_tables(self):

        self.create_number_of_all_requests()
        self.create_number_of_requests_by_type()
        self.create_top_10_of_most_frequent_requests()
        self.create_top_5_of_biggest_requests_with_4xx_status()
        self.create_top_5_of_users_by_quantity_with_5xx_status()

        self.client.session.commit()
