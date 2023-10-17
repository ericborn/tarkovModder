# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:14:22 2023

@author: Eric
"""
import os
import json
import shutil

def load_json(file_path):
    item_file = open(file_path, 'r', encoding='utf8')
    item_data = json.loads(item_file.read())
    item_file.close()
    return item_data

def save_json(item_data, file_path):
    json_obj = json.dumps(item_data, indent=4)
    with open(file_path, 'w') as outfile:
        outfile.write(json_obj)
    outfile.close()

install_drive = 'C:/'
eft_version = 'eft 3.7.1/'

base_file_name = 'base.json'
case_id = '5795f317245977243854e041'
prapor_id = '54cb50c76803fa8b248b4571'
bag_parent = '5448e53e4bdc2d60728b4567'
key_parent = '5c99f98d86f7745c314214b3'
rig_parent = '5448e5284bdc2dcb718b4567'
mag_parent = '5448bc234bdc2d3c308b4569'
ammo_parent = '5485a8684bdc2da71d8b4567'
key_tool_id = '59fafd4b86f7745ca07e1232'
therapist_id = '54cb57776803fa99248b456e'
medical_parent = '5448f39d4bdc2d0a728b4568'
headwear_parent = '5a341c4086f77401f2541505'
body_armor_parent = '5448e54d4bdc2dcc718b4568'
armored_equipment_parent = '57bef4c42459772e8d35a53b'

mod_trader_img_path = 'C:/Users/Eric/Desktop/eft/mods/traders/'
bot_path = install_drive + eft_version + 'Aki_Data/Server/configs/bot.json'
map_path = install_drive + eft_version + 'Aki_Data/Server/database/locations/'
trader_path = install_drive + eft_version + 'Aki_Data/Server/database/traders/'
trader_img_path = install_drive + eft_version + 'Aki_Data/Server/images/traders/'
ragfair_path = install_drive + eft_version + 'Aki_Data/Server/configs/ragfair.json'
global_path = install_drive + eft_version + 'Aki_Data/Server/database/globals.json'
location_path = install_drive + eft_version + 'Aki_Data/Server/configs/location.json'
quest_config_path = install_drive + eft_version + 'Aki_Data/Server/configs/quest.json'
insurance_path = install_drive + eft_version + 'Aki_Data/Server/configs/insurance.json'
item_path = install_drive + eft_version + 'Aki_Data/Server/database/templates/items.json'
quest_path = install_drive + eft_version + 'Aki_Data/Server/database/templates/quests.json'
bear_bot_path = install_drive + eft_version + 'Aki_Data/Server/database/bots/types/bear.json'
usec_bot_path = install_drive + eft_version + 'Aki_Data/Server/database/bots/types/usec.json'
hideout_areas_path = install_drive + eft_version + 'Aki_Data/Server/database/hideout/areas.json'
hideout_workout_path = install_drive + eft_version + 'Aki_Data/Server/database/hideout/qte.json'
hideout_settings_path = install_drive + eft_version + 'Aki_Data/Server/database/hideout/settings.json'
hideout_scav_case_path = install_drive + eft_version + 'Aki_Data/Server/database/hideout/scavcase.json'
hideout_production_path = install_drive + eft_version + 'Aki_Data/Server/database/hideout/production.json'
prapor_path = trader_path + prapor_id + '/' + base_file_name
therapist_path = trader_path + therapist_id + '/' + base_file_name

bot_data = load_json(bot_path)
item_data = load_json(item_path)
quest_data = load_json(quest_path)
global_data = load_json(global_path)
bear_data = load_json(bear_bot_path)
usec_data = load_json(usec_bot_path)
prapor_data = load_json(prapor_path)
ragfair_data = load_json(ragfair_path)
location_data = load_json(location_path)
therapist_data = load_json(therapist_path)
insurance_data = load_json(insurance_path)
quest_config_data = load_json(quest_config_path)
hideout_areas_data = load_json(hideout_areas_path)
hideout_workout_data = load_json(hideout_workout_path) 
hideout_settings_data = load_json(hideout_settings_path)
hideout_scav_case_data = load_json(hideout_scav_case_path)
hideout_production_data = load_json(hideout_production_path)

# money list
money_list = ['5449016a4bdc2d6f028b456f', '5696686a4bdc2da3298b456a',
              '569668774bdc2da2298b4568']

# secure containers
container_list = ['544a11ac4bdc2d470e8b456a', '5857a8b324597729ab0a0e7d',
                  '59db794186f77448bc595262', '5857a8bc2459772bad15db29',
                  '5c093ca986f7740a1867ab12']

# car, Salewa, grizzly, IFAK, AI-2, AFAK, sanitar ifak
med_kit_ids = ['590c661e86f7741e566b646a', '544fb45d4bdc2dee738b4568',
               '590c657e86f77412b013051d', '5755356824597772cb798962',
               '590c678286f77426c9660122', '60098ad7c2240c0fe85c570a',
               '5e99711486f7744bfc4af328']

# bleed, surg kits, pain meds
other_med_ids = ['5751a25924597722c463c472', '5d02778e86f774203e7dedbe', 
                 '5d02797c86f774203f38e30a', '5e8488fa988a8701445df1e4',
                 '5af0548586f7743a532b7e99', '5af0454c86f7746bf20992e8']

bag_keys = []
key_keys = []
rig_keys = []
mag_keys = []
ammo_keys = []
case_keys = []
armor_keys = []
helmet_keys = []
armored_equipment_keys = []
all_keys = list(item_data.keys())

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
    
    # bags
    if item_data[key]['_parent'] == bag_parent:
       bag_keys.append(key)
    
    # keys
    if item_data[key]['_parent'] == key_parent:
       key_keys.append(key)
    
    # mags
    if item_data[key]['_parent'] == mag_parent:
       mag_keys.append(key)
        
    # ammo
    if item_data[key]['_parent'] == ammo_parent:
        ammo_keys.append(key)
        
    # containers
    if item_data[key]['_parent'] == case_id:
        case_keys.append(key)

# all items to mod durability     
mod_keys = armor_keys + rig_keys + helmet_keys + armored_equipment_keys

# mags max ammo
for key in mag_keys:
    try:
        item_data[key]['_props']['Cartridges'][0]['_max_count'] /= 1.5
    except:
        pass
    
# bags
for bags in bag_keys:
    item_data[bags]['_props']['Grids'][0]['_props']['cellsH'] -= 2
    item_data[bags]['_props']['Grids'][0]['_props']['cellsV'] -= 2

# secure containers
for container in container_list:
    item_data[container]['_props']['Grids'][0]['_props']['cellsH'] -= 2
    item_data[container]['_props']['Grids'][0]['_props']['cellsV'] -= 2

# cases
for case in case_keys:
    item_data[case]['_props']['Grids'][0]['_props']['cellsH'] -= 2
    item_data[case]['_props']['Grids'][0]['_props']['cellsV'] -= 2

# inertia changes
global_data['config']['Stamina']['FallDamageMultiplier'] /= 0.25

# default {'x': -3, 'y': -2, 'z': 0}
global_data['config']['Stamina']['OverweightConsumptionByPose']['x'] /= 0.5
global_data['config']['Stamina']['OverweightConsumptionByPose']['y'] /= 0.5

global_data['config']['Stamina']['ProneConsumption'] /= 0.5

global_data['config']['Stamina']['SitToStandConsumption'] /= 0.5
global_data['config']['Stamina']['SprintDrainRate'] /= 0.5
global_data['config']['Stamina']['SprintOverweightLimits']['x'] /= 1.25
global_data['config']['Stamina']['SprintOverweightLimits']['y'] /= 1.25
global_data['config']['Stamina']['StandupConsumption']['x'] /= 0.5
global_data['config']['Stamina']['StandupConsumption']['y'] /= 0.5

inertia_multi = 0.6

# default 0.15
global_data['config']['Inertia']['MinDirectionBlendTime'] /= inertia_multi

# default "x": 0.05, "y": 0.4675
global_data['config']['Inertia']['WalkInertia']['x'] /= inertia_multi
global_data['config']['Inertia']['WalkInertia']['y'] /= inertia_multi

# 0.3
global_data['config']['Inertia']['BaseJumpPenalty'] /= inertia_multi

# 0.4
global_data['config']['Inertia']['BaseJumpPenaltyDuration'] /= inertia_multi

# 'x': 4
global_data['config']['Inertia']['SpeedLimitAfterFallMax']['x'] /= inertia_multi

# default  {'x': 0, 'y': 55, 'z': 0}
global_data['config']['Inertia']['SprintBrakeInertia']['y'] /= inertia_multi

# tilt is inverted where a larger number is faster/less inertia effect
# 'x': 0.6, 'y': 0.5
global_data['config']['Inertia']['TiltInertiaMaxSpeed']['x'] /= 1.3
global_data['config']['Inertia']['TiltInertiaMaxSpeed']['y'] /= 1.3

# 'x': 1.2, 'y': 0.8
global_data['config']['Inertia']['TiltMaxSideBackSpeed']['x'] /= 1.3
global_data['config']['Inertia']['TiltMaxSideBackSpeed']['y'] /= 1.3

# 'x': 0.8, 'y': 0.5
global_data['config']['Inertia']['TiltStartSideBackSpeed']['x'] /= 1.3
global_data['config']['Inertia']['TiltStartSideBackSpeed']['y'] /= 1.3

# med items
for med in other_med_ids:
    item_data[med]['_props']['MaxHpResource'] /= 10
    
# Adjust weight of all items
weight_modifier = 0.35
for key in all_keys:
    try:
        item_data[key]['_props']['Weight'] /= weight_modifier
    except:
        pass
    
# gpu bonus for bitcoin farm
for area in hideout_areas_data:
    if area['_id'] == '5d494a445b56502f18c98a10':
        for key in area['stages'].keys():
            if area['stages'][key]['bonuses']:
                if area['stages'][key]['bonuses'][0]['filter'][0] == '57347ca924597744596b4e71':
                    area['stages'][key]['bonuses'][0]['value'] -= 10   
    for key in area['stages'].keys():
        area['stages'][key]['constructionTime'] = 1
        
# scav case
for scav in range(0, len(hideout_scav_case_data)):
    hideout_scav_case_data[scav]['ProductionTime'] = 1800
    for product in hideout_scav_case_data[scav]['EndProducts']:
        min_value = int(hideout_scav_case_data[scav]['EndProducts'][product]['min'])
        min_value += 1
        
        max_value = int(hideout_scav_case_data[scav]['EndProducts'][product]['max'])
        max_value += 1
        
        hideout_scav_case_data[scav]['EndProducts'][product]['min'] = str(min_value)
        hideout_scav_case_data[scav]['EndProducts'][product]['max'] = str(max_value)
        
# loot modifiers
for loot in location_data['looseLootMultiplier']:
    location_data['looseLootMultiplier'][loot] /= 2

for loot in location_data['staticLootMultiplier']:
    location_data['staticLootMultiplier'][loot] /= 2

folder_list = os.listdir(map_path)
remove_list = ['develop','hideout','privatearea','suburbs','terminal',
               'town','base.json']

for items in remove_list:
    folder_list.remove(items)
    
for folder in folder_list:
    full_path = map_path + folder + '/' + base_file_name
    map_data = load_json(full_path)
    
    map_data['EscapeTimeLimit'] /= 2
    map_data['BotStop'] /= 2
    map_data['GlobalContainerChanceModifier'] /= 2
    map_data['GlobalLootChanceModifier'] /= 2
    
save_json(bot_data, bot_path)
save_json(item_data, item_path)
save_json(quest_data, quest_path)
save_json(prapor_data, prapor_path)
save_json(global_data, global_path)
save_json(bear_data, bear_bot_path)
save_json(usec_data, usec_bot_path)
save_json(ragfair_data, ragfair_path)
save_json(location_data, location_path)
save_json(therapist_data, therapist_path)
save_json(insurance_data, insurance_path)
save_json(quest_config_data, quest_config_path)
save_json(hideout_areas_data, hideout_areas_path)
save_json(hideout_workout_data, hideout_workout_path)
save_json(hideout_settings_data, hideout_settings_path)
save_json(hideout_scav_case_data, hideout_scav_case_path)
save_json(hideout_production_data, hideout_production_path)
