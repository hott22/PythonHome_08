# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её
# и все вложенные директории.

# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов
# в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
import json
import os
import pickle
import csv


js_ = 'home8.json'
csv_ = 'home8.csv'
pickle_ = 'home8.pickle'
dir_ = 'D:\\Python\\new'


def directory_(json_file: str, csv_file: str, pickle_file, dir_path: str) -> None:
    dict_file_or_dir = {}
    for path, dir_name, file_name in os.walk(dir_path):
        print(f'{path = }\n{dir_name = }\n{file_name = }\n')
        list_dir = os.listdir(path)
        for i in list_dir:
            if os.path.isdir(path + '\\' + i):
                string = path + '\\' + i
                dict_file_or_dir[i] = {'entity': 'dir'}
                size = 0
                for ele in os.scandir(string):
                    size += os.stat(ele).st_size
                dict_file_or_dir[i]['size'] = str(size)

            elif os.path.isfile(path + '\\' + i):
                dict_file_or_dir[i] = {'entity': 'file'}
                dict_file_or_dir[i]['size'] = str(os.path.getsize(path + '\\' + i))
            dict_file_or_dir[i]['parent'] = path.split('\\')[-2]

    print(dict_file_or_dir)
    with(
        open(json_file, 'w', encoding='utf-8') as js_,
        open(csv_file, 'w', newline='', encoding='utf-8') as csv_,
        open(pickle_file, 'wb') as pick_,
    ):
        json.dump(dict_file_or_dir, js_, indent=2)
        pickle.dump(dict_file_or_dir, pick_)
        csv_write = csv.writer(csv_, dialect='excel')
        list_ = [[level_, id_, name_] for level_, i_u in dict_file_or_dir.items()
                 for id_, name_ in i_u.items()]
        csv_write.writerow(list_)


if __name__ == '__main__':
    directory_(js_, csv_, pickle_, dir_)
