from dbfread import DBF
import os
from icecream import ic
from datetime import datetime
import time
import collections



def time_format():
    return f'{datetime.now()}|> '


ic.configureOutput(prefix=time_format, includeContext=True)


def find_needed_doc(str):
    #example:
    #record['CONSNAME'].startswith('D    1')
    expected_table = ['1SBCONS.DBF']
    if l in expected_table:
        if (record['CONSNAME'].startswith(str)):
            #and (record['CONSVAL']):
            return record


def show_doc_structure(rec):
    rec = dict()
    # D  4182 3Оклад       1 11.2 0      3x  6
    # 3Оклад       1 =>№, наименование, тип
    # 1-число,2-текст, 3-дата, 4-субконто
    # 11.2 0  =>дл 11, .2 точн, 0 экр
    # 3x  6 => копировать из рек 3, пропуск при коп х, пор.6
    #
    # doc_vid: 1-шапка, 2-таблица, 3-инф.табло, 6-комментарий
    # doc_type: 1 число, 2 текст, 3 дата, 4 субконто, 5 счет, 6 валюта
    # doc_check: только цифра - №субконто, ЗН|21 - субконто из знач21

    #'CONSNAME', 'D    12 4сумма       1  6.2 0      0   4'), ('CONSVAL', '"1 Вывод документа"; "2 Вывод документа"')
    #'CONSNAME', 'D0000120401'), ('CONSVAL', '; "3 Вывод документа"; "4 Вывод документ')
    try:
        rec['doc_vid'] = int(record['CONSNAME'][6:7])
        rec['doc_nr'] = int(record['CONSNAME'][7:9])
        rec['doc_name'] = record['CONSNAME'][9:21]
        rec['doc_type'] = record['CONSNAME'][21:23]
        rec['doc_length'] = record['CONSNAME'][23:25]
        rec['doc_toch'] = record['CONSNAME'][25:27]
        rec['doc_ekr'] = record['CONSNAME'][27:29]
        rec['doc_check'] = record['CONSNAME'][29:34]
        rec['doc_copy'] = record['CONSNAME'][34:36]
        rec['doc_prop1'] = record['CONSNAME'][36:37]
        rec['doc_prop2'] = record['CONSNAME'][37:38]
        rec['doc_poz'] = int(record['CONSNAME'][38:40])
    except:
        rec['doc_poz'] = 0
        rec['doc_nr'] = 0
    return rec



def find_all_docs():
    #example
    #OrderedDict([('CONSTYPE', 'I'), ('CONSNO', '  418'), ('CONSNAME', '6.0. Tootasu: Maksude kinnitamine 15Soom'),
    # ('CONSVAL', 'TSD.15kinni\\tsd2018.gfd           6')])
    expected_table = ['1SBCONS.DBF']
    if l in expected_table:
        if (record['CONSTYPE'] == 'I'):
            return record





func_flag = 2


#path_for_base = '/Dropbox/1C_Soome/Soome/'
path_for_base = '/1SBW6/leer/'
record_dict = dict()


list_db = [_ for _ in os.listdir(rf'/Volumes/[C] Windows 10/{path_for_base}')
           if (_.endswith('.dbf')) or (_.endswith('.DBF'))]
for l in list_db:
    base_flag = 0
    if base_flag == 1:
        print()
        print('*** new ***')
        print(l)

    path_ = f'/Volumes/*Windows 10/{path_for_base}{l}'




    table = DBF(path_, encoding='cp866')


    exception_list = ['1SBSVPR.DBF', '1SBGLKN.DBF']


    for record in table:
        if func_flag == 1:  # распечатать список всех документов
            if find_all_docs():
                print(find_all_docs())

        if func_flag == 2:

            #  ('CONSNO', '  418') номер документа берем из списка 1 =>
            # 'D  418', 'D00418', в n вводим только этот номер
            n = 1
            nr1 = 'D' + str(n).rjust(5)
            nr2 = 'D' + str(n).rjust(5, '0')
            nr3 = 'RF' + str(n).rjust(6, '0')
            # if ((find_needed_doc(nr1) or find_needed_doc(nr2))
            #         and record['CONSVAL']):
            if find_needed_doc(nr1) or find_needed_doc(nr2):
                if find_needed_doc(nr1):
                    rec_value = record['CONSVAL']
                    d_pos = show_doc_structure(record)['doc_poz']
                    d_nr = show_doc_structure(record)['doc_nr']
                    d_vid = show_doc_structure(record_dict)['doc_vid']
                    d_name = show_doc_structure(record_dict)['doc_name']
                    d_key = d_vid, d_pos, d_nr
                    record_dict[d_key] = [d_name, rec_value]
                if find_needed_doc(nr2):
                    d_nr = int(record['CONSNAME'][7:9])
                    d_vid = int(record['CONSNAME'][6])
                    for k in record_dict.keys():
                        if d_vid == k[0] and d_nr == k[2]:
                            rec_value = record_dict.get(k)[1] + record['CONSVAL']
                            record_dict[k] = [record_dict.get(k)[0], rec_value]




        if func_flag == 3:
            if l not in exception_list:
                print(record)

if func_flag == 2:
    out1 = ''
    od = collections.OrderedDict(sorted(record_dict.items()))
    for k, v in od.items():
        out = f'{k}: {v}' +'\r'
        out1 += out
    #ic(out1)
    v = open(f'/Volumes/[C] Windows 10/{path_for_base}out.txt', 'w')
    v.write(out1)
    v.close()
    #print(out1)





