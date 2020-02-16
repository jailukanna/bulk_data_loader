import xmltodict
import requests

NYC_BIKE_SHARE_S3_REPO = 'https://s3.amazonaws.com/capitalbikeshare-data'


def _s3_xml_result_to_dict():
    response = requests.get(NYC_BIKE_SHARE_S3_REPO)
    print(response.content)
    ordered_dict = xmltodict.parse(response.content)['ListBucketResult']['Contents']
    print(ordered_dict)
    for value in ordered_dict:
        print(value)
        for val1 in value:
            print(val1)
            print(value[val1])

    result = [items[key] for items in ordered_dict for key in items if key == 'Key' and '.zip' in items[key]]
    print(result)


if __name__ == '__main__':
    _s3_xml_result_to_dict()
