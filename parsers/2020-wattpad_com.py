import collections
from parsers import base


class Parse(base.Parser):
    """
        A Wattpad.com 2020 breach data parser
        Source File SHA-1: dea79791e87043a3f76e4d75f33855c7278b0197 cleaned.csv
        Good Lines: 269,631,125
    """

    name = "None"
    web = "wattpad.com"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                NAME,PASSWORD,EMAIL,LOGINIP,REALNAME,LOCATION,COUNTRY,PHONE,DOB
                ivanyuen,$2y$10$ngltmcu/sjOYAyi/1zKe4.8rob04dqG90cFAeIVvUneV9/ul/EwLO,iyuen@yahoo.com,24.114.57.156,Ivan Yuen,"Toronto, Ontario",CA,,1977-01-07

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(',')

        if '@' in row[2]:
            email = row[2]
        else:
            email = ''
        domain = row[2].split('@')[1] if '@' in email else ''
        pw_hash = row[1].strip()

        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                if len(row.split(',')) < 8:
                    print("x", end='')
                    continue

                yield self.row_format(row)