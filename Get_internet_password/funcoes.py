#Todas as funções utilizadas em Wifi_password.py

def relatorio(added, not_added):
    
    if added != "" :
        print("Estas são as novas adições:\n" + added)
        print("\n")
        if not_added != "":
            print("Estas combinações não foram adicionadas por já existirem na base de dados:\n" + not_added)
        return True
    elif added != "":
        print("Não há adições para a base de dados. Todas as combinações já estão presentes")
        return False
    elif added == "" and not_added == "":
        print("Não há redes disponíveis neste computador")
    else:
        return False
        

def copia_de_seguranca(ficheiro, ficheiro_seguranca):
    f = open(ficheiro,"r")
    f_s = open(ficheiro_seguranca, "w")
    copia_seguranca = f.read()
    f_s.write(copia_seguranca)

    f.close()
    f_s.close()

    sucesso = "Cópia de segurança efetuada com sucesso"
    return print(sucesso)

    
