import os
import logging
from collections import namedtuple

# Конфигурация логирования
logging.basicConfig(filename='log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent'])

def get_file_info(path):
    try:
        entries = os.listdir(path)
        for entry in entries:
            full_path = os.path.join(path, entry)
            name, extension = os.path.splitext(entry)
            is_directory = os.path.isdir(full_path)

            file_info = FileInfo(name=name, extension=extension, is_directory=is_directory, parent=os.path.basename(path))
            logging.info(file_info)

            if is_directory:
                get_file_info(full_path)

    except OSError as e:
        logging.error(f"Ошибка при обработке {path}: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Обработка содержимого директории и логирование информации.")
    parser.add_argument("directory_path", help="Путь до директории для обработки.")

    args = parser.parse_args()

    if not os.path.exists(args.directory_path):
        print("Указанный путь к директории не существует.")
    else:
        get_file_info(args.directory_path)
