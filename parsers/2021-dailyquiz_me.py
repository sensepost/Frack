import collections
from parsers import base


class Parse(base.Parser):
    """
        Dailyquiz.me breach data parser
        Source File SHA-1: a08a93b5828ed61c09863e43e28d0f08a68ed221  dailyquiz.me2021.csv
        Good Lines: 10,875,573
    """

    name = "None"
    web = "dailyquiz.me"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                username,password,email
                lizzy,lizzyloo,u_ecoleman@umassd.edu

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        email = domain = password = ''
        row = r.split(',')

        if len(row) == 3:
            email = row[2].replace('\'', '').strip()
            domain = email.split('@')[1] if '@' in email else ''
            password = row[1].replace('\'', '').strip()
        else:
            email = domain = password = ''
        
        return self.name, self.web, int(self.year), domain, email, password, '', ''

    def process_rows(self) -> collections.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)
