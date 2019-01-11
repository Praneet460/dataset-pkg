from requests import get
from requests.exceptions import RequestException
from contextlib import closing


def simple_get(url: str):
    """
    Attempts to get the content at 'url' by making an HTTP GET request. If the content-type of response is some kind of HTML/XML, return the text content, otherwise return None.
    """

    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as error:
        log_error('Error during requests to {0} : {1}'.format(url, str(error)))
        return None


def is_good_response(resp):
    """
    Return True if the response seems to be HTML, False otherwise
    """
    content_type = resp.headers['content-type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def log_error(error):
    """
    It is always a good idea to log errors. This function just prints them.
    """
    print(error) 


if __name__ == '__main__':
    """
    Return the simple_get function on 'www.google.com'
    """
    print(simple_get('https://www.google.com/'))