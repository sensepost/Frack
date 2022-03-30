import collections
from parsers import base


class Parse(base.Parser):
    """
        000Webhost.com breach data parser
        Source File SHA-1: afa1decf087a48eef4adf8f554baf1cbcbbb580c  2015-000webhost.com_14.8kk.txt
        Good Lines: 14,803,311
    """

    name = "None"
    web = "000Webhost.com"
    year = "2015"

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
