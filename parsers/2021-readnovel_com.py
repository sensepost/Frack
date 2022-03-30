import collections

from parsers import base


class Parse(base.Parser):
    """
        readnovel.com breach data parser
        Source File SHA-1: ec6c014b17096592994cbb82c502d5b8b9694f0f  Readnovel.com_Dehash.txt
        Good Lines: 10,908,803
    """

    name = "None"
    web = "readnovel.com"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                -vatrushka-@ukr.net:-vatrushka-:240386
                .d.y.n.c.lyday@gmail.com:OxitruscurrizAl:u7n6Pby6kH

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        row = r.split(':')

        if len(row) == 3:
            email = row[1]
            try:
                domain = row[1].split('@')[1]
            except:
                domain = ''
            password = row[2].strip()
        else:
            email = domain = password = ''
        
        #print(f'{email}:{password}')

        return self.name, self.web, int(self.year), domain, email, password, '', ''

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)
