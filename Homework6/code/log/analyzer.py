from os import path
import pandas as pd
from urllib.parse import unquote


REQUEST_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

base_dir = path.abspath(path.join(__file__, ".."))
file_path = path.join(base_dir, 'access.log')

log_data = open(file_path, 'r')

df_list = []

for line in log_data:

    for c in '[', ']', '"':
        line1 = line.replace(c, '')
    columns = line1.split(' ')

    ip = columns[0]
    date = columns[3]
    method = columns[5]
    url = unquote(columns[6])
    version = columns[7]
    status = columns[8]
    size = columns[9]
    usr = ' '.join(line.split(' ')[11:]).replace('\n', '')

    df_list.append([ip, date, method, url, version, status, size, usr])

log = pd.DataFrame(df_list, columns=['ip', 'date', 'method', 'url', 'version', 'status', 'size', 'usr'])


def number_of_all_requests(df):
    return len(df)


def number_of_requests_by_type(df):
    new_df = df['method'].unique()
    count_list = {'invalid_method': 0}
    for i in new_df:
        if i in REQUEST_METHODS:
            count_list[i] = df['method'].value_counts()[i]
        else:
            count_list['invalid_method'] += 1
    return count_list


def top_10_of_most_frequent_requests(df):
    new_df = df[['url']].copy()
    return new_df['url'].value_counts()[:10].to_dict()


def top_5_of_biggest_requests_with_4xx_status(df):
    new_df = df[['url', 'status', 'size', 'ip']].copy()
    new_df = new_df[new_df['status'].isin([str(i).zfill(2) for i in range(400, 499)])].sort_values('size', ascending=0)
    return new_df.head(5).values.tolist()


def top_5_of_users_by_quantity_with_5xx_status(df):
    new_df = df[['status', 'ip']].copy()
    return new_df[new_df['status'].isin([str(i).zfill(2) for i in range(500, 599)])].value_counts()[:5].to_dict()


number_of_all_requests_result = number_of_all_requests(log)

number_of_requests_by_type_result = number_of_requests_by_type(log)

top_10_of_most_frequent_requests_result = top_10_of_most_frequent_requests(log)

top_5_of_biggest_requests_with_4xx_status_result = top_5_of_biggest_requests_with_4xx_status(log)

top_5_of_users_by_quantity_with_5xx_status_result = top_5_of_users_by_quantity_with_5xx_status(log)
