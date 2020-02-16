# Load NYC Citi Bike Trip csv data files into MySQL Server Using Python

This project downloads NYC bike share data and loads large dataset (~25.5 million rows) onto database (MySQL) efficiently using Pandas in batch mode

The data is taken from NYC public data source. Multiple csv files are zipped (by year, quarter etc). All files are under S3 bucket https://s3.amazonaws.com/capitalbikeshare-data'

https://www.citibikenyc.com/system-data
https://s3.amazonaws.com/capitalbikeshare-data/index.html

This program connects to public s3 bucket, downloads zip files to system temp directory, extracts and uploaded csv data into MySql database.

Check for sample s3_result.xml under project root directory

download_dir = System Temp Directory + '/nyc_bike_data'

Total records loaded : 25,539,024 (~25.5 million records)

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
  `ID` int AUTO_INCREMENT,
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

set PYTHONPATH=%PYTHONPATH%;E:/python/bulk_data_loader/data_loader;

run python script ./bulk_data_loader/data_loader/nyc_bike_share.py config_ini_file

ex:
python E:/python/bulk_data_loader/data_loader/nyc_bike_share.py E:/python/bulk_data_loader/config/db.ini


```

## Author

* **Deepa Aswathaiah**



## Program out

```

(base) E:\python\bulk_data_loader>python E:/python/bulk_data_loader/data_loader/nyc_bike_share.py E:/python/bulk_data_loader/config/db.ini
['E:/python/bulk_data_loader/data_loader/nyc_bike_share.py', 'E:/python/bulk_data_loader/config/db.ini']
C:\Users\RAMESH~1\AppData\Local\Temp
Retriving list of bike share files from s3 bucket: https://s3.amazonaws.com/capitalbikeshare-data
xml parsed result: ['2010-capitalbikeshare-tripdata.zip', '2011-capitalbikeshare-tripdata.zip', '2012-capitalbikeshare-tripdata.zip', '2013-capitalbikeshare-tripdata.zip', '2014-capitalbikeshare-tripdata.zip',
'2015-capitalbikeshare-tripdata.zip', '2016-capitalbikeshare-tripdata.zip', '2017-capitalbikeshare-tripdata.zip', '201801-capitalbikeshare-tripdata.zip', '201802-capitalbikeshare-tripdata.zip', '201803-capitalb
ikeshare-tripdata.zip', '201804-capitalbikeshare-tripdata.zip', '201805-capitalbikeshare-tripdata.zip', '201806-capitalbikeshare-tripdata.zip', '201807-capitalbikeshare-tripdata.zip', '201808-capitalbikeshare-t
ripdata.zip', '201809-capitalbikeshare-tripdata.zip', '201810-capitalbikeshare-tripdata.zip', '201811-capitalbikeshare-tripdata.zip', '201812-capitalbikeshare-tripdata.zip', '201901-capitalbikeshare-tripdata.zi
p', '201902-capitalbikeshare-tripdata.zip', '201903-capitalbikeshare-tripdata.zip', '201904-capitalbikeshare-tripdata.zip', '201905-capitalbikeshare-tripdata.zip', '201906-capitalbikeshare-tripdata.zip', '20190
7-capitalbikeshare-tripdata.zip', '201908-capitalbikeshare-tripdata.zip', '201909-capitalbikeshare-tripdata.zip', '201910-capitalbikeshare-tripdata.zip', '201911-capitalbikeshare-tripdata.zip', '201912-capitalb
ikeshare-tripdata.zip', '202001-capitalbikeshare-tripdata.zip']
files under s3 bucket:
2010-capitalbikeshare-tripdata.zip
2011-capitalbikeshare-tripdata.zip
2012-capitalbikeshare-tripdata.zip
2013-capitalbikeshare-tripdata.zip
2014-capitalbikeshare-tripdata.zip
2015-capitalbikeshare-tripdata.zip
2016-capitalbikeshare-tripdata.zip
2017-capitalbikeshare-tripdata.zip
201801-capitalbikeshare-tripdata.zip
201802-capitalbikeshare-tripdata.zip
201803-capitalbikeshare-tripdata.zip
201804-capitalbikeshare-tripdata.zip
201805-capitalbikeshare-tripdata.zip
201806-capitalbikeshare-tripdata.zip
201807-capitalbikeshare-tripdata.zip
201808-capitalbikeshare-tripdata.zip
201809-capitalbikeshare-tripdata.zip
201810-capitalbikeshare-tripdata.zip
201811-capitalbikeshare-tripdata.zip
201812-capitalbikeshare-tripdata.zip
201901-capitalbikeshare-tripdata.zip
201902-capitalbikeshare-tripdata.zip
201903-capitalbikeshare-tripdata.zip
201904-capitalbikeshare-tripdata.zip
201905-capitalbikeshare-tripdata.zip
201906-capitalbikeshare-tripdata.zip
201907-capitalbikeshare-tripdata.zip
201908-capitalbikeshare-tripdata.zip
201909-capitalbikeshare-tripdata.zip
201910-capitalbikeshare-tripdata.zip
201911-capitalbikeshare-tripdata.zip
201912-capitalbikeshare-tripdata.zip
202001-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/2010-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/2011-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/2012-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/2013-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/2014-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/2015-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/2016-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/2017-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201801-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201802-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201803-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201804-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201805-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201806-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201807-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201808-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201809-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201810-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201811-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201812-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201901-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201902-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201903-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201904-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201905-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201906-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201907-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201908-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201909-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201910-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201911-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/201912-capitalbikeshare-tripdata.zip
downloading file: https://s3.amazonaws.com/capitalbikeshare-data/202001-capitalbikeshare-tripdata.zip
Reading files from path: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data
Following files downloaded:
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2010-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2011-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2012Q1-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2012Q2-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2012Q3-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2012Q4-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2013Q1-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2013Q2-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2013Q3-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2013Q4-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2014Q1-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2014Q2-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2014Q3-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2014Q4-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2015Q1-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2015Q2-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2015Q3-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2015Q4-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2016Q1-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2016Q2-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2016Q3-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2016Q4-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2017Q1-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2017Q2-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2017Q3-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2017Q4-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201801_capitalbikeshare_tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201802-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201803-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201804-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201805-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201806-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201807-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201808-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201809-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201810-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201811-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201812-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201901-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201902-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201903-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201904-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201905-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201906-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201909-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201910-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201911-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201912-capitalbikeshare-tripdata.csv
C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\202001-capitalbikeshare-tripdata.csv
loading files into dataframe
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2010-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2011-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2012Q1-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2012Q2-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2012Q3-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2012Q4-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2013Q1-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2013Q2-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2013Q3-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2013Q4-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2014Q1-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2014Q2-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2014Q3-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2014Q4-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2015Q1-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2015Q2-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2015Q3-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2015Q4-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2016Q1-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2016Q2-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2016Q3-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2016Q4-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2017Q1-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2017Q2-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2017Q3-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\2017Q4-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201801_capitalbikeshare_tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201802-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201803-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201804-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201805-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201806-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201807-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201808-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201809-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201810-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201811-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201812-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201901-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201902-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201903-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201904-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201905-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201906-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201909-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201910-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201911-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\201912-capitalbikeshare-tripdata.csv
loading file into dataframe: C:\Users\RAMESH~1\AppData\Local\Temp/nyc_bike_data\202001-capitalbikeshare-tripdata.csv
csv files data read into dataframe elapsed time (sec): 412.15625
inserting dataframe into database table
   Duration           Start date             End date  Start station number                  Start station  End station number                    End station Bike number Member type
0      1012  2010-09-20 11:27:04  2010-09-20 11:43:56                 31208       M St & New Jersey Ave SE               31108                  4th & M St SW      W00742      Member
1        61  2010-09-20 11:41:22  2010-09-20 11:42:23                 31209                 1st & N St  SE               31209                 1st & N St  SE      W00032      Member
2      2690  2010-09-20 12:05:37  2010-09-20 12:50:27                 31600                  5th & K St NW               31100  19th St & Pennsylvania Ave NW      W00993      Member
3      1406  2010-09-20 12:06:05  2010-09-20 12:29:32                 31600                  5th & K St NW               31602        Park Rd & Holmead Pl NW      W00344      Member
4      1413  2010-09-20 12:10:43  2010-09-20 12:34:17                 31100  19th St & Pennsylvania Ave NW               31201                 15th & P St NW      W00883      Member
Duration                25539024
Start date              25539024
End date                25539024
Start station number    25539024
Start station           25539024
End station number      25539024
End station             25539024
Bike number             25539010
Member type             25539024
dtype: int64
(25539024, 9)
reading config file from: E:/python/bulk_data_loader/config/db.ini
connection_info: Engine(mysql+mysqlconnector://test:***@127.0.0.1:3306/test?use_pure=True)
dataframe columns: Index(['Duration', 'Start date', 'End date', 'Start station number',
       'Start station', 'End station number', 'End station', 'Bike number',
       'Member type'],
      dtype='object')
dataframe columns: Index(['Duration', 'Start_date', 'End_date', 'Start_station_number',
       'Start_station', 'End_station_number', 'End_station', 'Bike_number',
       'Member_type'],
      dtype='object')
data inserted into database
Database insert elapsed time (sec): 680.734375

(base) E:\python\bulk_data_loader>

Database insert elapsed time (sec): 700.015625


Total records inserted ~25.5 millions rows



```