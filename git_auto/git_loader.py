import random
import string
import os
import sys
import platform

URL = f"https://github.com/{sys.argv[1]}/{sys.argv[2]}.git"
FILE_NAME = "random.txt"


def generate_random_python_code(length):
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    return ''.join(random.choice(characters) for _ in range(length))


def create_random_python_code_file():
    num_lines = random.randint(200, 500)
    max_line_length = 100  # İstediğiniz maksimum satır uzunluğu
    with open(FILE_NAME, "w") as f:
        for _ in range(num_lines):
            line = generate_random_python_code(max_line_length)
            f.write(line + "\n")


def delete_temp():
    os.chdir('..')

    if platform.system() == 'Windows':
        os.system("rmdir /s /q temp_repo")
    else:
        os.system('rm -rf temp_repo')


def clean_repository():
    os.system(f'git clone {URL} temp_repo')  # Uzak repo klonla
    os.chdir('temp_repo')  # Temp dizinine geç
    os.system('git rm -r *')  # Mevcut bütün dosyaları temizle
    os.system('git commit -m "Clean repository"')
    os.system('git push')  # Temizlenmiş repoyu geri yükle


def load_file():
    create_random_python_code_file()  # Temp dizininde random dosyayı oluştur
    os.system('git add {}'.format(FILE_NAME))
    os.system('git commit -m "Add {}"'.format(FILE_NAME))
    os.system('git push')  # Dosyayı geri yükle


def main():
    print("\n" + "="*10 + " Repository Temizleniyor " + "="*10)
    clean_repository()  # Önce mevcut bütün dosyaları temizle
    print("\n" + "="*10 + " Random Dosya Ekleniyor " + "="*10)
    load_file()  # Sonra belirtilen dosyayı yükle
    print("\n" + "="*10 + " Temp Dizini Siliniyor " + "="*10)
    delete_temp()  # Temp dizinini sil
    print("\n" + "="*10 + " Temp Dizini Silindi " + "="*10)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Example usage: python git-loader.py Nickname RepositoryName")
        exit()

    for i in range(random.randint(1, 1)):
        main()
