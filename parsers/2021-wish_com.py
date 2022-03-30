import collections
from parsers import base


class Parse(base.Parser):
    """
        A wish.com breach data parser
        Source File SHA-1: cf475b17a7ed3fee45d17ccb57763c7a5c99ad9d  35k_Wish.com_2021_Stranded.txt
        Good Lines: 35,376
    """

    name = "None"
    web = "wish.com"
    year = "2021"

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
        domain = row[0].split('@')[1]
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

                yield self.row_format(row)
