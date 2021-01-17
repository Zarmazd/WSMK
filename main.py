import random
import time
import math

# solely for PyCharm. Won't affect anything.
time.sleep(0.00001)
ajf4evm98f = random.randint(0, 0)
axw0mcw0efm = math.sqrt(16)
# This concludes.

supplies_amount = 2000

metaunits_dict = {}

unit_dict_key = 0
unit_dict = {
    'Name': 'CZ38',
    'Type': 'Pistol',
    'Ammo used': '.380 ACP',
    'Base attack': 45,
    'Capacity': 9,
    'Accuracy': 0.7,
    'Supplies': 5,
    'Rarity': 'Common'
}
metaunits_dict[str(unit_dict_key)] = unit_dict
unit_dict_key += 1
unit_dict = {
    'Name': 'Mars Auto .36',
    'Type': 'Pistol',
    'Ammo used': '.360 Mars',
    'Base attack': 43,
    'Base defense': 6,
    'Capacity': 10,
    'Accuracy': 0.65,
    'Supplies': 7,
    'Rarity': 'Rare'
}
metaunits_dict[str(unit_dict_key)] = unit_dict
unit_dict_key += 1
unit_dict = {
    'Name': 'FN Grand',
    'Type': 'Pistol',
    'Ammo used': '9.65x23mm Browning',
    'Base attack': 48,
    'Base defense': 4,
    'Capacity': 8,
    'Accuracy': 0.7,
    'Supplies': 6,
    'Rarity': 'Epic'
}
metaunits_dict[str(unit_dict_key)] = unit_dict
unit_dict_key += 1
unit_dict = {
    'Name': 'MP-3008',
    'Type': 'Submachine gun',
    'Ammo used': '9x19 Para',
    'Base attack': 35,
    'Base defense': 5,
    'Capacity': 32,
    'Accuracy': 0.4,
    'Supplies': 13,
    'Rarity': 'Rare'
}
metaunits_dict[str(unit_dict_key)] = unit_dict
units = []
units.append('CZ38')
units.append('Mars Auto .36')
units.append('FN Grand')
units.append('MP-3008')
arsenal_dict = {}
arsenal_dict[0] = 'CZ38'


def add_weapon(weapon_name):
    lastkey = 0
    for key in arsenal_dict:
        lastkey = key
    lastkey += 1
    arsenal_dict[lastkey] = weapon_name


add_weapon('Mars Auto .36')
add_weapon('MP-3008')


def showarsenal():
    for a in arsenal_dict:
        print(a, '-', arsenal_dict[a])
    whichtoget = input('If you want to see a detailed information, type in the key. ')
    print('')
    weapon_being_shown = arsenal_dict[int(whichtoget)]
    for key in metaunits_dict:
        dict_being_shown = metaunits_dict[key]
        if dict_being_shown['Name'] == weapon_being_shown:
            for a in dict_being_shown:
                print(a + ':', dict_being_shown[a])
        else:
            pass
    print('')
    wksp = input('If you want to return to the arsenal, print 1. If you want to return to the main screen, print 2.')
    wksp = int(wksp)
    if wksp == 1:
        showarsenal()
    elif wksp == 2:
        showms()
    else:
        print('Unknown code. Returning to the main screen...')
        showms()
def showms():
    print('')
    print('')
    print('Current amount of supplies:', supplies_amount)
    print('To see the arsenal, print 1')
    print('To get to the weapon building facility, print 2')
    actioncommand = int(input())
    if actioncommand == 1:
        showarsenal()
    elif actioncommand == 2:
        showbuild()
    else:
        pass
showms()

# This one is...experimental, probably. Will create a new branch.
#def battlestat_search(unit):
    #for key in metaunits_dict:
        #dict_shown = metaunits_dict[key]
        #if dict_shown['Name'] == unit:
            #for a in dict_shown:

#def shootout1(first, second):


    #for key in metaunits_dict:
        #dict_show =