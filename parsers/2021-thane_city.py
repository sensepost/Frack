import collections
from parsers import base


class Parse(base.Parser):
    """
        thane.city breach data parser
        Source File SHA-1: 3607a577329e3a52a540ee2cc76db3faea589981  thane.city - 2021-07-04.txt
        Good Lines: 18,440
    """

    name = "None"
    web = "thane.city"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                deepakkeswani@yahoo.com:$P$BfEQQHYahm1sOAGiqAO86p/nBv3llS.

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(':')
        if (len(row) == 2) and ('@' in row[0]):
            email = row[0]
            domain = email.split('@')[1]
            hash = row[1].strip()
        else:
            email = domain = hash = ''

        return self.name, self.web, int(self.year), domain, email, '', hash, ''

    def process_rows(self) -> collections.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)
