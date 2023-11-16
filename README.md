
README - Progama de criptografia
## Introdução
Este é um programa Python que foi feito para facilitar o uso de hashs, criptografia de arquivos e analise para vericidade de arquivos

##Última Modificação: 16/11/2023 13:46

## Funcionalidades
O programa oferece as seguintes funcionalidades:

*Fazer a hash de um arquivo: Permite calcular hashes MD5, SHA256, ou SHA512 de um arquivo.

*Criptografar um arquivo em Fernet: Utiliza a biblioteca Fernet para criptografar um arquivo selecionado.

*Descriptografar um arquivo em Fernet: Descriptografa um arquivo previamente criptografado com Fernet.

*Comparar arquivos: Compara dois arquivos para verificar se possuem a mesma hash MD5, SHA256, e SHA512.

*Identificar tipo de hash: Informa o tipo de hash (MD5, SHA256, ou SHA512) com base no comprimento da hash fornecida.

## Utilização
Ao executar o programa, selecione a opção desejada digitando o número correspondente.
Para fazer a hash de um arquivo, criptografar ou descriptografar um arquivo em Fernet, siga as instruções apresentadas.

*1)Fazer a hash de um arquivo:
  Ao fazer a hash de um arquivo voce ira selecionar o tipo de hash disponivel MD5, SHA-256 ou SHA-512 após isso uma janela com o seu explorador de arquivos abrirá
  e voce escolhera o arquivo após isso o código ira executar e será demonstrado para voce a hash do arquivo

*2)Criptografar um arquivo em Fernet:
  Para criptografar um arquivo usando Fernet após selecionado a opção uma janela com o explorador de arquivos irá abrir e ao escolher o arquivo de sua escolha
  voce podera dar nome para um arquivo que conterar uma chave de criptografação após isso o arquivo sera criptografado e não poderá ser acessado dando erro.

  ![image](https://github.com/KaduLm/Crypto/assets/63614354/236d572e-72a8-460c-8b15-493347855903)

  ![image](https://github.com/KaduLm/Crypto/assets/63614354/8eaee6c0-785c-4c9a-8c88-7d955d44430f)

*3)Descriptografando um arquivo em Fernet:
  Para a descriptografação de um arquivo só sera possível se voce possuir a chave na qual ele foi criptografado, após ter acesso a essa chave podemos escolher o arquivo e digitar o nome da chave, 
  no exemplo abaixo foi usado o mesmo arquivo que usei para criptografar anteriormente

  ![image](https://github.com/KaduLm/Crypto/assets/63614354/e8129ab8-0648-49e8-be40-3aac410da176)

  ![image](https://github.com/KaduLm/Crypto/assets/63614354/5210ef94-4d99-40c1-a71c-ca751bdf4e2c)

*4)Comparar arquivos para descobrir se eles possuem a mesma hash:
  Para comparar se 2 arquivos possuem a mesma hash podemos usar essa função em que comparamos os arquivos nos modelos de hash MD5, SHA256, e SHA512.
  Primeiro ao selecionarmos a opção a janela do gerenciador de arquivos sera aberto e selecionaremos 1 arquivos e daremos enter, após isso essa janela abrira de novo e selecionaremos o 2 arquivo
  com isso o progama ira analisar as hashs de ambos e dira se são ou não identicos.

  ![image](https://github.com/KaduLm/Crypto/assets/63614354/9bdd942e-66d9-444a-9fdd-b4d23282585b)

  ![image](https://github.com/KaduLm/Crypto/assets/63614354/8e7f878a-338b-41bb-a339-cd23602a8244)

  Como pudermos ver os arquivos são diferentes nos conteudos então suas hashs tambem serão, mesmo se tiverem o mesmo nome isso não influenciara pois ele se baseia pelo conteudo.

*5)Identificar tipo de hash:
  Esta função tem como objeitvo identificar o tipo de hash no código desenvolvido apenas MD5, SHA256, e SHA512 são os modelos identificados, esta função foi baseada no que eu consegui entender do 
  "HASH IDENTIFER" que eu conheci pelo Kali Linux enquanto estudava um pouco sobre segurança da informação. Segue abaixo a foto do hash identifier

  ![image](https://github.com/KaduLm/Crypto/assets/63614354/1772cd3d-cabb-4ba3-a690-5bfe1271f288)

  Aqui é a minha versão:

![image](https://github.com/KaduLm/Crypto/assets/63614354/160605fd-fa51-4967-8b76-89e58f17d318)


## Requisitos
O código requer a instalação da biblioteca cryptography para o uso do Fernet. Você pode instalá-la utilizando o seguinte comando:

pip install cryptography


## Notas Adicionais
Certifique-se de ter permissões adequadas para ler, gravar e executar os arquivos que serão manipulados pelo programa.
Ao criptografar e descriptografar em Fernet, o programa utiliza arquivos com extensão .key para armazenar as chaves. Se o arquivo não existir, uma nova chave será gerada.

## Contribuições
Se você encontrar bugs, ou desejar contribuir com melhorias no código, sinta-se à vontade para entrar em contato.
