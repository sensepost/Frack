import collections
from parsers import base


class Parse(base.Parser):
    """
        yahoo.com breach data parser
        Source File SHA-1: 54a19fb48d6e04564c60788b951041d0ee9c8e7d  2012-Yahoo.com_77kk.txt
        Good Lines: 76,420,481
    """

    name = "None"
    web = "yahoo.com"
    year = "2012"

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

    def process_rows(self) -> collections.abc.Iterable[tuple]:
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
