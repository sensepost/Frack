import collections
from parsers import base


class Parse(base.Parser):
    """
        MyHeritage.com breach data parser
        Source File SHA-1: fd925fc97dde636c2097ca23e4e59a567e4f006d  2017-Myheritage.com_81kk.txt | e3a149b563695ce0bcbf31e02266156bb04b1f97  2017-MyHeritage.com_23kk.txt
        Good Lines: 81,544,618 | 
    """

    name = "None"
    web = "MyHeritage.com"
    year = "2017"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                kriistel@web.de:chucks2310

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(':')

        email = row[0]
        domain = row[0].split('@')[1] if '@' in email else ''
        password = row[1].strip()

        return self.name, self.web, int(self.year), domain, email, password, '', ''

    def process_rows(self) -> collections.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue
                    
                if len(row.split(':')) != 2:
                    continue

                yield self.row_format(row)
