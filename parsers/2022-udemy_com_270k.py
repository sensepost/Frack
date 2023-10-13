import collections
from parsers import base


class Parse(base.Parser):
    """
        udemy.com 2022 breach data parser
        Source File SHA-1: a351e34973aa81b90daf575bdfec62bea25b79c5  udemy.com 270k.txt
        Good Lines: 267,082
    """

    name = "None"
    web = "udemy.com"
    year = "2023"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                haise47naruto@gmail.com:258047

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
                # Emails cannot start with a :
                if row.startswith(':'):
                    row = row[1:]
                # Fix some malformed rows
                if ":PASS::" in row:
                    row = row.replace(":PASS::", ":")
                if len(row.split(':')) != 2:
                    continue

                yield self.row_format(row)
