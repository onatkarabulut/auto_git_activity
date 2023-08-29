import random
import string
import os

def generate_random_python_code(length):
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    return ''.join(random.choice(characters) for _ in range(length))

def create_random_python_code_file(filename):
    num_lines = random.randint(500, 1000) 
    max_line_length = 200  # İstediğiniz maksimum satır uzunluğu
    with open(filename, "w") as f:
        for _ in range(num_lines):
            line = generate_random_python_code(max_line_length)
            f.write(line + "\n")
    

def clean_repository():
    os.system('git clone {} temp_repo'.format(repo_name))  # Uzak repo klonla
    os.chdir('temp_repo')  # Temp dizinine geç
    os.system('git rm -r *')  # Mevcut bütün dosyaları temizle
    os.system('git commit -m "Clean repository"')
    os.system('git push origin main')  # Temizlenmiş repoyu geri yükle
    os.chdir('..')  # Önceki dizine geri dön
    os.system('rm -rf temp_repo')  # Temp dizini sil

def load_file(filename):
    os.system('git clone {} temp_repo'.format(repo_name))  # Uzak repo klonla
    os.chdir('temp_repo')  # Temp dizinine geç
    os.system('cp ../{} .'.format(filename))  # Hedef dosyayı temp dizinine kopyala
    os.system('git add {}'.format(filename))
    os.system('git commit -m "Add {}"'.format(filename))
    os.system('git push origin main')  # Dosyayı geri yükle
    os.chdir('..')  # Önceki dizine geri dön
    os.system('rm -rf temp_repo')  # Temp dizini sil

def main():
    filename = "random_python_code.py"
    create_random_python_code_file(filename)
    print("===============================================")
    clean_repository()  # Önce mevcut bütün dosyaları temizle
    print("===============================================")
    load_file(filename)  # Sonra belirtilen dosyayı yükle
    print("===============================================")
    
if __name__ == '__main__':
    repo_name = "https://github.com/onatkarabulut/git_loader.git" # Öncelikle GitHub'da bir private repo oluşturun ve linkini sonuna '.git' ekleyerek girin
    for i in range (random.randint(1,8)):
        main()
