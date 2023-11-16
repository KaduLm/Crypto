'''TENTATIVA DE ALTERAÇÕES NA FUNÇÃO DE HASH COM O INTUITO DE REDUZIR E FACILITAR O CÓDIGO 
Ultima modificação: 16/11/2023 13:46'''

import os
import tkinter as tk
from tkinter import filedialog
import tkinter
from cryptography.fernet import Fernet
import hashlib
import time
import progressbar



def escolha():
    root = tkinter.Tk()  
    root.withdraw()

    print(" BBBBBBB      A     TTTTTTTTT  CCCCC    OOO   DDDDD   EEEEE")
    print(" B     B     A A        T     C     C  O   O  D    D  E")
    print(" B     B    A   A       T     C        O   O  D     D E")
    print(" BBBBBBB   A     A      T     C        O   O  D     D EEEEE")
    print(" B     B  AAAAAAAA      T     C        O   O  D     D E")
    print(" B     B  A       A     T     C     C  O   O  D    D  E")
    print(" BBBBBBB A         A    T      CCCCC    OOO   DDDDD   EEEEE")

    while True:
        resp_criptografada = None

        print("1. Fazer a hash de um arquivo")
        print("2. Criptografar um arquivo em Fernet")
        print("3. Descriptografar um arquivo em Fernet")
        print("4. Comparar arquivos para descobrir se eles possuem a mesma hash")
        print("5. Identificar tipo de hash")
        print("6. Sair")

        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            hash()
        elif opcao == 2:
            resp_criptografada = Cripto_Fernet()
            for i in progressbar.progressbar(range(100)):
                time.sleep(0.1)
            if resp_criptografada:
                print("O arquivo " + resp_criptografada + " foi criptografado em Fernet")
            else:
                print("Nenhum arquivo foi criptografado em Fernet")
        elif opcao == 3:
            resp_criptografada = Descripto_Fernet()
            for i in progressbar.progressbar(range(100)):
                time.sleep(0.1)
            if resp_criptografada:
                print("O arquivo " + resp_criptografada + " foi descriptografado em Fernet")
            else:
                print("Nenhum arquivo foi descriptografado em Fernet")
        elif opcao == 4:
            comparador()
        elif opcao == 5:
            identificar_hash()
        elif opcao == 6:
            print("Saindo...")
            break

    root.destroy()  



def escolher_arquivo(root):
    arquivo_escolhido = filedialog.askopenfilename()

    if arquivo_escolhido:
        print("O arquivo a ser criptografado será o " + arquivo_escolhido)
        return arquivo_escolhido
    else:
        resp = input("Nenhum arquivo foi escolhido, deseja voltar ao menu? (S/N): ")
        if resp.lower() == 's':
            return escolher_arquivo(root)
        else:
            escolha()


def comparar_arquivo():
    window = tk.Tk()
    window.withdraw()
    primeiro_arquivo = filedialog.askopenfilename()

    print("O primeiro arquivo a ser comparado será o " + primeiro_arquivo)

    window = tk.Tk()
    window.withdraw()
    segundo_arquivo = filedialog.askopenfilename()

    print("O segundo arquivo a ser comparado será o " + segundo_arquivo)

    if primeiro_arquivo and segundo_arquivo:
        with open(primeiro_arquivo, 'rb') as arquivo1, open(segundo_arquivo, 'rb') as arquivo2:
            conteudo1 = arquivo1.read()
            conteudo2 = arquivo2.read()
            
            hash_md5_1 = hashlib.md5(conteudo1).hexdigest()
            hash_md5_2 = hashlib.md5(conteudo2).hexdigest()

            hash_sha256_1 = hashlib.sha256(conteudo1).hexdigest()
            hash_sha256_2 = hashlib.sha256(conteudo2).hexdigest()

            hash_sha512_1 = hashlib.sha512(conteudo1).hexdigest()
            hash_sha512_2 = hashlib.sha512(conteudo2).hexdigest()

        funcao_timer()
        if hash_md5_1 == hash_md5_2:
            print("Mesma hash MD5: " + hash_md5_1)
        else:
            print("Hashs MD5 diferentes: " + hash_md5_1 + " " + hash_md5_2)

        if hash_sha256_1 == hash_sha256_2:
            print("Mesma hash SHA256: " + hash_sha256_1)
        else:
            print("Hashs SHA256 diferentes: " + hash_sha256_1 + " " + hash_sha256_2)

        if hash_sha512_1 == hash_sha512_2:
            print("Mesma hash SHA512: " + hash_sha512_1)
        else:
            print("Hashs SHA512 diferentes: " + hash_sha512_1 + " " + hash_sha512_2)
    else:
        return 0

def hash_MD5():
    caminho_do_arquivo = escolher_arquivo()
    if caminho_do_arquivo:
        tamanho_arquivo = os.path.getsize(caminho_do_arquivo)
        with open(caminho_do_arquivo, 'rb') as arquivo:
            conteudo = arquivo.read()
            hash_obj = hashlib.md5(conteudo)
            criptogracao = hash_obj.hexdigest()
            return criptogracao
    else:
        return 0


def hash_SHA256():
    caminho_do_arquivo = escolher_arquivo()
    if caminho_do_arquivo:
        with open(caminho_do_arquivo, 'rb') as arquivo:
            conteudo = arquivo.read()
            hash_obj = hashlib.sha256(conteudo)
            criptogracao = hash_obj.hexdigest()
            return criptogracao
    else:
        return 0


def hash_SHA512():
    caminho_do_arquivo = escolher_arquivo()
    if caminho_do_arquivo:
        with open(caminho_do_arquivo, 'rb') as arquivo:
            conteudo = arquivo.read()
            hash_obj = hashlib.sha512(conteudo)
            criptogracao = hash_obj.hexdigest()
            return criptogracao
    else:
        return 0


def Cripto_Fernet():
    caminho_do_arquivo = escolher_arquivo()
    if caminho_do_arquivo:
        arquivo_chave = input("Digite o nome do arquivo .key para usar como chave: ")
        chave = ler_chave(arquivo_chave)
        fernet = Fernet(chave)

        with open(caminho_do_arquivo, 'rb') as arquivo:
            conteudo_arquivo = arquivo.read()

        criptografado = fernet.encrypt(conteudo_arquivo)

        with open(caminho_do_arquivo, 'wb') as arquivo_criptografado:
            arquivo_criptografado.write(criptografado)

        print("Arquivo criptografado em Fernet com sucesso.")
        return caminho_do_arquivo

def Descripto_Fernet():
    caminho_do_arquivo = escolher_arquivo()
    if caminho_do_arquivo:
        arquivo_chave = input("Digite o nome do arquivo .key para usar como chave: ")
        chave = ler_chave(arquivo_chave)
        fernet = Fernet(chave)

        with open(caminho_do_arquivo, 'rb') as arquivo_criptografado:
            criptografado = arquivo_criptografado.read()

        descriptografado = fernet.decrypt(criptografado)

        arquivo_descriptografado_nome = caminho_do_arquivo.replace('.encrypted', '.decrypted')

        with open(arquivo_descriptografado_nome, 'wb') as arquivo_descriptografado:
            arquivo_descriptografado.write(descriptografado)

        print("Arquivo descriptografado em Fernet com sucesso. Salvo como:", arquivo_descriptografado_nome)
        return caminho_do_arquivo


def ler_chave(nome_arquivo_chave):
    extensao = '.key'
    arquivo = nome_arquivo_chave + extensao

    if not nome_arquivo_chave:
        return Fernet.generate_key()

    if not os.path.isfile(arquivo):
        print("Arquivo de chave não encontrado. Criando uma nova chave...")
        chave = Fernet.generate_key()
        with open(arquivo, 'wb') as filekey:
            filekey.write(chave)
        print(f"Chave Fernet gerada e salva no arquivo '{arquivo}' com sucesso.")
    else:
        with open(arquivo, 'rb') as filekey:
            chave = filekey.read()
    return chave


def comparador():
    comparar_arquivo()


def funcao_timer():
    for i in progressbar.progressbar(range(50)):
        time.sleep(0.1)


def identificar_hash():
    print("Cole a hash: ")
    hash = input()
    funcao_timer()
    if len(hash) == 32:
        print("Hash está no padrão MD5")
    elif len(hash) == 64:
        print("Hash está no padrão SHA256")
    elif len(hash) == 128:
        print("Hash está no padrão SHA512")

def hash():
    print("1. MD5")
    print("2. SHA256")
    print("3. SHA512")
    number = int(input())
    if(number==1):
        resp_criptografada = hash_MD5()
        funcao_timer()
        if resp_criptografada:
                print("Essa hash " + resp_criptografada + " foi do arquivo escolhido e está no formato MD5")
        else:
                print("Não foi feita a hash em MD5")
    elif(number==2):
        resp_criptografada = hash_SHA256()
        funcao_timer()
        if resp_criptografada:
                print("Essa hash " + resp_criptografada + " foi do arquivo escolhido e está no formato SHA256")
        else:
                print("Não foi feita a hash em SHA256")
    elif(number==3):
        resp_criptografada = hash_SHA512()
        funcao_timer()
        if resp_criptografada:
                print("Essa hash  " + resp_criptografada + " foi do arquivo escolhido e está no formato SHA512")
        else:
                print("Não foi feita a hash em SHA512")
    else:
        escolha()


if __name__ == "__main__":
    escolha()

