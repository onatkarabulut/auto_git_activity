#!/bin/bash

read -p "Devam etmek istiyor musunuz? (E/H): " answer
if [[ "$answer" == "E" || "$answer" == "e" || "$answer" == "Y" || "$answer" == "y" ]]; then
    read -p "GitHub kullanıcı adınızı giriniz: " github
    read -p "Repository ismini giriniz: " repository
    echo "Devam ediliyor..."
    python3 ./git-loader.py $github $repository

else
    echo "İşlem iptal edildi."
fi

