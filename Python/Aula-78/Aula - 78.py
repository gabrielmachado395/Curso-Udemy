import os
import shutil

caminho_original = r'C:\Users\gabriel\OneDrive\Imagens\Capturas de tela'
caminho_novo = r'C:\Users\gabriel\OneDrive\Imagens\Capturas de tela2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if '.png' in file:
            os.remove(new_file_path)
            print(f'Arquivo {file} apagados com sucesso.')
        