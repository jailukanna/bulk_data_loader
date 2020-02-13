# Load NYC Citi Bike Trip csv data files into MySQL Server Using Python

This project loads large dataset onto database (MySQL) efficiently using Pandas in batch mode

The data is taken from NYC public data source 

https://www.citibikenyc.com/system-data
https://s3.amazonaws.com/capitalbikeshare-data/index.html


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 3.7.0 or higher, I have not tested in previous version of python
Dependency lib's are added into requirement.txt, run dependency.txt to install required python packages.



### Installing and running

A step by step series of examples that tell you how to get a development env running

Install dependency packages 

```
cd ./bulk_data_loader
pip install -r requirements.txt

update database connection details in ./bulk_data_loader/config/db.ini

[MySQL]
username: test
password: password_here
host: 127.0.0.1:3306
schema_name: test
#echo_sql: True
mysql_connector_use_pure: True



Create Table Script:

CREATE TABLE `nyc_bike_share` (
  `ID` int NOT NULL,
  `Bike_number` varchar(45) DEFAULT NULL,
  `Member_type` varchar(45) DEFAULT NULL,
  `Start_date` datetime DEFAULT NULL,
  `End_date` datetime DEFAULT NULL,
  `Start_station_number` int DEFAULT NULL,
  `Start_station` varchar(500) DEFAULT NULL,
  `End_station_number` int DEFAULT NULL,
  `End_station` varchar(500) DEFAULT NULL,
  `Duration` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) COMMENT='NYC bike share data';



```
### Running

```
run python script ./bulk_data_loader/data_loader/nyc_bike_share.py directory_path_where_csv_files_located config_ini_file

ex:
python E:/python/bulk_data_loader/data_loader/nyc_bike_share.py E:/python/data/capitalbikeshare-tripdata E:/python/bulk_data_loader/config/db.ini


```

## Author

* **Deepa Aswathaiah**



## Program out

```

python ./data_loader/nyc_bike_share.py E:/python/data/capitalbikeshare-tripdata E:/python/bulk_data_loader/config/db.ini
['E:/python/bulk_data_loader/data_loader/nyc_bike_share.py', 'E:/python/data/capitalbikeshare-tripdata', 'E:/python/bulk_data_loader/config/db.ini']
Reading files from path: E:/python/data/capitalbikeshare-tripdata
['E:/python/data/capitalbikeshare-tripdata\\2016Q1-capitalbikeshare-tripdata.csv', 'E:/python/data/capitalbikeshare-tripdata\\2016Q2-capitalbikeshare-tripdata.csv', 'E:/python/data/capitalbikeshare-tripdata\\20
16Q3-capitalbikeshare-tripdata.csv', 'E:/python/data/capitalbikeshare-tripdata\\2016Q4-capitalbikeshare-tripdata.csv', 'E:/python/data/capitalbikeshare-tripdata\\2017Q1-capitalbikeshare-tripdata.csv', 'E:/pytho
n/data/capitalbikeshare-tripdata\\2017Q2-capitalbikeshare-tripdata.csv', 'E:/python/data/capitalbikeshare-tripdata\\2017Q3-capitalbikeshare-tripdata.csv', 'E:/python/data/capitalbikeshare-tripdata\\2017Q4-capit
albikeshare-tripdata.csv', 'E:/python/data/capitalbikeshare-tripdata\\202001-capitalbikeshare-tripdata.csv']
loading files into dataframe
loading file into dataframe: E:/python/data/capitalbikeshare-tripdata\2016Q1-capitalbikeshare-tripdata.csv
loading file into dataframe: E:/python/data/capitalbikeshare-tripdata\2016Q2-capitalbikeshare-tripdata.csv
loading file into dataframe: E:/python/data/capitalbikeshare-tripdata\2016Q3-capitalbikeshare-tripdata.csv
loading file into dataframe: E:/python/data/capitalbikeshare-tripdata\2016Q4-capitalbikeshare-tripdata.csv
loading file into dataframe: E:/python/data/capitalbikeshare-tripdata\2017Q1-capitalbikeshare-tripdata.csv
loading file into dataframe: E:/python/data/capitalbikeshare-tripdata\2017Q2-capitalbikeshare-tripdata.csv
loading file into dataframe: E:/python/data/capitalbikeshare-tripdata\2017Q3-capitalbikeshare-tripdata.csv
loading file into dataframe: E:/python/data/capitalbikeshare-tripdata\2017Q4-capitalbikeshare-tripdata.csv
loading file into dataframe: E:/python/data/capitalbikeshare-tripdata\202001-capitalbikeshare-tripdata.csv
csv files data read into dataframe elapsed time (sec): 30.953125
inserting dataframe into database table
   Duration           Start date             End date  Start station number                     Start station  End station number                  End station Bike number Member type
0       166  2016-01-01 00:06:58  2016-01-01 00:09:44                 31102               11th & Kenyon St NW               31105         14th & Harvard St NW      W01346      Member
1       448  2016-01-01 00:10:20  2016-01-01 00:17:48                 32039  Old Georgetown Rd & Southwick St               32002  Bethesda Ave & Arlington Rd      W22202      Member
2       715  2016-01-01 00:13:52  2016-01-01 00:25:48                 31222         New York Ave & 15th St NW               31214        17th & Corcoran St NW      W21427      Member
3       213  2016-01-01 00:15:29  2016-01-01 00:19:03                 31506         1st & Rhode Island Ave NW               31509     New Jersey Ave & R St NW      W01294      Member
4       872  2016-01-01 00:16:16  2016-01-01 00:30:49                 31041              Prince St & Union St               31048          King St Metro South      W22058      Member
Duration                7288740
Start date              7288740
End date                7288740
Start station number    7288740
Start station           7288740
End station number      7288740
End station             7288740
Bike number             7288740
Member type             7288740
dtype: int64
(7288740, 9)
reading config file from: E:/python/bulk_data_loader/config/db.ini
connection_info: Engine(mysql+mysqlconnector://test:***@127.0.0.1:3306/test?use_pure=True)
data inserted into database
Database insert elapsed time (sec): 700.015625

 
```
