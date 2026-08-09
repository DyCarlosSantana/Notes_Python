# Usar Pillow ou OpenCV


from PIL import Image
import os # Importar para verificar se o arquivo existe

''' Imagens PNG são arquivos que contém transparência (RGBA) que o JPEG não suporta, por isso é necessário converter para RGB. Essa conversão não se faz necessaria em outros tipos de arquivo como JPG, JPEG, GIF, etc'''

pasta_arquivos = os.listdir('Imagens')
print(pasta_arquivos)

for arquivo in pasta_arquivos:
    # Abrir o arquivo
    img = Image.open(f'Imagens/{arquivo}').convert('RGB')

    # Salvar o aquivo em outro formato
    img.save(f'PDF/{arquivo}.pdf') #ou podemos usar o .replace para substituir o .png por .jpg
    
    
