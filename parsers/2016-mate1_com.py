import collections
from parsers import base


class Parse(base.Parser):
    """
        Mate1.com breach data parser
        Source File SHA-1: 9544484fa88dcc6652e5503c0e5296ac7191e39c  2016-Mate1.com_27.5kk.txt
        Good Lines: 27,337,079
    """

    name = "None"
    web = "Mate1.com"
    year = "2016"

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
