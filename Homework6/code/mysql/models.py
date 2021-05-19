from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class NumberOfAllRequests(Base):

    __tablename__ = 'number_of_all_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return '<NumberOfAllRequests(number_of_all_requests=%r)>' % self.number_of_all_requests

    number_of_all_requests = Column(Integer, primary_key=True)


class NumberOfRequestsByType(Base):

    __tablename__ = 'number_of_requests_by_type'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return '<NumberOfRequestsByType(request_type=%r, number=%r)>' % (self.request_type,
                                                                         self.number)

    request_type = Column(String(15), primary_key=True)
    number = Column(Integer)


class Top10OfMostFrequentRequests(Base):

    __tablename__ = 'top_10_of_most_frequent_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return '<Top10OfMostFrequentRequests(url=%r, number=%r)>' % (self.url,
                                                                     self.number)

    url = Column(String(100), primary_key=True)
    number = Column(Integer)


class Top5OfBiggestRequestsWith4XXStatus(Base):

    __tablename__ = 'top_5_of_biggest_requests_with_4xx_status'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return '<Top5OfBiggestRequestsWith4XXStatus(url=%r, status=%r, size=%r, ip=%r)>' % (self.url,
                                                                                            self.status,
                                                                                            self.size,
                                                                                            self.ip)

    url = Column(String(1000), primary_key=True)
    status = Column(Integer)
    size = Column(Integer)
    ip = Column(String(16))


class Top5OfUsersByQuantityWith5XXStatus(Base):

    __tablename__ = 'top_5_of_users_by_quantity_with_5xx_status'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return '<Top5OfUsersByQuantityWith5XXStatus(ip=%r, quantity=%r)>' % (self.ip,
                                                                             self.quantity)

    ip = Column(String(16), primary_key=True)
    quantity = Column(Integer)
