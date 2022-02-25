import collections
from parsers import base


class Parse(base.Parser):
    """
        Bigbasket.com breach data parser
        Source File SHA-1: a4dd21b5ca4e98c82417262f82957005de2db637 bb.sql
        Good Lines: 20,489,857
    """

    name = "None"
    web = "www.bigbasket.com"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            Sample:
            (1,'2011-11-02 17:54:40','2020-02-06 16:00:19',NULL,5508,'prshanth.py@gmail.com',
            'sha1$b6f84$1b2b6a277dff95df33a5176fcc2faab419589d1f','Prashanth','Vijayendra','1985-02-25',
            '',0,0,0,'2019-08-01 13:46:49','127.0.0.1','49.206.14.56','2011-11-02 17:54:40',11,
            'Shamanna Lane,Church road',560017,_binary '\0\0\0\0\0\0\0\�\��iS@#ƫ�\�)@','',NULL,
            'ALREADY_ACTIVATED1','83592',0,NULL,'No:33,Flat No:006,Arrcons Agna Indraprasta','bangalore'
            ,1,1,'Murugeshpalya',0,612,'612','prshanthpy@gmail.com','','no33flatno006arrconsagnaindraprastashamannalanechurchroad'
            ,0,1,'MzE0OTkyNTYxNQ==',45,NULL,'',NULL,'',1,'A-DX-XBO-95998165-14','2012-09-05','2019-10-14',51,'BBO-52794-030912'
            ,5323.43,80349.96,807,793,76213.00,79361.40,5323.00,2420,2435,'gmail.com',59.97,9506.56,NULL,5634.33,'2019-10-02'
            ,NULL,'2014-04-13',0.00,1,NULL,'prshanth.py@gmail.com',NULL,NULL,NULL,NULL)
            
            :param r:
            :return:
        """

        row = r.split(',')

        email = row[5].replace('\'', '').strip()
        pw_hash = row[6].replace('\'', '').strip()
        domain = email.split('@')[1] if '@' in email else ''
        #print(f"{email},{pw_hash},{domain}")

        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                if not row.startswith(r"INSERT INTO `member_member` VALUES"):
                    continue
                
                if len(row.split('VALUES')) != 2:
                    print("x", end='')
                    continue

                _, values = row.split('VALUES')
                inserts = values.split(r'),(')

                for value_tuple in inserts:
                    yield self.row_format(value_tuple)
