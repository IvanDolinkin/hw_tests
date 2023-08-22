import requests
import os
from dotenv import load_dotenv

load_dotenv()

DISK_TOKEN = os.getenv('DISK_TOKEN')
path = os.getenv('disk_path')


def create_folder(token, path):
    headers = {'Accept': 'application/json', 'Authorization': token}
    params = {'path': path}
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    resp = requests.put(url, params=params, headers=headers)
    return resp.status_code


def delete_folder(token, path):
    headers = {'Accept': 'application/json', 'Authorization': token}
    params = {'path': path}
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    resp = requests.delete(url, params=params, headers=headers)
    return resp.status_code


def get_info(token, path):
    headers = {'Accept': 'application/json', 'Authorization': token}
    params = {'path': path}
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    resp = requests.get(url, params=params, headers=headers)
    return resp


if __name__ == '__main__':
    # print(create_folder(DISK_TOKEN, path))
    # print(delete_folder(DISK_TOKEN, path))
    info = get_info(DISK_TOKEN, path)
    print()
