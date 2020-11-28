import json
import os


def logger(file, i, string='ошибка', err=''):
    with open('readme.txt', 'a', encoding='utf-8') as log:
        log.write(f'{file}/{i} {string} {err}\n')


files = os.listdir()
for file in files:

    if os.path.isdir(file):
        if file[0] == '.':
            continue  # делал в PC исключал рабочую папку
        else:
            lst = os.listdir(file)

            for i in lst:
                with open(f'{file}/{i}') as read_f:
                    data = json.load(read_f)
                    if file == 'event':
                        try:
                            us_id = data['user_id']
                            if us_id == None:
                                string = 'не верные данные user_id:'
                                logger(file, i, string, us_id)
                            if i[:-5] != data['id']:
                                string = 'название файла не совпадает с ID'
                                logger(file, i, string)
                        except Exception as err:
                            string = 'ошибка:'
                            logger(file, i, string, err)
                    if type(data) != dict:
                        err = type(data)
                        string = 'имеет не верный тип:'
                        logger(file, i, string, err)
                    else:
                        try:
                            if len(data) == 0:
                                err = len(data)
                                string = 'имеет длину:'
                                logger(file, i, string, err)
                        except Exception as err:
                            string = 'ошибка'
                            logger(file, i, string, err)
