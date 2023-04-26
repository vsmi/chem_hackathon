from scholarly import scholarly, ProxyGenerator
import json

FILE = 'test.json'
#FILE = 'key_words.json'
# API_KEY = 'a2c9a2977a45bfe07ba0e0823bbcfc20'  # qarnavalvleg@gmail.com
#API_KEY = '5d00a7f480732c7529ed954bc73a1f73'  # vikulek.smi@gmail.com


# API_KEY = 'ab8689d71796916e3fea09000fc965b5'  # vleg.turk@gmail.com
API_KEY = 'cce7489e8ac31351b35f70dfa735cd5b' # vika.smirnowa@yandex.ru
# API_KEY = '8bdae1708a84c12dce6d2c5cd461739f' #Dima1


def find_articles(kw: str):
    search_query = scholarly.search_pubs(kw, year_low=2020, sort_by='date')
    lists_of_articles = []
    try:
        for i in range(2):
            lists_of_articles.append(next(search_query))
    except StopIteration:
        print("STOP ITERATION")
    json_item = json.dumps(lists_of_articles, indent=4)
    return json_item


"""
Настройка прокси
"""
pg = ProxyGenerator()
success = pg.ScraperAPI(API_KEY)
#success = pg.FreeProxies()
scholarly.use_proxy(pg)

"""
Работа со списком ключевых слов
"""
with open(FILE, 'r') as f_for_read:
    d = json.load(f_for_read)
    for key, value in d.items():
        print(f"Start for feature {key}")
        for key_word in value:
            with open(f'outputs/{key}_{key_word}.json', 'w+') as f:
                print(f"Retrieve data for {key_word}")
                json_to_write = find_articles(key_word)
                f.write(json_to_write)
                print(f"Stop for feature {key}")







#search_query = scholarly.search_pubs('hepatogenous poisoning', year_low=2020, sort_by='date')
# try:
#     search_query = scholarly.search_pubs('Perception of physical stability and center of mass of 3D objects')
#     scholarly.pprint(next(search_query))
# except StopIteration:

# search_query = scholarly.search_pubs('hepatogenous poisoning', year_low=2000, sort_by='date')
# with open('generator.txt', 'r') as f1:
#     lst = []
#     for line in f1:
#         s = f1.readline()
#         print(s)
#         json_acceptable_string = s.replace("'", "\"")
#         print(type(json_acceptable_string))
#         d = json.loads(json_acceptable_string)
#         print(type(d))
#         # lst.append(d)
#
# search_query = iter(lst)
# total = search_query.total_size
# total = len(search_query)

#iter1 = iter(range(5))

# try:
#     lst1 = []
#     for i in range(3):
#         print(f'{i=}')
#         a = next(iter1)
#         print(a)
#         lst1.append(a)
#     print('inside try', lst1)
# except StopIteration:
#     print("We are here")
#     print('inside except', lst1)
#
# print('the end')
# s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
# json_acceptable_string = s.replace("'", "\"")
# d = json.loads(json_acceptable_string)
#
# print(d, type(d))
