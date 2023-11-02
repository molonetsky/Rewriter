import os

print('Current folder:', os.getcwd())


def rewritten_files():

    try:
        path = f"{str(input('Введите каталог откуда переписывать файлы: '))}"
        os.chdir(path)
        new_file = f"{str(input('Введите имя будучи созданного файла: '))}"     # задаём имя файлу который всё соберёт
        file = open(f'{new_file}', 'w')     # открываем файл

        st_number = 0
        for files in os.walk(path):
            files_names = files[2]
            for names in files_names:
                st_number += 1
                file.write(str(st_number) + ' ' + files[0] + "\\" + names + '\n')
        print(f'Всего было переписано {st_number} файлов')
        print(f'Реврайт прошёл успешно!')
        file.close()

    except Exception as _ex:
        print('Пожалуйста, проверьте код на наличие ошибок')


def main():
    rewritten_files()


if __name__ == '__main__':
    main()
