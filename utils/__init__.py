import glob

import configparser
import tempfile

import pandas as pd
import sqlalchemy
import time
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
from pathlib import Path


def read_config_sections(config_ini_file: str) -> dict:
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


def get_connection_engine(config_ini_file: str):
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


def list_files(dir_path: str) -> list:
    """
    list csv files from the directory
    :param dir_path: path to csv files
    :return: list of csv files
    """
    print('Reading files from path: {}'.format(dir_path))
    csv_files = [file for file in glob.glob(dir_path + "/*.csv")]

    return csv_files


def load_csv_files_into_df(csv_files: list) -> pd.DataFrame:
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


def download_zip_file(zip_url: str):
    """
    download zip url and extract into target directory
    :param zip_url:
    :param target_dir:
    :return: Location where zip file extracted
    """
    print('downloading file: {}'.format(zip_url))
    # make directory if not exists
    download_dir = tempfile.gettempdir() + '/nyc_bike_data'
    Path(download_dir).mkdir(parents=True, exist_ok=True)
    # print('downloading files under: {}'.format(download_dir))
    with urlopen(zip_url) as zipped:
        with ZipFile(BytesIO(zipped.read())) as zipfile:
            zipfile.extractall(download_dir)
            return download_dir
