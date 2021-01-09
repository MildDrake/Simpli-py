from playsound import playsound
from shutil import copyfile
import os


def backup():
    bar = "\ "
    Back_Up_have = str(os.getcwd()) + bar[:1] + "Back_Up" + bar[:1] + "Albums_I_have_secure.txt"
    Back_Up_buy = str(os.getcwd()) + bar[:1] + "Back_Up" + bar[:1] + "Albums_I_wana_buy_secure.txt"
    copyfile("Albums_I_have.txt", Back_Up_have)
    copyfile("Albums_I_wanna_buy.txt", Back_Up_buy)

def get_alb_art_diction(file, albums, artists, dictionary):
    # //opening files

    alb_file = open(file, "r")    
    list_of_lines = alb_file.readlines()
    
    # //formating the Lists
    list_of_lines = list_of_lines[1:]

    # here we verify the existing albums, artists and we make our dictionary
    for i in range(len(list_of_lines)):
        stuff = list_of_lines[i]

        # If "stuff" is an artist do this:
        if (stuff != "\n") and (stuff[0] != "-"):
            # put it in artists list
            artists.append(stuff[:-2])

            for item in list_of_lines[i + 1:]:
                if item == "\n":
                    # Ignore, it's a new line
                    continue
                elif item[0] == "-":
                    # Put it in the albums list and in the dictionary with the name of the artist
                    albums.append(item[2:-2])
                    dictionary[item[2:-2]] = {stuff[:-2]}
                else:
                    # New artist, new value, break the cycle!
                    break
    alb_file.close()

def read_doc (doc):
    document = open(doc, "r")
    for line in document:
        print(line[:-1])
    document.close()


def write_dictionary(dictionary, file_name):
    file = open(file_name, "w")

    #First paragraph determination
    if file_name == "Albums_I_have.txt":
        file.write("These are the albums I have at the moment, 2021: test")
    elif file_name == "Albums_I_wanna_buy.txt":
        file.write("These are the albums I wanna buy:")
    file.write("\n\n")
    artists = []
    albums = []

    for artist in dictionary.values():
        #If the artist was writen, ingore
        if artist in artists:
            continue
        else:
            #Write the paragraph for the artist
            #Adds the artist to the artits list so this condition wont verify again
            artists.append(artist)
            file.write("\n" + str(artist)[2:-2] + ":\n")

        for album, value in dictionary.items():
            #if the album belongs to the artist and not in albums, write it down
            if album in albums:
                continue
            elif value == artist:
                file.write("- " + album + ";\n")
                albums.append(album)
    file.close()


def solta_o_som_DJ():
    bar = "\ "
    secret1 = str(os.getcwd()) + bar[:1] + "Include" + bar[:1] + "Nothing_to_se_here" + bar[:1] + "I_wan_to_break_free.txt"
    secret2 = str(os.getcwd()) + bar[:1] + "Include" + bar[:1] + "Nothing_to_se_here" + bar[:1] + "Queen - I Want To Break Free.mp3"

    #Give a hint
    copyfile(secret1,"I_wan_to_break_free.txt" )
    copyfile(secret2,"Queen - I Want To Break Free.mp3")

    read_doc("I_wan_to_break_free.txt")
    playsound("Queen - I Want To Break Free.mp3", 0)

    #Delete them
    os.remove(str(os.getcwd()) + bar[:1] + "I_wan_to_break_free.txt")
    os.remove(str(os.getcwd()) + bar[:1] + "Queen - I Want To Break Free.mp3")


