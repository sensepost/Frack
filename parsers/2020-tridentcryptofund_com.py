import collections
from parsers import base


class Parse(base.Parser):
    """
        tridentep.com 2020 breach data parser
        Source File SHA-1: 0cf4fc830234dce6027753787b264912c8cf30ee  Trident_EP_Dehash.txt
        Good Lines: 182,262
    """

    name = "None"
    web = "tridentcryptofund.com"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                happyending0801@gmail.com:Happyending1225

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
