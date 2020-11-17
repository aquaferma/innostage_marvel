import requests
import hashlib
import datetime
import json
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

public_key = settings.MARVEL_PUBLIC_KEY
private_key = settings.MARVEL_PRIVATE_KEY


def get_hash(timestamp):
    hash = hashlib.md5()
    hash.update(str(timestamp).encode('utf-8'))
    hash.update(private_key.encode('utf-8'))
    hash.update(public_key.encode('utf-8'))
    return hash.hexdigest()


def get_auth_credentials():
    timestamp = datetime.datetime.now().timestamp()

    return {
        "ts": timestamp,
        "hash": get_hash(timestamp),
        "apikey": public_key,
    }


def make_request(uri, params):
    
    auth_creds = get_auth_credentials()
    params.update(auth_creds)

    try:
        response = requests.get(uri, params=params)

    except requests.RequestException as ex:

        logger.error(f"Marvel API network error: {ex} uri {uri} params: {params}")
        return True, "Проблемы с соединением, повторите позже"

    if response.status_code == 200:
        try:
            data = response.json()

            logger.info(f"Marvel API: uri: {uri} params: {params} json: {data}")

            return False, data

        except json.JSONDecodeError as ex:
            logger.error(f"Marvel API json decode error: {ex} uri: {uri} params: {params} body: {response.body}")

            return True, "Ошибка сервера"

    elif response.status_code == 409:
        return True, "Ошибка входных параметров"
    
    elif response.status_code == 404:
        return True, "Данных не найдено"

    else:
        logger.error(f"Marvel API status_code error: {ex} uri: {uri} params: {params} body: {response.body}")
        return True, "Непредвиденная ошибка, обратитесь к администратору "
    
        
        


