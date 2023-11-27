import collections
from parsers import base


class Parse(base.Parser):
    """
        magicduel.com 2023 breach data parser
        Source File SHA-1: c4407d573d6b3dc5ab3331d2c28d5a245e6a3401  MagicalDuel_EP_Dehash.txt
        Good Lines: 109,111
    """

    name = "None"
    web = "magicduel.com"
    year = "2023"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                007dunlop@fsmail.net:nathan

           email,password

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
