# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:36:08 2023

@author: Eric
"""

import json
import os

health_mod_amount = 3

#############
# mod bots
#############
file_path = 'G:/eft 13-5-1/EFT/Aki_Data/Server/database/bots/types/'
file_list = os.listdir(file_path)

for files in file_list:
    file = open(file_path+files, 'r', encoding='utf8')
    data = json.loads(file.read())
    
    for bodyParts in data['health']['BodyParts'][0]:
        data['health']['BodyParts'][0][bodyParts]['min'] *= health_mod_amount
        data['health']['BodyParts'][0][bodyParts]['max'] *= health_mod_amount
        
    json_obj = json.dumps(data, indent=4)
    
    with open(file_path+files, 'w') as outfile:
        outfile.write(json_obj)
        
    file.close()  
    outfile.close()
    
#############
# only works for new profiles
#############
player_file_path = 'G:/eft 13-5-1/EFT/Aki_Data/Server/database/globals.json'
player_file = open(player_file_path, 'r', encoding='utf8')

player_data = json.loads(player_file.read())

for bodyParts in player_data['config']['Health']['ProfileHealthSettings']['BodyPartsSettings']:
    player_data['config']['Health']['ProfileHealthSettings']['BodyPartsSettings'][bodyParts]['Maximum'] *= health_mod_amount

    player_data['config']['Health']['ProfileHealthSettings']['BodyPartsSettings'][bodyParts]['Default'] *= health_mod_amount
    
player_json_obj = json.dumps(player_data, indent=4)

with open(player_file_path, 'w') as player_outfile:
    player_outfile.write(player_json_obj)
    
player_file.close()  
player_outfile.close()

#############
# mod existing profiles
#############
player_profile_path = 'G:/eft 13-5-1/EFT/user/profiles/'
profile_list = os.listdir(player_profile_path)

for profiles in profile_list:
    profile = open(player_profile_path+profiles, 'r', encoding='utf8')
    profile_data = json.loads(profile.read())
    
    for body_part in profile_data['characters']['pmc']['Health']['BodyParts']:
        profile_data['characters']['pmc']['Health']['BodyParts'][body_part]['Health']['Current'] *= health_mod_amount
        profile_data['characters']['pmc']['Health']['BodyParts'][body_part]['Health']['Maximum'] *= health_mod_amount
        
    json_obj = json.dumps(profile_data, indent=4)
    
    with open(player_profile_path+profiles, 'w') as outfile:
        outfile.write(json_obj)
        
    profile.close()  
    outfile.close()

