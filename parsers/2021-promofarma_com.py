import collections
from parsers import base


class Parse(base.Parser):
    """
        A promofarma.com breach data parser
        Source File SHA-1: 2f9a7bcdbc37fa6d94700ee22035d93c0cc24657  promofarma.com(2021).csv
        Good Lines: 2,549,177
    """

    name = "None"
    web = "promofarma.com"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                '15f9631230ccdb901871c75b3056ef77@pf.com','873731.9734634198.ajDr/YppfLxM'

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        pw_hash = email = domain = ''
        row = r.split(',')

        email = row[0].replace('\'', '').strip()
        pw_hash = row[1].replace('\'', '').strip()
        domain = email.split('@')[1] if '@' in email else ''

        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)
