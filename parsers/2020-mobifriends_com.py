import collections
from parsers import base


class Parse(base.Parser):
    """
        MobiFriends.com breach data parser
        Source File SHA-1: 3944a67b7375bc15437db8d0c3812eedf7070673  mobifriends-users.sql
        Good Lines: 3,640,926
    """

    name = "None"
    web = "mobifriends.com"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            Sample:
                (801,   'amelie',   '30fae425f2aae929053643e717a114c6', 'iolax68@hotmail.com',  0,  '1970-07-20',   '2008-11-15
                00:44:15',  NULL,   '08201',    40713,  8,  73, 1,  '609204568',    4,  '2010-03-30 19:20:24',  1,  0,  1,  1)
            
            :param r:
            :return:
        """

        row = r.split(',')
        email = row[3].replace('\'', '').strip()
        pw_hash = row[2].replace('\'', '').strip()
        domain = email.split('@')[1] if '@' in email else ''
        #print(f"{email},{pw_hash},{domain}")

        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)
