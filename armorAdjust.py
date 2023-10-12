# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 17:51:56 2023

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

install_drive = 'G:/'
eft_version = '3.7.0/'

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

map_path = install_drive + eft_version + 'Aki_Data/Server/database/locations/'
trader_path = install_drive + eft_version + 'Aki_Data/Server/database/traders/'
trader_img_path = install_drive + eft_version + 'Aki_Data/Server/images/traders/'
mod_trader_img_path = 'C:/Users/Eric/Desktop/eft/mods/traders/'
ragfair_path = install_drive + eft_version + 'Aki_Data/Server/configs/ragfair.json'
global_path = install_drive + eft_version + 'Aki_Data/Server/database/globals.json'
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

item_data = load_json(item_path)
quest_data = load_json(quest_path)
global_data = load_json(global_path)
bear_data = load_json(bear_bot_path)
usec_data = load_json(usec_bot_path)
prapor_data = load_json(prapor_path)
ragfair_data = load_json(ragfair_path)
therapist_data = load_json(therapist_path)
insurance_data = load_json(insurance_path)
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

# multiply all durabilities
# durability_adjustment = 3
# for key in mod_keys:
#     try:
#         item_data[key]['_props']['Durability'] *= durability_adjustment 
#         item_data[key]['_props']['MaxDurability'] *= durability_adjustment 
#     except:
#         pass

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

###
# mag reloading changes
###
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

# cut base load/unload times in half
# default 0.85 and 0.3
global_data['config']['BaseLoadTime'] *= 0.75
global_data['config']['BaseUnloadTime'] *= 0.75

# adjust max number of flea offers to 100 from -10000 to 10000 rep
global_data['config']['RagFair']['maxActiveOfferCount'][0]['count'] = 100
global_data['config']['RagFair']['maxActiveOfferCount'][0]['to'] = 10000

# larger money stack size
for money in money_list:
    item_data[money]['_props']['StackMaxSize'] = 999999

# expand bags
for bags in bag_keys:
    item_data[bags]['_props']['Grids'][0]['_props']['cellsH'] += 2
    item_data[bags]['_props']['Grids'][0]['_props']['cellsV'] += 2

# expand secure containers
for container in container_list:
    item_data[container]['_props']['Grids'][0]['_props']['cellsH'] += 2
    item_data[container]['_props']['Grids'][0]['_props']['cellsV'] += 2
    
    item_data[container]['_props']['Grids'][0]['_props']['filters'] = []

# expand cases
# make all cases 2x2 larger and remove item filter
for case in case_keys:
    item_data[case]['_props']['Grids'][0]['_props']['cellsH'] += 2
    item_data[case]['_props']['Grids'][0]['_props']['cellsV'] += 2
    
    item_data[case]['_props']['Grids'][0]['_props']['filters'] = []

# manually set the keytool to be 6x6
# item_data[key_tool_id]['_props']['Grids'][0]['_props']['cellsH'] = 6
# item_data[key_tool_id]['_props']['Grids'][0]['_props']['cellsV'] = 6

# set all keys to unlimited uses
for key in key_keys:
    item_data[key]['_props']['MaximumNumberOfUsage'] = 0

###
# stamina/inertia changes
###

# shouldn't need adjusting due to changes to all item weight
# global_data['config']['Stamina']['BaseOverweightLimits']['x']
# global_data['config']['Stamina']['BaseOverweightLimits']['y']
# global_data['config']['Stamina']['BaseOverweightLimits']['z']

# stamina changes
# default {'x': 0.17, 'y': 0.7, 'z': 0}
global_data['config']['Stamina']['CrouchConsumption']['x'] = 0.1
global_data['config']['Stamina']['CrouchConsumption']['y'] = 0.3

global_data['config']['Stamina']['FallDamageMultiplier'] *= 0.25

# default {'x': -3, 'y': -2, 'z': 0}
global_data['config']['Stamina']['OverweightConsumptionByPose']['x'] *= 0.5
global_data['config']['Stamina']['OverweightConsumptionByPose']['y'] *= 0.5

global_data['config']['Stamina']['ProneConsumption'] *= 0.5

global_data['config']['Stamina']['SitToStandConsumption'] *= 0.5
global_data['config']['Stamina']['SprintDrainRate'] *= 0.5
global_data['config']['Stamina']['SprintOverweightLimits']['x'] *= 1.25
global_data['config']['Stamina']['SprintOverweightLimits']['y'] *= 1.25
global_data['config']['Stamina']['StandupConsumption']['x'] *= 0.5
global_data['config']['Stamina']['StandupConsumption']['y'] *= 0.5

# inertia changes
inertia_multi = 0.6

# 'SideTime': {'x': 2, 'y': 1, 'z': 0}
global_data['config']['Inertia']['SideTime']['x'] = 0.0
global_data['config']['Inertia']['SideTime']['y'] = 0.0

# default "x": 0.1, "y": 0.45
global_data['config']['Inertia']['MoveTimeRange']['x'] = 0
global_data['config']['Inertia']['MoveTimeRange']['y'] = 0

# default 0.15
global_data['config']['Inertia']['MinDirectionBlendTime'] *= inertia_multi

# default "x": 0.05, "y": 0.4675
global_data['config']['Inertia']['WalkInertia']['x'] *= inertia_multi
global_data['config']['Inertia']['WalkInertia']['y'] *= inertia_multi

# 0.3
global_data['config']['Inertia']['BaseJumpPenalty'] *= inertia_multi

# 0.4
global_data['config']['Inertia']['BaseJumpPenaltyDuration'] *= inertia_multi

# 'x': 4
global_data['config']['Inertia']['SpeedLimitAfterFallMax']['x'] *= inertia_multi

# default  {'x': 0, 'y': 55, 'z': 0}
global_data['config']['Inertia']['SprintBrakeInertia']['y'] *= inertia_multi

# tilt is inverted where a larger number is faster/less inertia effect
# 'x': 0.6, 'y': 0.5
global_data['config']['Inertia']['TiltInertiaMaxSpeed']['x'] *= 1.3
global_data['config']['Inertia']['TiltInertiaMaxSpeed']['y'] *= 1.3

# 'x': 1.2, 'y': 0.8
global_data['config']['Inertia']['TiltMaxSideBackSpeed']['x'] *= 1.3
global_data['config']['Inertia']['TiltMaxSideBackSpeed']['y'] *= 1.3

# 'x': 0.8, 'y': 0.5
global_data['config']['Inertia']['TiltStartSideBackSpeed']['x'] *= 1.3
global_data['config']['Inertia']['TiltStartSideBackSpeed']['y'] *= 1.3

# {'x': 0, 'y': 65, 'z': 0.5}
# global_data['config']['Inertia']['InertiaLimits']['y'] = 65
# global_data['config']['Inertia']['InertiaLimits']['z'] = 0.5

#######
# XP changes
#######
global_data['config']['WeaponSkillProgressRate'] = 2
global_data['config']['SkillsSettings']['WeaponSkillProgressRate'] = 2

# xp for door breach/unlock
global_data['config']['exp']['expForLockedDoorBreach'] = 100
global_data['config']['exp']['expForLockedDoorOpen'] = 100

# I think this increases loot exp on subsequent items, no idea
global_data['config']['exp']['loot_attempts'][1] = {'k_exp': 0.5}
global_data['config']['exp']['loot_attempts'][2] = {'k_exp': 0.5}

# increase xp for a headshot kill
global_data['config']['exp']['kill']['pmcHeadShotMult'] = 1.75

# reduce distance needed to be considered a longshot
global_data['config']['exp']['kill']['longShotDistance'] = 25

# increase xp at the end of match for different outcomes
# lower requirements for survived status to 10 xp or 60 seconds
global_data['config']['exp']['match_end']['killedMult'] = 1.5

global_data['config']['exp']['match_end']['miaMult'] = 1.5
global_data['config']['exp']['match_end']['mia_exp_reward'] = 500

global_data['config']['exp']['match_end']['runnerMult'] = 1.5
global_data['config']['exp']['match_end']['runner_exp_reward'] = 500

global_data['config']['exp']['match_end']['survivedMult'] = 2
global_data['config']['exp']['match_end']['survived_exp_requirement'] = 10
global_data['config']['exp']['match_end']['survived_exp_reward'] = 1000
global_data['config']['exp']['match_end']['survived_seconds_requirement'] = 60

#######
# repair durability costs
#######
global_data['config']['RepairSettings']['durabilityPointCostArmor'] = 0.05
global_data['config']['RepairSettings']['durabilityPointdurabilityPointCostGunsCostArmor'] = 0.05

#######
# health items mods
#######
def mod_med_item(item_id, max_uses, hp_recovery_rate, stim_buff=''):
    item_data[item_id]['_props']['MaxHpResource'] = max_uses
    item_data[item_id]['_props']['hpResourceRate'] = hp_recovery_rate
    item_data[item_id]['_props']['StimulatorBuffs'] = stim_buff

# car, Salewa, grizzly, AI-2, IFAK, AFAK, sanitar ifak
mod_med_item(med_kit_ids[0], 30, 0, 'BuffsCarKit')
mod_med_item(med_kit_ids[1], 50, 0, 'BuffsSalewa')
mod_med_item(med_kit_ids[2], 100, 0, 'BuffsGrizzly')
mod_med_item(med_kit_ids[3], 500, 125)
mod_med_item(med_kit_ids[4], 1250, 175)
mod_med_item(med_kit_ids[5], 2000, 225)
mod_med_item(med_kit_ids[6], 2000, 225)

# item_data[med_kit_ids[3]]['_props']

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

add_med_buff('BuffsCarKit', 300, 5)
add_med_buff('BuffsSalewa', 300, 10)
add_med_buff('BuffsGrizzly', 600, 20)

for med in other_med_ids:
    item_data[med]['_props']['MaxHpResource'] *= 10

###
# ammo adjusts
###
# distinct_ammo = []
# for key in ammo_keys:
#     distinct_ammo.append(item_data[key]['_props']['StackMaxSize'])

# distinct_ammo = set(distinct_ammo)

for key in ammo_keys:
    # set all ammo max stack to 600
    item_data[key]['_props']['StackMaxSize'] = 600
    
    # set max ammo stack by ammo type
    # if item_data[key]['_props']['StackMaxSize'] in [15, 20]:
    #     item_data[key]['_props']['StackMaxSize'] = 100
    # if item_data[key]['_props']['StackMaxSize'] in [30, 40, 50, 70]:
    #     item_data[key]['_props']['StackMaxSize'] = 300


# Adjust weight of all items
weight_modifier = 0.35
for key in all_keys:
    try:
        item_data[key]['_props']['Weight'] *= weight_modifier
    except:
        pass
####
# buy/sell all items on flea
####
for item in item_data:
    item_data[item]['_props']['CanSellOnRagfair'] = True
    item_data[item]['_props']['CanRequireOnRagfair'] = True

ragfair_data['sell']['simulatedSellHours'] = 1
ragfair_data['sell']['chance']['base'] = 100
ragfair_data['sell']['chance']['overpriced'] = 3
ragfair_data['sell']['chance']['underpriced'] = 3
ragfair_data['sell']['time']['base'] = 0.1
ragfair_data['sell']['time']['max'] = 0.1

ragfair_data['dynamic']['purchasesAreFoundInRaid'] = True
ragfair_data['dynamic']['blacklist']['enableBsgList'] = False
ragfair_data['dynamic']['offerAdjustment']['adjustPriceWhenBelowHandbookPrice'] = True
ragfair_data['dynamic']['offerAdjustment']['maxPriceDifferenceBelowHandbookPercent'] = 0.01
ragfair_data['dynamic']['offerAdjustment']['handbookPriceMultipier'] = 5
ragfair_data['dynamic']['offerAdjustment']['priceThreshholdRub'] = 999999

####
# hideout
####
# smaller is better
# 'generatorFuelFlowRate': 0.001319444444444,
# 'airFilterUnitFlowRate': 0.004722222222222,
# larger is better
# 'gpuBoostRate': 0.041225
hideout_settings_data['generatorFuelFlowRate'] *= 0.5
hideout_settings_data['airFilterUnitFlowRate'] *= 0.5
hideout_settings_data['gpuBoostRate'] = 0.041225

# set construction of any hideout areas to 1
# iterate through areas looking for bitcoin farm id 5d494a445b56502f18c98a10
# iterate through stages of the farm looking for bonus attributes with
# a filter for the graphics card id 57347ca924597744596b4e71
# multiply the bonus by 10
for area in hideout_areas_data:
    if area['_id'] == '5d494a445b56502f18c98a10':
        for key in area['stages'].keys():
            if area['stages'][key]['bonuses']:
                if area['stages'][key]['bonuses'][0]['filter'][0] == '57347ca924597744596b4e71':
                    area['stages'][key]['bonuses'][0]['value'] += 10   
    for key in area['stages'].keys():
        area['stages'][key]['constructionTime'] = 1

# set production of all items to 1 
for items in hideout_production_data:
    items['productionTime'] = 1

# set workout speed and success range to the same values for each stage    
for workout in range(0, len(hideout_workout_data[0]['quickTimeEvents'])):
    hideout_workout_data[0]['quickTimeEvents'][workout]['successRange'] = {'x': 0.50, 'y': 0.15}
    hideout_workout_data[0]['quickTimeEvents'][workout]['speed'] = 2

# set all scav case runs to 30 min
# add 1 extra min and max products for common, rare and super rare
# values stored as a string in the json so conversion between types was needed
for scav in range(0, len(hideout_scav_case_data)):
    hideout_scav_case_data[scav]['ProductionTime'] = 1800
    for product in hideout_scav_case_data[scav]['EndProducts']:
        min_value = int(hideout_scav_case_data[scav]['EndProducts'][product]['min'])
        min_value += 1
        
        max_value = int(hideout_scav_case_data[scav]['EndProducts'][product]['max'])
        max_value += 1
        
        hideout_scav_case_data[scav]['EndProducts'][product]['min'] = str(min_value)
        hideout_scav_case_data[scav]['EndProducts'][product]['max'] = str(max_value)

####
# insurance changes
####
insurance_data['insuranceMultiplier'][prapor_id] = 0.15
insurance_data['insuranceMultiplier'][therapist_id] = 0.15

insurance_data['returnChancePercent'][prapor_id] = 0.95
insurance_data['returnChancePercent'][therapist_id] = 0.95
insurance_data['runIntervalSeconds'] = 60

prapor_data['insurance']['min_return_hour'] = 0
prapor_data['insurance']['max_return_hour'] = 0
prapor_data['insurance']['max_storage_time'] = 666
therapist_data['insurance']['min_return_hour'] = 0
therapist_data['insurance']['max_return_hour'] = 0
therapist_data['insurance']['max_storage_time'] = 666

####
# bot name changes
####

bear_name_list = ["15NUNDR","1STLINE","1V1IRL","2RETSGUY","360NSCP","5FNGRS",
                  "6969DKS","90S E","AGATHA","ALINWRE","ALXFACE","ANOOSE1",
                  "ARYNBNZ","ASS2MTH","ASSPLAY","AZNPSSY","BABYDCK","BALDRIK",
                  "BALHAIR","BALLPIT","BALLPLY","BEATOFF","BIRDUP","BLCKFCE",
                  "BLDWALL","BLKFMTR","BLL5GTS","BLPITSPK","BLWDUDES","BOITKLR",
                  "BOYBTTR","BOYLOVE","BRD1ST","BRNJWS","BRNTJEW","BRSTMLK",
                  "BUTTCHG","BYOCV19","CAMPR","CARADIN","CHNAVRS","CLPTRP",
                  "COCKSOX","COKENRG","COKERNG","COKLIFE","COKNWAY","COSBYD",
                  "CUMDUMP","CUMGUZL","CUMONME","CV19FUN","DADFCKR","DCKBERD",
                  "DCKCHCK","DCKHOLE","DCKNAIR","DCKPLS","DEZNUTZ","DIDLER",
                  "DIKCHSE","DOALINE","DOBABYS","DRAGQUN","DRTYVAG","DWNSHFT",
                  "EATSEED","EGLEYE6","EMEPAR","F4GSLYR","FATLINE","FCKDADS",
                  "FCKLKY","FCKTRMP","FLPYHAT","FNCEJMP","FNGRBST","FNGRME",
                  "FNGTRP","FTFJ247","FTFJ314","FTFJ365","GAGER69","GASCHBR",
                  "GAY4GOD","GAY4PAY","GAYFUEL","GITIKLD","GNKFERY","GOHMMEX",
                  "GOOFBLS","GOTKIDS","GOTPPR","GOTRAIL","GOTTOES","GRBPSSY",
                  "GRINDER","GRLAFNGR","GTDIDLD","GTRKDM8","GTTKLD","GTTKLED",
                  "H8BLCKS","HARDAF","HARDDIK","HEILHLR","HIPPYBS","HOGFEST",
                  "HOGFTHR","HOGMSTR","HRAMBE","HVCNDY","HWIBCOL","I(HEART)COKE",
                  "I(HEART)DRGS","I(HEART)ISIS","I(HEART)SLVS","IDOBLOW",
                  "IDOGUYS","IDOKIDS","IFKSLNTS","IH8GAYS","ISQUIRT","JELORPE",
                  "JEWBTCH","JEWSTAR","JEWTITS","JPJESUS","JSTREKX","KIDTKLR",
                  "KINDR","KLANKAR","KLANVAN","KUMLORD","LADYBOY","LINESFJ",
                  "LOTLZRD","LSD4ME","LTITHPN","MANLOVE","MDMABCH","MEATSPN",
                  "MSLMBAN","MSTRACE","MTHDOUT","NEDMEAT","NEEDRPE","NGGRDCK",
                  "NI69GR","NIGAFAG","NMBRSEC","NOGIRLS","NOMASKS","NOWIHRD",
                  "NZISTBL","OHCHUM","OLDPEDO","PAULWKR","PEPCOCK","PEWPEWW",
                  "PLANDMC","PLLCSBY","PNTMSTR","POPPERS","POUNDME","PSHROPE",
                  "PUTNCRTN","PWRBFST","PWRBTTM","RAILME","RCKGRME","RDNBIDN",
                  "SANDNGR","SANSBSH","SCKDADS","SHOOTER","SHTYBDY","SLKDADY",
                  "SNDBULL","SNDITM8","SPUNKME","STEPDON","STMPYRD","STROKIT",
                  "SWALWS","SWTYBLS","TBRODY","TEARBAG","TENSILE","TKLMSTR",
                  "TNKTNK","TOTS4ME","TRAPBAR","TRE50TY","TREKLLR","TRIGGRD",
                  "TROLL","TYRODND","UMADBRO","UNCLJON","USERVE","UWUTM8",
                  "VAXCHIP","WALMRT5","WARNI","WHTCLAW","WHTPWR","WHTRGHT",
                  "WIZZBNG","WOOLLEG"]

usec_name_list = ["12YoSoaking","2Dudes1Butt","2DudesCuddling","2DudesSoaking",
                  "2YOAbortions","AbdulPussigap","Aborted12YO","AbortedLimbs",
                  "AbortYourTeen","aCowboysHeavyLoad","AllBeefWienerThief",
                  "AmeerAnaland","AnalAlpha","AnalAndy","AnalOmega",
                  "AngelHairMilfs","AssAssassin","assclampsncables",
                  "AuschwitzLarry","BabyHooker","BabyOilSprinkler","bagofagtits",
                  "Ballsdeep Invagina","BaronVonNiggerSnatch",
                  "beefcurtainfacemask","BigTireLips","bloodystoolsample",
                  "BloodyVag","bonerpills","bonerwind","BoofingBarbarian",
                  "boofroof","BootyBarbarian","BradyBunchBangBus",
                  "BrokeBackWetback","buttchopshop","ButterCreamDream",
                  "ChumBucket","ChumLee","coronatits","Cowboy3Way","CowboyDocking",
                  "CowboyNutJuice","CowboyNutMilk","CreekWaterSock","DadsBangingDads",
                  "DankBowels","DavidGobbleDicks","DeepSpaceDominican","deepStink",
                  "DeerCockWaterSock","DickPickles","DoorDashDildo","DoTheNeedful",
                  "DunlopLips","DynastyAssMaster","FagetFighter","fagetflounder",
                  "FatGrannyTits","FatTits","FillMeUpBottomCup","FillMeUpCowboy",
                  "FillMeWithCowboyLoads","FirestoneLips","FoolOfAGook",
                  "ForeskinSharPei","GagMeGrandpa","gat5cables","gayassnicknolte",
                  "gayassovertime","gaymechanics","GoodyearLips","GrampaThickFinger",
                  "grandpa'sfuckingdad","GrandPappysLappy","GrandpasGigglestick",
                  "GranpasGospelPipe","GrindrGearGayms","growsomeballs","handoffthegay",
                  "hotholes","InEachOther","JackFags","KeepinItBeefy","kriskilsonklan",
                  "LibsKillBabies","LooseCabooseAnoose","LSDSoakTrain","lvl99PwrBottom",
                  "lvl99RoidBottom","lvl99RoidMage","MammyThickFinger","MaPaMenageATrois",
                  "MeatMage","MeemawsMeatPocket","MeemawsMeatSock","MeemawsMerkin",
                  "MeemawsMustache","memawsmeatcliff","MexicansGetAbortions","MichelinLips",
                  "moistorpedo","MomsDirtyCarpet","MomsIntoGayDads","MotorcycleJesus",
                  "mrmonoclejesuspeanut","MuffMage","muffslammer69","mustybutts",
                  "mustysluts","myDADbangsDUDES","NiggerLipsPapa","NoseSprayGirlfriend",
                  "NotGayWithBros","notmypope","numbersecond","OutHouseHandy",
                  "PapaTickleStick","PaypalPoon","PipeSquasher","postgamecoitus",
                  "PR0lap5e","PR0lapse","ProlapsePapa","ProstateBoxer","PunjabBallsdeep",
                  "QueenSexPot","RamenTilapia","rapejayleno","RapeRogue","Rebups4Rape",
                  "Repubs4BabyRape","RepubsLike2Rape","rollcoal","SammyPickles",
                  "SlowFagBangerz","snowconeoverride","SoakingBedBounce","SoggyFupa",
                  "SoundingOldMen","sourstingraybuttblast","SSealant",
                  "StartedFromTheBottomNowImQueer","TamponBill","thatsdoughnuts",
                  "thx4servants","TioPepesChurro","toetikler","TotallyNotGay",
                  "TuBerculos1s2","VagrantNegrosSoftlySuckingAssholes",
                  "VenomousNarcsSellingSweetAmphetamines",
                  "VeryNiggardySexSwingsAdvertisements","VNSSAsofficialcunt",
                  "WangWarrior","WhiteClawAndCocaine","WhiteLineHighway",
                  "WienerWizard","YourDadsFuckToy","VagabonDuneCoon",
                  "antiqueboner","StevenHonkings","RainwaterCrank",
                  "SubsandwichDocking","BulgingTrashSack","fucksandwich",
                  "urinewhore","fuckglove","AfricanSimilac","DoubleAbort",
                  "BloatoFaggins","CondomStrike","trannyhosefest","gthinomath",
                  "hookemdano","KenyanBreastmilk","TransgenderApe","bostonshotgun"]

bear_data['firstName'] = bear_name_list
usec_data['firstName'] = usec_name_list

########
# map changes
########
folder_list = os.listdir(map_path)
remove_list = ['develop','hideout','privatearea','suburbs','terminal',
               'town','base.json']

for items in remove_list:
    folder_list.remove(items)

for folder in folder_list:
    full_path = map_path + folder + '/' + base_file_name
    map_data = load_json(full_path)
    
    map_data['EscapeTimeLimit'] *= 2
    map_data['MinDistToExitPoint'] = 1
    map_data['MinDistToFreePoint'] = 1
    map_data['BotStop'] *= 2
    map_data['GlobalContainerChanceModifier'] *= 2
    map_data['GlobalLootChanceModifier'] *= 2
    
    for exits in range(0,len(map_data['exits'])):
        map_data['exits'][exits]['Chance'] = 100
        
    save_json(map_data, full_path)

###
# quest changes
###
# remove wait time until quest can be started
for quest in quest_data:
    try:
        if quest_data[quest]['conditions']['AvailableForStart'][0]['_parent'] == 'Quest':
            quest_data[quest]['conditions']['AvailableForStart'][0]['_props']['availableAfter'] = 0
    except:
        pass

##########
# save and close files
##########
save_json(item_data, item_path)
save_json(quest_data, quest_path)
save_json(prapor_data, prapor_path)
save_json(global_data, global_path)
save_json(bear_data, bear_bot_path)
save_json(usec_data, usec_bot_path)
save_json(ragfair_data, ragfair_path)
save_json(therapist_data, therapist_path)
save_json(insurance_data, insurance_path)
save_json(hideout_areas_data, hideout_areas_path)
save_json(hideout_workout_data, hideout_workout_path)
save_json(hideout_settings_data, hideout_settings_path)
save_json(hideout_scav_case_data, hideout_scav_case_path)
save_json(hideout_production_data, hideout_production_path)

#####
# replace trader img files
#####
img_list = os.listdir(mod_trader_img_path)

for img in img_list:
    shutil.copy(mod_trader_img_path+img, trader_img_path+img)