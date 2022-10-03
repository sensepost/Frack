import collections
from parsers import base


class Parse(base.Parser):
    """
        start.film breach data parser
        Source File SHA-1: ee8e74c9ef9322ec67b7eaf14082804cf77fd7af  data.csv
        Good Lines: 7,455,793
    """

    name = "None"
    web = "start.film"
    year = "2022"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                kriistel@web.de:chucks2310

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(',')
        hash = ''

        try:
            email = row[0]
            domain = row[0].split('@')[1]
            hash = row[2].strip()
        except:
            email = domain = hash = ''

        return self.name, self.web, int(self.year), domain, email, '', hash, ''

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)
