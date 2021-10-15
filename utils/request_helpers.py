import requests
import logging
from bs4 import BeautifulSoup
from .protocol_prefix import check_protocol
# from mg_exceptions.exc import WebsiteNotFoundError


def get_webpage(url) -> str:
    try:

        response = requests.get(url)
        if response.status_code in range(200, 299):
            logging.info(f'Status code: {response.status_code} for {url}')
            return response.text

    except requests.exceptions.ConnectionError:
        logging.error(f'Website "{url}" was not found.')
        # raise WebsiteNotFoundError
        # if we find some dead link I do not wanna script to break.
        # Here we do a logging of it and continuing to parse...
    finally:
        pass


def clear_links(response) -> list:
    if response is not None:
        parser = BeautifulSoup(response, 'html.parser')
        links = parser.find_all('a')
        all_links = [_.get('href') for _ in links]
        http_links = [_ for _ in all_links if check_protocol(_)]
        return http_links
    else:
        return []
