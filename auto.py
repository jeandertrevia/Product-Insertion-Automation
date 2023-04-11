# automacao cadastro produto

import pyautogui
from time import sleep

# Registro de Usuario
pyautogui.click(946, 605, duration=2)

pyautogui.click(964, 543, duration=2)
pyautogui.write("jeander")

pyautogui.click(968, 574, duration=2)
pyautogui.write('123')

pyautogui.click(915, 610, duration=2)

# 1 - Clicar e digitar meu usuario
pyautogui.click(1010, 538, duration=2)
pyautogui.write("jeander")

# 2 - Clicar e digitar minha senha
pyautogui.click(992, 572, duration=2)
pyautogui.write('123')

# 3 - clicar em "Entrar"
pyautogui.click(860, 612, duration=2)

# 4 - Extrair cada produto
with open('produtos.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

         #  1 - clicar e digitar produto
        pyautogui.click(668, 538, duration=2)
        pyautogui.write(produto)

        #  2 - clicar e digitar quantidade
        pyautogui.click(604, 560, duration=2)
        pyautogui.write(quantidade)

        #  3 - clicar e digitar preço
        pyautogui.click(631, 598, duration=2)
        pyautogui.write(preco)

        #  4 - clicar em registrar
        pyautogui.click(495, 790, duration=2)
        sleep(1)
