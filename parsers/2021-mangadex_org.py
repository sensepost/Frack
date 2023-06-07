import collections
from parsers import base


class Parse(base.Parser):
    """
        A mangadex.org breach data parser
        Source File SHA-1: 16574c7590d218214d518e4ac5d29107440f5b36  MangaDex.org.txt
        Good Lines: 542,093
    """

    name = "None"
    web = "mangadex.org"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                kriistel@web.de:chucks2310

           email,password

            :param r:
            :return:
        """

        row = r.split('\t')
        hash = ''

        try:
            email = row[2]
            domain = row[2].split('@')[1]
            hash = row[3].strip()
            #password = row[1].strip()
        except:
            email = domain = password = ''
        
        print(email + ':' + hash)

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
