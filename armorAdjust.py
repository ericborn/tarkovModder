# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 17:51:56 2023

@author: Eric
"""

import json
import math

item_file_path = 'G:/eft 13-5-1/EFT/Aki_Data/Server/database/templates/items.json'
item_file = open(item_file_path, 'r', encoding='utf8')
item_data = json.loads(item_file.read())

global_file_path = 'G:/eft 13-5-1/EFT/Aki_Data/Server/database/globals.json'
global_file = open(global_file_path, 'r', encoding='utf8')
global_data = json.loads(global_file.read())

durability_adjustment = 3

body_armor_parent = '5448e54d4bdc2dcc718b4568'
rig_parent = '5448e5284bdc2dcb718b4567'
headwear_parent = '5a341c4086f77401f2541505'
armored_equipment_parent = '57bef4c42459772e8d35a53b'
mag_parent = '5448bc234bdc2d3c308b4569'
medical_parent = '5448f39d4bdc2d0a728b4568'
ammo_parent = '5485a8684bdc2da71d8b4567'

# grizzly, AFAK, Car, IFAK, AI-2, Salewa, sanitar ifak
med_kit_ids = ['590c657e86f77412b013051d', '60098ad7c2240c0fe85c570a', \
               '590c661e86f7741e566b646a', '590c678286f77426c9660122', \
               '5755356824597772cb798962', '544fb45d4bdc2dee738b4568', \
               '5e99711486f7744bfc4af328']

armor_keys = []
rig_keys = []
helmet_keys = []
armored_equipment_keys = []
mag_keys = []
ammo_keys = []

for key in item_data.keys():
    # armor
    if item_data[key]['_parent'] == body_armor_parent:
        armor_keys.append(key)
    if item_data[key]['_parent'] == rig_parent and \
        item_data[key]['_props']['MaxDurability'] > 0:
        rig_keys.append(key)
    if item_data[key]['_parent'] == headwear_parent and \
        item_data[key]['_props']['MaxDurability'] > 0 and \
        item_data[key]['_props']['ArmorType'] != 'None':
       helmet_keys.append(key)
    if item_data[key]['_parent'] == armored_equipment_parent:
        armored_equipment_keys.append(key)
    
    # mags
    if item_data[key]['_parent'] == mag_parent:
        ammo_keys.append(key)
        
    # ammo
    if item_data[key]['_parent'] == ammo_parent:
        mag_keys.append(key)

# all items to mod durability     
mod_keys = armor_keys + rig_keys + helmet_keys + armored_equipment_keys

# multiply all durabilities
for key in mod_keys:
    try:
        item_data[key]['_props']['Durability'] *= durability_adjustment 
        item_data[key]['_props']['MaxDurability'] *= durability_adjustment 
    except:
        pass

# created to rollback making all mag loading speed 
# positive when it should've been negative
# original_values = {}
# for key in mag_keys:
#     try:
#         original_values[item_data[key]['_id']] = item_data[key]['_props']['LoadUnloadModifier']
#     except:
#         pass

# for key in original_values:
#     item_data[key]['_props']['LoadUnloadModifier'] = original_values[key]


# fixed range adjustments
# negative values increase loading speed
# need to figure out the formula for diminishing returns
for key in mag_keys:
    try:
        if item_data[key]['_props']['LoadUnloadModifier'] >= 0:
            item_data[key]['_props']['LoadUnloadModifier'] = -20
        if item_data[key]['_props']['LoadUnloadModifier'] <= -1 and \
            item_data[key]['_props']['LoadUnloadModifier']>= -15:
                item_data[key]['_props']['LoadUnloadModifier'] = -35
        if item_data[key]['_props']['LoadUnloadModifier'] <= -16:
            item_data[key]['_props']['LoadUnloadModifier'] = -45
    except:
        pass

# TODO
# isn't working how I want it to, too extreme at 1 and not extreme
# enough at 100, also needs to set modifier as a negative number
# function for exponential decay to decrease the gain
# as the base modifier increases
# a = starting value
# r = decay rate
# x = total operations
# def exp_decay(a, r, x):
#     f = a*(1-r)**x
#     return(f)

# starting_amount = 0.75
# decay_rate = 0.1

# print(exp_decay(0.75, 0.1, 1)*100)
# print(exp_decay(1, 0.1, value_100)*100)

# print(exp_decay(value_1, 0.1, 5))
# print(exp_decay(value_100, 0.1, 5))

# probably easier to just set the stats 
# manually per item since there are only 5
# order of the list
def mod_med_item(item_id, max_uses, hp_recovery_rate, stim_buff=''):
    item_data[item_id]['_props']['MaxHpResource'] = max_uses
    item_data[key]['_props']['hpResourceRate'] = hp_recovery_rate
    item_data[key]['_props']['StimulatorBuffs'] = stim_buff


def add_med_buff(buff_name, duration, heal_amt):
    global_data['config']['Health']['Effects']['Stimulator']['Buffs'][buff_name] = [{
                                                                                        "AbsoluteValue": "true",
                                                                                        "BuffType": "HealthRate",
                                                                                        "Chance": 1,
                                                                                        "Delay": 1,
                                                                                        "Duration": duration,
                                                                                        "SkillName": "",
                                                                                        "Value": heal_amt
                                                                                    }] 
add_med_buff('BuffsGrizzly', 600, 20)
add_med_buff('BuffsSalewa', 300, 10)
add_med_buff('BuffsCarKit', 300, 5)
################

# ammo adjusts

"StackMaxSize": 50

##########
# save and close files
##########
def save_json(item_data, open_file, file_path):
    
    json_obj = json.dumps(item_data, indent=4)
    
    with open(file_path, 'w') as outfile:
        outfile.write(json_obj)
    
    open_file.close()  
    outfile.close()
    
save_json(item_data, item_file, item_file_path)
save_json(global_data, global_file, global_file_path)