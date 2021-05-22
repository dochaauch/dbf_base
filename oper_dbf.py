from dbfread import DBF
import os


def find_doc_with_vyr(str):
    #record['CONSNAME'].startswith('D    1')
    expected_table = ['1SBCONS.DBF']
    if l in expected_table:
        if (record['CONSNAME'].startswith(str)) and (record['CONSVAL']):
            return record


list_db = [_ for _ in os.listdir(r'/Volumes/[C] Windows 10/1SBW6/leer/')
           if (_.endswith('.dbf')) or (_.endswith('.DBF'))]
for l in list_db:
    print()
    print('*** new ***')
    print(l)

    path_ = f'/Volumes/*Windows 10/1SBW6/leer/{l}'



    table = DBF(path_, encoding='cp866')


    exception_list = ['1SBSVPR.DBF', '1SBGLKN.DBF']


    for record in table:
        if l not in exception_list:
            print(record)
            #print(find_doc_with_vyr('D    1'))





