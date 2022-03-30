import collections
from parsers import base


class Parse(base.Parser):
    """
        A Jefit.com 2020 breach data parser
        Source File SHA-1: 93893c06dc3b29871b058978438d78566e9fad43  Jefit(2020).csv
        Good Lines: 2,891,960
    """

    name = "None"
    web = "jefit.com"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        email = domain = password = ''
        row = r.split(':')

        email = row[0].strip()
        password = row[1].strip()
        domain = email.split('@')[1] if '@' in email else ''

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