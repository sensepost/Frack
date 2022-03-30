import collections
from parsers import base


class Parse(base.Parser):
    """
        teespring.com breach data parser
        Source File SHA-1: 73b11542564476ba784756e42f8b0cc97cb7a282  teespring.csv
        Good Lines: 4,504,993
    """

    name = "None"
    web = "teespring.com"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                crystalallen831@gmail.com,12a86d0ef5f1852a2028e7606381245dfe5a3907

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(',')
        if (len(row) == 2) and ('@' in row[0]):
            email = row[0]
            domain = email.split('@')[1]
            hash = row[1].strip()
        else:
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
