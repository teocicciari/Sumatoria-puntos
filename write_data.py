# -*- coding: utf-8 -*-
import os

def merge_data(player_list, player_dict):
	new_list = []
	try:
		cant_t = len(player_list[0][1])
	except:
		cant_t = 0

	for player in player_list:
		print(player_dict)
		print(player_list)
		name = player[0]
		print(name)
		pts_list = player[1]
		try:
			pts = player_dict.pop(name)
			pts_list.append(pts)
		except:
			pts_list.append(0)
		s = sum(pts_list)
		new_list.append((name, pts_list, s))
	
	for key, value in player_dict.items():
		name = key
		pts_list = []
		for i in range(0, cant_t):
			pts_list.append(0)
		pts_list.append(value)
		s = sum(pts_list)
		new_list.append((name, pts_list, s))
		
	return(new_list)

def write_sumatoria(player_list):
    os.rename("sumatoria", "sumatoria.bak")

    with open("sumatoria", "w") as file:
        for player in player_list:
            file.write("{0} - ".format(player[0]))
            for e in player[1]:
                file.write("{0} - ".format(e))
            file.write("{0}\n".format(player[2]))