import requests
def yadisk_folder_create(token: str) -> int:
    url_yadisk = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers_yadisk = {'Authorization': token}
    response = requests.put(url_yadisk, params={'path': 'test'}, headers=headers_yadisk)
    return response.status_code
def yadisk_folder_delete(token: str) -> int:
    url_yadisk = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers_yadisk = {'Authorization': token}
    response = requests.delete(url_yadisk, params={'path': 'test'}, headers=headers_yadisk)
    return response.status_code
if __name__ == '__main__':
    token = '' # Введите свой токен
    print(yadisk_folder_create(token))
    print(yadisk_folder_delete(token))