import unidecode,  time, winsound
#pip install Unidecode


def help():
      print("You need to install Unidecode for the program to run correctly. Please just copy and paste the following commands to your OS' terminal: \npip install Unidecode\n\n")
      print("This program is very badly optimised, but it gets the job done.\nEvery dot is represented by \".\" and every not-dot is represented by \"_\". \"/\" represent the end of words")
      print("The system of Morse code is the International Morse Code\n")
      print("If your translation  got \"*\" in your code it is probably because there is some special charcter in your input. Try re-running the program and remove all of those.")
      print("If you find any bug, please send it to aluno3591@gmail.com")
      print()
      print("\"--------------------------------\"" * 5)
      

def morse_translator(frase):
      frase = frase.lower()
      frase = unidecode.unidecode(frase)
      translation = ""


      for letra in frase:
            if letra == "a":
                  translation += "._" + " "
            elif letra== "b":
                  translation += "_..." + " "
            elif letra == "c":
                  translation += "_._." + " "
            elif letra == "d":
                  translation += "_.." + " "
            elif letra == "e":
                  translation += "." + " "
            elif letra == "f":
                  translation += ".._." + " "
            elif letra == "g":
                  translation += "__." + " "
            elif letra == "h":
                  translation += "...." + " "
            elif letra == "i":
                  translation += ".." + " "
            elif letra == "j":
                  translation += ".___" + " "
            elif letra == "k":
                  translation += "_._" + " "
            elif letra == "l":
                  translation += "._.." + " "
            elif letra == "m":
                  translation += "__" + " "
            elif letra == "n":
                  translation += "_." + " "
            elif letra == "o":
                  translation += "___" + " "
            elif letra == "p":
                  translation += ".__." + " "
            elif letra == "q":
                  translation += "__._" + " "
            elif letra == "r":
                  translation += "._." + " "
            elif letra == "s":
                  translation += "..." + " "
            elif letra == "t":
                  translation += "_" + " "
            elif letra == "u":
                  translation += ".._" + " "
            elif letra == "v":
                  translation += "..._" + " "
            elif letra == "w":
                  translation += ".__" + " "
            elif letra == "x":
                  translation += "_.._" + " "
            elif letra == "y":
                  translation += "_.__" + " "
            elif letra == "z":
                  translation += "__.." + " "
            elif letra == "1":
                  translation += ".____" + " "
            elif letra == "2":
                  translation += "..___" + " "
            elif letra == "3":
                  translation += "...__" + " "
            elif letra == "4":
                  translation += "...._" + " "
            elif letra == "5":
                  translation += "....." + " "
            elif letra == "6":
                  translation += "_...." + " "
            elif letra == "7":
                  translation += "__..." + " "
            elif letra == "8":
                  translation += "___.." + " "
            elif letra == "9":
                  translation += "____." + " "
            elif letra == "0":
                  translation += "_____" + " "
            elif letra == " ":
                  translation += "/"
            else:
                  translation += "*"
      return translation

def keep_translation(phrase, translation, name_of_the_file = ""):
      #Defensive programing
      if name_of_the_file == "":
            name_of_the_file = "Morse_Code_Translation"
      name_of_the_file += ".txt"

      #File opening
      new_file = open(name_of_the_file, "w+")

      new_file.write(phrase + ":\n")
      new_file.write(translation)#Write translation
      
      new_file.close()

def produce_sound(code):
      if code == ".":
            winsound.Beep(300, 200)
      elif code == "_":
            winsound.Beep(300, 400)
      elif code == "/":
            time.sleep(1)
      else:
            time.sleep(0.5)
      
