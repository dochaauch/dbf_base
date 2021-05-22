#год валюты в одну фирму 50 евро
#в шестерке обратный курс
import dbf
import csv


number_val = 'V  220'
table = dbf.Table('/Users/docha/PycharmProjects/dbf_base/1/1SBCONS.DBF', codepage= 'cp866')
FILENAME = 'History.csv'

with open(FILENAME, "r", newline="", encoding='utf-8') as file:
    readerS = csv.reader(file, delimiter=';')
    valuta = {}
    next(readerS)
    for row in readerS:
        valuta['constype'] = 'K'
        valuta['consno'] = ''
        valuta['consname'] = number_val+row[0][6:8] +row[0][3:5]+row[0][0:2]
        valuta['consval'] = str(round(float(row[2]),4))

        #print(valuta)


        table.open(mode=dbf.READ_WRITE)
        table.append(valuta)
#
# table.append({'constype': 'K',
#               'consno': '',
#               'consname': 'V  220200421',
#               'consval': '0.8889',
#               'constype': 'K',
#               'consno': '',
#               'consname': 'V  220200422',
#               'consval': '0.9999',
#               })




for item in table:
     print(item)





#
#
# Writing data to records can be accomplished in a few different ways:
#
# using the record as a context manager:
#
# with table[0] as rec:
#      rec.name = "changed"
# using the dbf.Process function to deal with several records in a loop:
#
# for rec in Process(my_table):
#      rec.name = rec.name.title()
# using the write function in the dbf module:
#
# dbf.write(some_record, name='My New Name')
# I did it this way to enhance both safety and performance.

# dbf.write(table[0],name="changed")
#
# #!/usr/bin/python
#
# import dbf
# db = dbf.Table('MEST2.DBF')
# with db:
#     procod_idx = db.create_index(lambda rec: (rec.codigo, rec.procod))
#     match = procod_idx.search(match=(11, '000001'))
#     record = match[0]
#     with record:
#         record.proest = 25
#         record.dt_atualiz = '14/07/15 16:52'