from func_morse import *
import time

while True:
      #Need help?/quit
      input1 = input("help() for help\nquit() to quit\n")
      if input1 == "help()":
            help()
      elif input1 == "quit()":
            quit()

      #Translation
            
      frase = str(input("What phrase do you want to translate?  "))
      translation = morse_translator(frase)
      print(translation)


      #produce the sound
      for code in translation:
            produce_sound(code)
            


      #Confirming the keep function
      print("\n"*4)

      do = input("Do you want to keep the translation in a .txt file? (Return to omit)\ny or n?")
      password = ""
      while password != "123banzai":
            do = do.lower()
            if do == "y":
                  name_of_the_file = input("\nWhat is the name you want for the file of your translation? \nATTENTION: If you choose an already existing file, ***it will be overwritten***\n")
                  keep_translation(frase ,translation, name_of_the_file)
                  password = "123banzai"
            elif do == "n" or do == "":
                  password = "123banzai"
            else:
                  do = input("I'm sorry, I did not understand.\ny or n?")

      print("\"--------------------------------\"" * 5)




            
