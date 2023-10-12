import collections
from parsers import base


class Parse(base.Parser):
    """
        firmart.de breach data parser
        Source File SHA-1: 0e340a0ec68737bd2493e40529b25131d9204100
        Good Lines: 214,489
    """

    name = "None"
    web = "firmart.de"
    year = "2023"

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

        # print(email + ":" + password)

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
