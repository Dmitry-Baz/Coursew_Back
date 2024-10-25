import os
import requests
import json
from dotenv import load_dotenv
from pprint import pprint

# Загрузка переменных окружения
load_dotenv('config.env')

ya_token = os.getenv('YA_TOKEN')
vk_token = os.getenv('VK_TOKEN')


class VKBazyk:
    def __init__(self, access_token, version='5.199'):
        self.access_token = access_token
        self.version = version
        self.base_url = 'https://api.vk.com/method/'
        self.params = {
            'access_token': self.access_token,
            'v': self.version
        }

    def photo_info(self, user_id):
        url = f'{self.base_url}photos.get'
        params = {
            **self.params,
            'owner_id': user_id,
            'album_id': 'profile',
            'count': 5,
            'extended': 1
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Error fetching photos: {response.status_code}")
            return None
        return response.json()


class YD_VKBazyk:
    def __init__(self, token):
        self.headers = {'Authorization': f'OAuth {token}'}

    def create_folder(self, folder_name):
        response = requests.put(
            url='https://cloud-api.yandex.net/v1/disk/resources',
            headers=self.headers,
            params={'path': folder_name}
        )
        if response.status_code == 201:
            print(f'Folder "{folder_name}" successfully created.')
        elif response.status_code == 409:
            print(f'Folder "{folder_name}" already exists.')
        else:
            print(f'Failed to create folder "{folder_name}". Status code: {response.status_code}')
            print(f'API response: {response.json()}')
        return response.status_code

    def upload_file(self, file_path, file_name):
        upload_url = f"https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {'path': f'Ру-114/{file_name}', 'overwrite': 'true'}
        response = requests.get(upload_url, headers=self.headers, params=params)
        if response.status_code == 200:
            href = response.json().get('href')
            with open(file_path, 'rb') as file:
                upload_response = requests.put(href, files={'file': file})
                if upload_response.status_code == 201:
                    print(f"File '{file_name}' uploaded successfully.")
                else:
                    print(f"Error uploading file: {upload_response.status_code}")
        else:
            print(f"Error getting upload URL: {response.status_code}")


# Пример использования
vk_bazyk = VKBazyk(vk_token)
photos_info = vk_bazyk.photo_info(15272050)

if photos_info and 'response' in photos_info:
    yandex_disk = YD_VKBazyk(ya_token)
    folder_name = 'Ру-114'
    yandex_disk.create_folder(folder_name)

    results = []
    for photo in photos_info['response']['items']:
        likes_count = photo['likes']['count']
        file_name = f"{likes_count}.jpg"
        photo_url = photo['sizes'][-1]['url']  # Получаем URL самой большой фотографии
        
        # Загружаем фото на диск
        photo_response = requests.get(photo_url)
        if photo_response.status_code == 200:
            with open(file_name, 'wb') as f:
                f.write(photo_response.content)
            yandex_disk.upload_file(file_name, file_name)
            results.append({'file_name': file_name, 'likes': likes_count})
            os.remove(file_name)  # Удаляем локальный файл после загрузки
        else:
            print(f"Error fetching photo: {photo_response.status_code}")

    # Сохраняем информацию в JSON-файл
    with open('results.json', 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

    print("Results saved to results.json")
































