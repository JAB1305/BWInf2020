import random
import string
import time
from http import HTTPStatus

import requests


def check_site_exist(url):
    try:
        request = requests.get(url)
        return request.status_code == HTTPStatus.OK
    except:
        return False


foundUrl = False

while not foundUrl:
    url_start = "https://bbb-schulen.rlp.net/b/"
    token = (random.choice(string.digits)
             + random.choice(string.digits)
             + random.choice(string.digits)
             + "-"
             + random.choice(string.ascii_lowercase + string.digits)
             + random.choice(string.ascii_lowercase + string.digits)
             + random.choice(string.ascii_lowercase + string.digits)
             + "-"
             + random.choice(string.ascii_lowercase + string.digits)
             + random.choice(string.ascii_lowercase + string.digits)
             + random.choice(string.ascii_lowercase + string.digits)
             + "-"
             + random.choice(string.ascii_lowercase + string.digits)
             + random.choice(string.ascii_lowercase + string.digits)
             + random.choice(string.ascii_lowercase + string.digits))
    final_url = url_start + token
    file = open("urlfinder.txt", 'r', encoding='utf8')
    lines = file.readlines()
    print(len(lines))
    if any(final_url in s for s in lines):
        print("Duplicate")
        break
    writer = open("urlfinder.txt", 'a', encoding='utf8')
    writer.write("\n" + final_url)
    writer.close()
    if check_site_exist(final_url):
        print("Found URL")
        foundUrl = True
        break
    print("URL doesnt exist")
    time.sleep(3)
