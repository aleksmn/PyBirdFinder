import os
import logging

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)
logging.debug('Start of program')

file_path = os.path.dirname(__file__) + '/bird-data.txt'

logging.debug('file_path: ' + file_path)


def get_content(file_path):
    """Get list of lines from the file"""
    with open(file_path) as f:
        content = f.readlines()
    return [x.rstrip() for x in content]


def find_items(string, list_of_stings):
    """Find items conteining string in list"""
    return [x for x in list_of_stings if string in x or string.title() in x]


print('Здравствуйте, это Поиск Птиц!')

while True:
    to_find = input('Найти: ')
    logging.debug('input: ' + to_find)
    if to_find == 'end':
        logging.debug('end of script')
        break
    for i in find_items(to_find, get_content(file_path)):
        print(i)
    logging.debug('search ended')
    print('Поиск закончен.')

print('Спасибо за использование Поиска Птиц! До свидания!')
logging.debug('End of program')