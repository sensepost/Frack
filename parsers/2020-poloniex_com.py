import collections
from parsers import base


class Parse(base.Parser):
    """
        A poloniex.com breach data parser
        Source File SHA-1: 8cbbfe5731878aa7a5ee8902dca81ef9c42c77f8  Poloniex.com_950k.txt
        Good Lines: 951,400
    """

    name = "None"
    web = "poloniex.com"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                kriistel@web.de:chucks2310

           email,password

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

        #print(email + ':' + password)

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
