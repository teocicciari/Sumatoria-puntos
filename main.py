from read_data import *
from write_data import *
import sys

def main():

    # Getting the info from the tournament
    filename = input("Nombre del archivo de input: ")
    text = read_file(filename)
    check_file(text)

    player_list = read_sumatoria()
    print(player_list)
    tournament = read_tournament(text)
    player_dict = read_players_pts(text, tournament[4])
    player_list = merge_data(player_list, player_dict)
    print(player_list)
    write_sumatoria(player_list)
    
if __name__== "__main__":
	main()