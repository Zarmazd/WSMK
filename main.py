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
    'Ammo used': '9x17mm(or .380 ACP)',
    'Base attack': 45,
    'Supplies': 5,
    rarity: common
}
metaunits_dict[str(unit_dict_key)] = unit_dict
unit_dict_key += 1
unit_dict = {
     'Name': 'Mars Auto .36',
     'Type': 'Pistol',
     'Ammo used': '.360 Mars',
     'Base attack': 52, 
     'Supplies': 7,
     rarity: rare
}
metaunits_dict[str(unit_dict_key)] = unit_dict
unit_dict_key += 1
unit_dict = {
     'Name': 'FN Grand', 
     'Type': 'Pistol',
     'Ammo used': '9.65x23mm Browning',
     'Base attack': 48,
     'Supplies': 6,
     rarity: epic
}
metaunits_dict[str(unit_dict_key)] = unit_dict
unit_dict_key += 1
unit_dict = {
     'Name': 'MP 3008',
     'Type': 'Submachine gun',
     'Ammo used': '9x19 Para', 
     'Base attack': 35,
     'Supplies': 9,
     rarity: rare
}
metaunits_dict[str(unit_dict_key)] = unit_dict
common = 'Common'
rare = 'Rare'
epic = 'Epic'
units = []
units.append('CZ38')
units.append('Mars Auto .36')
units.append('FN Grand')
arsenal_dict = {}
arsenal_dict[0] = 'CZ38'
def showarsenal():
    for a in arsenal_dict:
        print(a, '-', arsenal_dict[a])
    whichtoget = input('If you want to see a detailed information, type in the key.')
    weapon_being_shown = arsenal_dict[int(whichtoget)]
    for usedkey in metaunits_dict:
        shown = False
        if shown is False:
            dwo = metaunits_dict[usedkey]
            if dwo['Name'] == weapon_being_shown:
                msk = 0
                print('')
                shown = True
                for a in dwo:
                msk += 1
                if msk <= 6;
                     print(a, '-', dwo[a])
                else:
                     break
        vsm = input('If you want to return to the main menu, type 1. If you want to return to the arsenal, print 2.')
        if vsm == '1':
            showms()
        elif vsm == '2':
            showarsenal()
        break
def showms():
    print('')
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
def showbuild():
