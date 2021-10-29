import collections
from parsers import base


class Parse(base.Parser):
    """
        canva.com breach data parser
        Source File SHA-1: 4726585905d51407b211c1e202cebe9741fcb492  Canva.txt
        Good Lines: 947,936
    """

    name = "None"
    web = "canva.com"
    year = "2019"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                &dali.nava@hotmail.com:dali.nava

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
