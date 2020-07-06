import os
import vlc
import logging
import webbrowser

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program')

my_dir = os.path.dirname(__file__)

BIRD_DATA = my_dir + '/bird-data.txt'
logging.debug('BIRD_DATA: ' + BIRD_DATA)

def play_sound(num, audio_dir = my_dir + '/media/audio/'):
    """Play mp3 file from audio directory"""

    fnames = os.listdir(audio_dir)
    file = [x for x in fnames if num.zfill(3) in x][0]
    logging.debug('Playing mp3: ' + audio_dir + file)
    print(f'Воспроизводится файл {file}')
    p = vlc.MediaPlayer(audio_dir + file)
    p.audio_set_volume(50)
    p.play()


def open_images(string_to_search):
    s = 'https://duckduckgo.com/?t=lm&q=' + string_to_search + '&ia=images&atb=v182-1&iax=images'
    webbrowser.open(s)

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
    if to_find == 'q':
        logging.debug('end of script')
        break
    for i in find_items(to_find, get_content(BIRD_DATA)):
        print(i)
    logging.debug('search ended')
    print('Поиск закончен.')
    user_input = input('Введите номер, чтобы воспроизвести аудио: ')
    if user_input == '':
        continue
    else:
        try:
            item = find_items(user_input, get_content(BIRD_DATA))[0]
            print('Выбрана запись', item)
            play_sound(user_input)
        except IndexError as error:
            print("Файл не найден. Ошибка:", error)

        yn = input('Искать фото в интернете? (д/н) ')
        if yn.upper() == 'Д':
            string_to_search = item.split(' - ')[1]
            open_images(string_to_search)
        else:
            continue 
    

print('Спасибо за использование Поиска Птиц! До свидания!')
logging.debug('End of program')