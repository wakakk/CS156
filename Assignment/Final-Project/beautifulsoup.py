from urllib.request import urlopen
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import requests


def ebay_url(keyword, page):
    ROOT = 'https://www.ebay.com/sch/i.html?'
    url = ROOT + urlencode({'_nkw': keyword, '_pgn': page})
    return url

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

result = []
i = 1
keyword = "hat"

page_link = ebay_url(keyword, i)
page_response = requests.get(page_link, headers=headers).text
page_content = BeautifulSoup(page_response, "html.parser")


# if page_content.find(class_='srp-results') is not None:
#     search_results = page_content.find(class_='srp-results').find_all(class_='s-item')
#     for item in search_results:
#         result.append(parse_item_ebay(item))
#         if len(result) > max_num:
#             result = result[:max_num]
#             return result
# elif page_content.find(class_='gv-ic full-width left') is not None:
#     search_results = page_content.find(class_='gv-ic full-width left').find_all(class_='sresult gvresult')
#     for item in search_results:
#         result.append(parse_item_ebay_alternative(item))
#         if len(result) > max_num:
#             result = result[:max_num]
#             return result
# else:
#     return result
# i += 1

print (page_content)
