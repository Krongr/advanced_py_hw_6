import requests


class YaDiskUser:
    initial_url = 'https://cloud-api.yandex.net/v1/disk/'


    def get_token(self, file_name:str) -> str:
        with open(file_name, 'rt', encoding='utf-8') as file:
            return file.read().strip()


    def create_folder(self, folder_name:str, url:str=initial_url) -> str:
        _headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.get_token("token.txt")}'
        }
        upload_url = f'{url}resources'
        params = {"path": folder_name}        
        return requests.put(upload_url, headers=_headers, 
            params=params)


    def get_folder_info(self, folder_name:str, url:str=initial_url) -> str:
        _headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.get_token("token.txt")}'
        }
        upload_url = f'{url}resources'
        params = {"path": folder_name}        
        return requests.get(upload_url, headers=_headers, 
            params=params)

    
    def delete_folder(self, folder_name:str, url:str=initial_url) -> str:
        _headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.get_token("token.txt")}'
        }
        upload_url = f'{url}resources'
        params = {"path": folder_name}        
        return requests.delete(upload_url, headers=_headers, 
            params=params)