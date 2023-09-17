# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 17:51:56 2023

@author: Eric
"""

import json

def load_json(file_path):
    item_file = open(file_path, 'r', encoding='utf8')
    item_data = json.loads(item_file.read())
    item_file.close()
    return item_data

global_path = 'G:/eft 13-5-1/EFT/Aki_Data/Server/database/globals.json'
item_path = 'G:/eft 13-5-1/EFT/Aki_Data/Server/database/templates/items.json'
bear_bot_path = 'G:/eft 13-5-1/EFT/Aki_Data/Server/database/bots/types/bear.json'
usec_bot_path = 'G:/eft 13-5-1/EFT/Aki_Data/Server/database/bots/types/usec.json'
hideout_areas_path = 'G:/eft 13-5-1/EFT/Aki_Data/Server/database/hideout/areas.json'
hideout_settings_path = 'G:/eft 13-5-1/EFT/Aki_Data/Server/database/hideout/settings.json'
hideout_production_path = 'G:/eft 13-5-1/EFT/Aki_Data/Server/database/hideout/production.json'

item_data = load_json(item_path)
global_data = load_json(global_path)
bear_data = load_json(bear_bot_path)
usec_data = load_json(usec_bot_path)
hideout_areas_data = load_json(hideout_areas_path)
hideout_settings_data = load_json(hideout_settings_path)
hideout_production_data = load_json(hideout_production_path)

body_armor_parent = '5448e54d4bdc2dcc718b4568'
rig_parent = '5448e5284bdc2dcb718b4567'
headwear_parent = '5a341c4086f77401f2541505'
armored_equipment_parent = '57bef4c42459772e8d35a53b'
mag_parent = '5448bc234bdc2d3c308b4569'
medical_parent = '5448f39d4bdc2d0a728b4568'
ammo_parent = '5485a8684bdc2da71d8b4567'

# car, Salewa, grizzly, IFAK, AI-2, AFAK, sanitar ifak
med_kit_ids = ['590c661e86f7741e566b646a', '544fb45d4bdc2dee738b4568',
               '590c657e86f77412b013051d', '5755356824597772cb798962',
               '590c678286f77426c9660122', '60098ad7c2240c0fe85c570a',
               '5e99711486f7744bfc4af328']

armor_keys = []
rig_keys = []
helmet_keys = []
armored_equipment_keys = []
mag_keys = []
ammo_keys = []
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
    
    # mags
    if item_data[key]['_parent'] == mag_parent:
       mag_keys.append(key)
        
    # ammo
    if item_data[key]['_parent'] == ammo_parent:
        ammo_keys.append(key)

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

###
# health items mods
###
def mod_med_item(item_id, max_uses, hp_recovery_rate, stim_buff=''):
    item_data[item_id]['_props']['MaxHpResource'] = max_uses
    item_data[item_id]['_props']['hpResourceRate'] = hp_recovery_rate
    item_data[item_id]['_props']['StimulatorBuffs'] = stim_buff

# car, Salewa, grizzly, AI-2, IFAK, AFAK, sanitar ifak
mod_med_item(med_kit_ids[0], 20, 0, 'BuffsCarKit')
mod_med_item(med_kit_ids[1], 30, 0, 'BuffsSalewa')
mod_med_item(med_kit_ids[2], 60, 0, 'BuffsGrizzly')
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

###
# ammo adjusts
###
# distinct_ammo = []
# for key in ammo_keys:
#     distinct_ammo.append(item_data[key]['_props']['StackMaxSize'])

# distinct_ammo = set(distinct_ammo)

for key in ammo_keys:
    if item_data[key]['_props']['StackMaxSize'] in [15, 20]:
        item_data[key]['_props']['StackMaxSize'] = 100
    if item_data[key]['_props']['StackMaxSize'] in [30, 40, 50, 70]:
        item_data[key]['_props']['StackMaxSize'] = 300

# Adjust weight of all items
weight_modifier = 0.35
for key in all_keys:
    try:
        item_data[key]['_props']['Weight'] *= weight_modifier
    except:
        pass
####
# hideout
####
# smaller is better
# 'generatorFuelFlowRate': 0.001319444444444,
# 'airFilterUnitFlowRate': 0.004722222222222,
# larger is better
# 'gpuBoostRate': 0.041225
hideout_settings_data['generatorFuelFlowRate'] *= 0.25
hideout_settings_data['airFilterUnitFlowRate'] *= 0.25
hideout_settings_data['gpuBoostRate'] = 0.09

# set construction of any hideout areas to 1
for area in hideout_areas_data:
    for key in area['stages'].keys():
        area['stages'][key]['constructionTime'] = 1

# set production of all items to 1 
for items in hideout_production_data:
    items['productionTime'] = 1

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

##########
# save and close files
##########
def save_json(item_data, file_path):
    
    json_obj = json.dumps(item_data, indent=4)
    
    with open(file_path, 'w') as outfile:
        outfile.write(json_obj)
 
    outfile.close()

save_json(item_data, item_path)
save_json(global_data, global_path)
save_json(bear_data, bear_bot_path)
save_json(usec_data, usec_bot_path)
save_json(hideout_areas_data, hideout_areas_path)
save_json(hideout_settings_data, hideout_settings_path)
save_json(hideout_production_data, hideout_production_path)