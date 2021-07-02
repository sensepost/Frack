from parsers import base
import collections


class Parse(base.Parser):
    """
        Wedmegood.com 2021 breach data parser
        Source File SHA-1: 7f218df16c31449354ffae70d2cf63e174bbfd45  wedmegood_symfony-PROD.backup_Jan_06_21_06-30.sql
        Good Lines: 446,672
    """

    name = "None"
    web = "wedmegood.com"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            Sample: 
                [' (7', "'yogesh.sahni@live.in'", "'yogesh.sahni@live.in'", "'yogesh.sahni@live.in'", "'yogesh.sahni@live.in'", '1',
                 'NULL', "'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'",
                 'NULL', 'NULL', 'NULL', '\'a:1:{i:0;s:9:\\"ROLE_USER\\";}\'', "'yogesh--7'", 'NULL', 'NULL', 'NULL', "'2018-06-22 06:49:22'", 'NULL', 'NULL', 
                 '0', "'0000-00-00 00:00:00'", '0', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', '0', 'NULL', '0', '0', 'NULL', 'NULL', 'NULL']

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(',')
        email = ''

        if '@' in row[1]:
            email = row[1].replace('\'', '').strip()
        elif '@' in row[2]:
            email = row[2].replace('\'', '').strip()
        elif '@' in row[3]:
            email = row[3].replace('\'', '').strip()
        elif '@' in row[4]:
            email = row[4].replace('\'', '').strip()
        pw_hash = row[7].replace('\'', '').strip()
        domain = email.split('@')[1] if '@' in email else ''

        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue
                if not row.startswith(r"INSERT INTO `member`"):
                    continue

                _, values = row.split('VALUES')
                inserts = values.split(r'),(')

                for value_tuple in inserts:
                    yield self.row_format(value_tuple)