from functions import *
import os, time

#Do a backup of our .txt files
backup()

#get information of what Albums_I_have
albums_got = []
artists_got = []
dictionary_got = {}
get_alb_art_diction("Albums_I_have.txt", albums_got, artists_got, dictionary_got)

#get information of Albums_I_wanna_buy
albums_buy = []
artists_buy = []
dictionary_buy = {}
get_alb_art_diction("Albums_I_wanna_buy.txt", albums_buy, artists_buy, dictionary_buy)




while True:
    os.system("CLS")
    command = input("What do you want do?\n1 = Add an Album\n2 = Check my lists\n\"return\" to quit\n")
    os.system('CLS')


    #Add an Album
    if command == "1":
        while command != "":
            os.system('CLS')
            command = input("What do you want to do?\n1 = I Want to buy another Album\n2 = I Bought an Album\n\"return\" to quit\n")
            os.system('CLS')

            #Add to Buying list
            if command == "1":
                all = True
                while all == True:
                    os.system('CLS')
                    #Get the name of the album and artist
                    print("Make sure you write the names properly, please")
                    print("What is the name of the Album?")
                    name_alb = str(input())
                    print("What is the name of it's artist?")
                    name_art = str(input())

                    dictionary_buy[name_alb] = {name_art}

                    #are those all the inputs?
                    all = input("1 = I'm finished with my albums\n2 = I have more albums\n0 = Go back\n")
                    if all == "1":
                        all = False
                    elif all == "0":
                        break
                os.system('CLS')
                if all == "0":
                    #dictionary_buy[name_alb] might not exist
                    try:
                        del dictionary_buy[name_alb]
                        # won't execute write dictionary
                        continue
                    except:
                        # won't execute write dictionary
                        continue

                #writing everything as it should in the wish list
                write_dictionary(dictionary_buy, "Albums_I_wanna_buy.txt")


            #Bought an album
            #Remove the album from Albums_I_wanna_buy list, add it to Albums_I_have
            elif command == "2":
                print("Congratulations for your acquisition!")
                while True:
                    #Getting the names of the albums and artists
                    print("Make sure you write the names properly, please")
                    print("What is the name of the Album?")
                    name_alb = str(input())
                    #turn off
                    if name_alb == "":
                        print("Finishing the process...")
                        time.sleep(1)
                        break

                    print("What is the name of it's artist?")
                    name_art = str(input())

                    #turn off
                    if name_art == "":
                        print("Finishing the process...")
                        time.sleep(1)
                        break

                    try:
                        #if it exists in the wish list, delete it
                        if dictionary_buy[name_alb] == {name_art}:
                            del dictionary_buy[name_alb]
                    except:
                        print("I can see this Album wasn't in your wish list")
                        time.sleep(1.5)

                    #Creating the new items in te dictionary of Albums_I_have
                    dictionary_got[name_alb] = {name_art}

                    os.system("CLS")
                    print("If you don't have any other new albums PRESS RETURN")

                #Writing everything as it should on both list
                write_dictionary(dictionary_buy, "Albums_I_wanna_buy.txt")
                write_dictionary(dictionary_got, "Albums_I_have.txt")



            #Easter egg
            elif command.lower() == "break free":
                os.system('CLS')
                solta_o_som_DJ()
                input()

            else:
                os.system('CLS')
                print("There was an error, please try again")




    #Check lists
    elif command == "2":
        command = input("1 = Check Albums I have\n 2 = Check Albums_I_wanna_buy\n 3 = Check both Lists\n")
        os.system("CLS")

        #All the 3 different commands
        if command == "1":
            read_doc("Albums_I_Have.txt")
        elif command == "2":
            read_doc("ALbums_I_wanna_buy.txt")
        elif command == "3":
            read_doc("Albums_I_Have.txt")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            read_doc("ALbums_I_wanna_buy.txt")
        input()









    #Stop the program
    elif command == "":
        break
    #Error
    else:
        print("There was an error, please try again")
