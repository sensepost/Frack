import collections
from parsers import base


class Parse(base.Parser):
    """
        A eskimi.com breach data parser
        Source File SHA-1: 4d8e13f73ab4c7df3716608f6db9d8f8849531a6  eskimi_dehash.txt
        Good Lines: 41
    """

    name = "None"
    web = "eskimi.com"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                kriistel@web.de:chucks2310

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(':')

        try:
            email = row[0]
            domain = row[0].split('@')[1]
            password = row[1].strip()
        except:
            email = domain = password = ''

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
