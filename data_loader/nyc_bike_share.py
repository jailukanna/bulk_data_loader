# -*- coding: utf-8 -*-
import sys

import pandas as pd
import time
import tempfile

import requests
import xmltodict

from utils import get_connection_engine, list_files, load_csv_files_into_df, download_zip_file

"""
    This class reads csv files and insert into database using pandas dataframe
"""

NYC_BIKE_SHARE_S3_REPO = 'https://s3.amazonaws.com/capitalbikeshare-data'


def _insert_into_db(df: pd.DataFrame, config_ini_file: str):
    """
    insert data into database from pandas dataframe
    :param df: data
    :param config_ini_file: db connection info file
    :return: None
    """
    start_time = time.process_time()

    print('inserting dataframe into database table')
    print(df.head())
    print(df.count())
    print(df.shape)
    connection_info = get_connection_engine(config_ini_file)
    print('connection_info: {}'.format(connection_info))
    df = df[0:5]

    # db_tab_cols = pd.read_sql(con=connection_info, sql='select * from nyc_bike_share where 1=2').columns.tolist()
    # print('db_tab_cols: {}'.format(db_tab_cols))
    # df.columns = db_tab_cols
    print('dataframe columns: {}'.format(df.columns))

    # rename columns to match with db table column name
    columns_to_rename = {'Duration': 'Duration', 'Start date': 'Start_date', 'End date': 'End_date',
                         'Start station number': 'Start_station_number',
                         'Start station': 'Start_station', 'End station number': 'End_station_number',
                         'End station': 'End_station', 'Bike number': 'Bike_number',
                         'Member type': 'Member_type'}
    df = df.rename(columns=columns_to_rename)

    print('dataframe columns: {}'.format(df.columns))
    df.to_sql(con=connection_info, name='nyc_bike_share', if_exists='append', method='multi',
              index=False, chunksize=1000)

    elapsed_time = time.process_time() - start_time
    print('data inserted into database')
    print('Database insert elapsed time (sec): {}'.format(elapsed_time))


def _parse_s3_xml_result_to_files(xml_content: str) -> list:
    """
    Parse xml to extract zip files. checkout sample s3_result.xml under this project root directory
    :param xml_content: s3 xml result
    :return: list of files
    """
    ordered_dict = xmltodict.parse(xml_content)['ListBucketResult']['Contents']
    # print(ordered_dict)
    result = [items[key] for items in ordered_dict for key in items if key == 'Key' and '.zip' in items[key]]
    print('xml parsed result: {}'.format(result))
    return result


def _get_s3_bucket_files(s3_bucket_url: str) -> list:
    """
    get zip files under s3 bucket
    :param s3_bucket_url:
    :return: list of zip files
    """
    print('Retriving list of bike share files from s3 bucket: {}'.format(NYC_BIKE_SHARE_S3_REPO))
    try:
        response = requests.get(s3_bucket_url)
        response.raise_for_status()
        files = _parse_s3_xml_result_to_files(response.content)
        print('files under s3 bucket:\n{}'.format('\n'.join(files)))
        return files
    except requests.exceptions.HTTPError as err:
        print(err)
        return None


def main(config_ini_file: str):
    """
    main program to invoke local functions
    :param config_ini_file:
    :return: None
    """
    s3_bucket_files = _get_s3_bucket_files(NYC_BIKE_SHARE_S3_REPO)
    if not s3_bucket_files:
        print(' No files in s3 bucket url: {}'.format(NYC_BIKE_SHARE_S3_REPO))

    for file in s3_bucket_files:
        dir_path_name = download_zip_file(NYC_BIKE_SHARE_S3_REPO + '/{}'.format(file))

    csv_files = list_files(dir_path_name)
    print('Following files downloaded:\n{}'.format('\n'.join(csv_files)))
    df = load_csv_files_into_df(csv_files)
    _insert_into_db(df, config_ini_file)


if __name__ == '__main__':
    input_args = sys.argv
    print(input_args)
    if len(input_args) < 2:
        print(
            "program argumensts missing. usage: python E:/python/bulk_data_loader/data_loader/nyc_bike_share.py file_path_to_db.ini")
        sys.exit(1)

    # path = 'https://s3.amazonaws.com/capitalbikeshare-data/2010-capitalbikeshare-tripdata.zip'
    config_ini_file = input_args[1]  # 'E:/python/bulk_data_loader/config/db.ini'
    print(tempfile.gettempdir())
    main(config_ini_file=config_ini_file)
