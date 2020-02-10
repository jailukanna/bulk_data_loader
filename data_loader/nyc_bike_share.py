# -*- coding: utf-8 -*-
import glob
import sys

import pandas as pd
import sqlalchemy
import configparser
import time

"""
    This class reads csv files and insert into database using pandas dataframe
"""


def read_config_sections(config_ini_file: str):
    """
    read configuration ini file sections
    :param config_ini_file: config file path
    :return: sections as dictionary
    """
    print('reading config file from: {}'.format(config_ini_file))
    config = configparser.ConfigParser()
    config.read(config_ini_file)
    section_dict = {section: {item[0]: item[1] for item in config.items(section)} for section in config.sections()}
    # print(section_dict)
    return section_dict


def _list_files(dir_path) -> list:
    """
    list csv files from the directory
    :param dir_path: path to csv files
    :return: list of csv files
    """
    print('Reading files from path: {}'.format(dir_path))
    csv_files = [file for file in glob.glob(dir_path + "/*.csv")]

    return csv_files


def _load_csv_files(csv_files: list) -> pd.DataFrame:
    """
    load csv files into dataframe
    :param csv_files:  list of csv file path
    :return: data frame
    """
    start_time = time.process_time()
    print('loading files into dataframe')
    df = pd.DataFrame()
    for file in csv_files:
        print('loading file into dataframe: {}'.format(file))
        csv_data = pd.read_csv(file)
        # print(csv_data.head().to_string())
        # print(csv_data.count())
        df = df.append(csv_data, ignore_index=True, sort=False)

    elapsed_time = time.process_time() - start_time
    print('csv files data read into dataframe elapsed time (sec): {}'.format(elapsed_time))

    return df


def _get_connection_engine(config_ini_file: str):
    """
    get mysql connection information from ini file
    :param config_ini_file:
    :return: sqlalchemy connection engine
    """
    ini_section_dict = read_config_sections(config_ini_file)
    db_config = ini_section_dict.get('MySQL')
    database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}?use_pure={4}'.
                                                   format(db_config.get('username'), db_config.get('password'),
                                                          db_config.get('host'), db_config.get('schema_name'),
                                                          db_config.get('mysql_connector_use_pure')),
                                                   echo=bool(db_config.get('echo_sql', False)), )
    return database_connection


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
    connection_info = _get_connection_engine(config_ini_file)
    print('connection_info: {}'.format(connection_info))
    df = df[0:10000]
    df.to_sql(con=connection_info, name='nyc_bike_sharenyc_bike_share', if_exists='append', method='multi',
              chunksize=10000)

    elapsed_time = time.process_time() - start_time
    print('data inserted into database')
    print('Database insert elapsed time (sec): {}'.format(elapsed_time))


def main(dir_path_name: str, config_ini_file: str):
    """
    main program to invoke local functions
    :param dir_path_name:
    :param config_ini_file:
    :return: None
    """
    csv_files = _list_files(dir_path_name)
    print(csv_files)
    df = _load_csv_files(csv_files)
    _insert_into_db(df, config_ini_file)


if __name__ == '__main__':
    input_args = sys.argv
    print(input_args)
    if len(input_args) < 3:
        print(
            "program argumensts missing. usage: python E:/python/bulk_data_loader/data_loader/nyc_bike_share.py E:/python/data/capitalbikeshare-tripdata E:/python/bulk_data_loader/config/db.ini")
    # path = 'E:/python/data/capitalbikeshare-tripdata'
    # config_ini_file = 'E:/python/bulk_data_loader/config/db.ini'
    main(dir_path_name=input_args[1], config_ini_file=input_args[2])
