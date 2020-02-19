# -*- coding: utf-8 -*-
import re

def read_sumatoria():
    with open("sumatoria", "r") as file:
        players = []

        for line in file.readlines():
            try:
                pts_list = []
                player = line.split(' - ')
                name = player.pop(0)
                player.pop(-1)
                for p in player:
                    pts_list.append(float(p))
                players.append((name, pts_list))
            except Exception as e:
                print(e)

    return(players)

def read_players_pts(text, tourn_type):
    '''
    Read players and his points
    '''

    player_dict = {}
    num_lines = sum(1 for line in text)

    for line in range(9, num_lines):
        player = text[line]
        name = player[13:36].rstrip()
        if tourn_type == 's':
            pts = player[-9:-6]
        else:
            pts = player[-16:-13]
        pts = float(re.sub('½','.5', pts))

        player_dict[name] = pts

    for key, value in player_dict.items():
        print(key +' '+ str(value))

    return(player_dict)

def read_tournament(text):
    '''
    Read the info of the tournament
    '''
    nameT = text[0].rstrip()
    organizator = text[2][31:].rstrip()
    eloMed = text[3][31:35].rstrip()
    date = text[4][31:42].rstrip()

    if (text[8][45:50] == "1.Rd."):
        type_T = "s"
    else:
        type_T = "a"

    return(nameT, date, organizator, eloMed, type_T)


def read_file(filename):
    with open(filename, "r") as file:
        text = file.readlines()
    
    return(text)

def check_file(text):
    '''
    Check that the input file have the right format
    '''

    patterns = ['Organizador', 'Elo medio', 'Fecha', '', 'Clasificación Final', '', 'Rank']
    cErrors = 0

    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')
    print("CHECKEAR FORMATO:")
    print('...')

    for i in range(7):
        if not (re.search(patterns[i], text[i+2])):
            cErrors = cErrors+1
            print("pattern: ", patterns[i])
            print("file: ", text[i+2])

    if (cErrors != 0):
        print('Errores encontrados en el formato: ', cErrors)
        print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')

    else:
        print('Formato de archivo OK!')
        print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')