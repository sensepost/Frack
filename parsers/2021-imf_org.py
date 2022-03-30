import collections

from parsers import base


class Parse(base.Parser):
    """
        imf.org breach data parser
        Source File SHA-1: 62b4d62c4070f7e3c9b31fb68958760d7cc41883  imf.org.csv
        Good Lines: 844
    """

    name = "None"
    web = "imf.org"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                barbararicardo@uol.com.br:lizie123
                'ja-fleury@bol.com.br:as102030

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        row = r.split(';')

        if len(row) == 3:
            email = row[0]
            try:
                domain = row[0].split('@')[1]
            except:
                domain = ''
            pw_hash = row[2].strip()
        else:
            email = domain = password = ''
        
        #print(f'{email}:{pw_hash}')

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
