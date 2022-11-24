TEL_NUMBERS = './tel_numbers.txt'
KOR_LAST_NAMES = './kr_last_name.txt'
KOR_FIRST_NAMES = './kr_first_name.txt'
# contact data format
VERSION = 'VERSION:3.0\n'
BEGIN = 'BEGIN:VCARD\n'
NAME_1 = 'N:' #김;철수;;;
NAME_2 = 'FN:' #철수 김
TEL_TYPE = 'TEL;type=CELL;type=VOICE;type=pref:'
END = 'END:VCARD\n'
 
with open('contact_list.vcf', 'w') as w, open(TEL_NUMBERS, 'r') as r:
    l = [s.strip() for s in r.readlines()]
    for _tel_number in l:
        last = kr_last_data.sample(1).to_string(header=None,index=False)
        first = kr_first_data.sample(1).to_string(header=None,index=False)
        w.write(BEGIN + VERSION + NAME_1 + last + ';' + first + ';;;'
                + '\n' + NAME_2 + first + ' ' + last + '\n' + TEL_TYPE + _tel_number + '\n' + END)