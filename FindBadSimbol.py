from dbfread import DBF


#в выводе найти в ручную обратный слэш \

table = DBF('/Users/docha/Desktop/Alistron2011 2/1SBSPSK.DBF', encoding='cp866')
            #encoding='cp866')



for record in table:
    if record['SCHSKKOD'] =='   11':
            #and record['SPSKNO']=='  261':
        a = [ord(char) for char in record['SPSKIM']]
        for element in a:

            if not 31 <= element <= 261 and not 1040 <= element <= 1104:
                
                print(element)
                print(record)
                print(record['SCHSKKOD'], record['SPSKUP'], record['SPSKNO'], record['SPSKIM'],
              str(record['SPSKIM']), record['SPSKIM'].encode('ascii', errors='ignore'))


