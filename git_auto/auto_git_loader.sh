#!/bin/bash

read -p "Devam etmek istiyor musunuz? (E/H): " answer
if [[ "$answer" == "E" || "$answer" == "e" || "$answer" == "Y" || "$answer" == "y" ]]; then
    echo "Devam ediliyor..."
    python3 /home/onat/Masaüstü/dev/auto-gitPy/git-loader.py

else
    echo "İşlem iptal edildi."
fi

