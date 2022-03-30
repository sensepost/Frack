import collections
from parsers import base


class Parse(base.Parser):
    """
        A Wattpad.com 2020 breach data parser
        Source File SHA-1: af9ddbc8138b013c80c882cb109991bd689c25d1 wattpad_24133700_lines.txt
        Good Lines: 23,987,479
    """

    name = "None"
    web = "wattpad.com"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                !4grimaldia@granbyschools.org,paris25

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(',')

        if '@' in row[0]:
            email = row[0]
        else:
            email = ''
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

                if len(row.split(',')) < 2:
                    continue

                yield self.row_format(row)