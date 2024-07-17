import pyautogui
import time
import os

def abrir_erp_login():
    # ABERTURA DO SISTEMA
    print("Abrindo ERP")
    os.startfile('C:\\Program Files\\Alterdata\\ERP\\Bimer.exe')
    time.sleep(5)

    # INSERIR USUARIO
    # pyautogui.click(950, 454)
    # pyautogui.write('MOISES')

    # INSERIR SENHA
    print("Inserindo Senha")
    pyautogui.click(945, 523)
    pyautogui.write('09042021')

    time.sleep(1)

    # ENTRAR
    print("Entrando")
    pyautogui.click(981, 631)
    time.sleep(1)

def extrair_relatorio():
    # EXPANDIR FATURAMENTO
    pyautogui.click(170, 231)
    time.sleep(1)

    # ABRIR FATURAMENTO
    pyautogui.click(108, 266)
    time.sleep(1)

    # ABRIR BI ESTOQUE
    pyautogui.click(133, 267)
    time.sleep(2)

    # RECUPERAR CENÁRIO
    pyautogui.click(156, 77)
    time.sleep(2)

    # SELECIONAR BI
    pyautogui.click(916, 396)
    time.sleep(2)

    # CONFIRMAR BI
    pyautogui.click(1060, 768)
    time.sleep(2)

    # FILTRAR 
    pyautogui.click(456, 81)
    time.sleep(5)

    # EXPORTAR
    print("Exportando")
    pyautogui.click(903, 85)
    time.sleep(1)

    # SELECIONAR PARA SOBRESCREVER
    pyautogui.click(804, 345)
    time.sleep(1)

    # SALVAR
    print("Salvando")
    pyautogui.click(1326, 608)
    time.sleep(1)

    # CONFIRMAR SAVE
    pyautogui.click(931, 548)

def executar_etl():
    # EXECUTAR EXTRATOR DE PYTHON
    os.startfile('C:\\Users\\Administrador\\Desktop\\Loja\\Busca Preço\\cod\\etl.py')
    time.sleep(2)

def fechar_sistema():
    # FECHANDO SISTEMA
    pyautogui.click(1902, 10)
    time.sleep(1)

    # CONFIRMANDO
    pyautogui.click(836, 554)

def main():
    abrir_erp_login()
    extrair_relatorio()
    executar_etl()
    fechar_sistema()
if __name__ == "__main__":
    main()

print("Finalizado")