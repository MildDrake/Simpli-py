from sys import platform

if platform == "win32" or platform == "win64" or platform =="win86":
        
        import subprocess, socket , pdb
        from funcoes import *
        import datetime
        
        #Fazer a copia de seguranca#
        print("Cópia de segurança:")
        copia_de_seguranca("Lista_Wifi.txt","Lista_Wifi_Secure.txt")
        print("\n")





        #Abertura dos documentos
        Lista_Wifi_a = open("Lista_Wifi.txt", "a")
        Lista_Wifi_r = open("Lista_Wifi.txt","r")


        INPUT = str(input("Quer adicionar algo ao nome do dispositivo? (Enter para omitir)\n"))
        nome_dispositivo_default = socket.gethostname()
        if INPUT != "":
                nome_do_dispositivo = nome_dispositivo_default + " " + INPUT
        else:
                nome_do_dispositivo = nome_dispositivo_default
        texto_a_colocar = [nome_do_dispositivo]
        todas_linhas = Lista_Wifi_r.readlines()


        #Actual code
        #pdb.set_trace()
        data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("ISO-8859-1").split("\n")

        Wifi = [line.split(":")[1][1:-1] for line in data if "All User Profile" in line]

        if 'Gorillaz.\x82.mainstream' in Wifi:
                #por algum motivo esta rede dá erro, devido a um time-out... de qualquer forma não exite mais
                Wifi.remove('Gorillaz.\x82.mainstream')

        for wifi in Wifi:
                results = subprocess.check_output(["netsh", "wlan", "show", "profiles", wifi, "key=clear"]).decode("ISO-8859-1").split("\n")
                results = [line.split(":")[1][1:-1] for line in results if "Key Content" in line]
                try:
                        print(f'Nome: {wifi}, Password: {results[0]}')
                        texto_a_colocar.append(f'Nome: {wifi}, Password: {results[0]}')
                except IndexError:
                        print(f'Nome: {wifi}, Password: Cannot be read!')
                        texto_a_colocar.append(f'Nome: {wifi}, Password: Não foi possível ler')
                except:
                        print(f'Nome: {wifi}, Password: Cannot be read! Error(not IndexError)')
                        texto_a_colocar.append(f'Nome: {wifi}, Password: houve um erro qualquer')
                        continue

        added = ""
        not_added = 1
        for item in texto_a_colocar:
                if (item + "\n" not in todas_linhas and "\n" + item not in todas_linhas and item not in todas_linhas) or (nome_do_dispositivo in item):
                        ()
                else:
                        not_added += 1
        #pdb.set_trace()
                        
        if len(texto_a_colocar) == not_added:
                texto_a_colocar = texto_a_colocar[1:]
                
        not_added = ""
        
        for item in texto_a_colocar:
                #Adicionar o nome do dispositivo
                if nome_do_dispositivo in item:
                        Lista_Wifi_a.write("\n----------\"\"--- " + item + " ---\"\"----------\n")
                #Adicionar da rede e da password
                elif item + "\n" not in todas_linhas and "\n" + item not in todas_linhas and item not in todas_linhas:
                        Lista_Wifi_a.write("\n" + str(item))
                        added += item + "\n"
                else:
                        not_added += item + "\n"
                        
        


        #Relatório
        print("\n"*2)
        if relatorio(added, not_added) == True:
                time = datetime.datetime.now()
                dia = str(time.day) + "/" + str(time.month) + "/" + str(time.year)
                Lista_Wifi_a.write("\n\n" + dia + "\n")
                
                


        #Fim_da_cópia_das_passwords
        Lista_Wifi_a.close()
        Lista_Wifi_r.close()
        
        input()
        















#Excepções dos outros sistemas operativos
        
elif platform == "linux" or platform == "linux2" or "linux" in platform:
        print("Este código nunca foi testado em Linux")
        input("\nAvançar por conta e risco")
        quit()

elif platform == "darwin":
        print("Por favor, não utilizar o código em MacOS")
        print("\n")
        input("ATENÇÂO: NÃO ABRIR O DOCUMENTO \"Lista_Wifi.txt\" PARA NÂO DESFORMTÁ-LO")
        quit()
else:
        input("Mas que raio de sistema operativo andas a usar?")
        quit()


        
