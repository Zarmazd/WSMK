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
    'unit_name': 'CZ38',
    'unit_type': 'Pistol',
    'unit_ammo': '9x17mm - .380 ACP',
    'unit_base-attack': 45,
    'unit_expense': 5
}
metaunits_dict[unit_dict_key] = unit_dict

units = []
arsenal_dict = {}
arsenal_dict[0] = 'CZ38'
def showarsenal():
    for a in arsenal_dict.keys:
        print(a, arsenal_dict[a])
    whichtoget = input('If you want to see a detailed information, type in the key.')
    for
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
