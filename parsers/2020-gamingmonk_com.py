import collections
from parsers import base


class Parse(base.Parser):
    """
        gamingmonk.com 2020 breach data parser
        Source File SHA-1: ea97b90c817d7d2532370c294002ec66b62de033  GaminhMonk_EP_Dehash.txt
        Good Lines: 9,574
    """

    name = "None"
    web = "gamingmonk.com"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                007mwnswrangwary@gmail.com:007iammwnswrang

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
                # Fix GMail Alias Usage
                # Eg: gloria.a.z.u123@gmail.com:Golden2017
                

                yield self.row_format(row)
