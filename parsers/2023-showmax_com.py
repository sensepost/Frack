import collections
from parsers import base


class Parse(base.Parser):
    """
        A showmax.com breach data parser
        Source File SHA-1: eb96fd5740691fc3fe5fd8b1c05f4896ea757f53 showmax_28k_parsed.txt
        Good Lines: 27428
    """

    name = "None"
    web = "showmax.com"
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
