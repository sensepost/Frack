import collections
from parsers import base


class Parse(base.Parser):
    """
        MyFitnessPal.com breach data parser
        Source File SHA-1: beabd8723bbea33982b91e85eb35cceae3e7faee  2018-myfitnesspal_emailpass_50M.txt
        Good Lines: 48,917,501
    """

    name = "None"
    web = "MyFitnessPal.com"
    year = "2018"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                kriistel@web.de:chucks2310

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(':')

        email = row[0]
        domain = row[0].split('@')[1] if '@' in email else ''
        password = row[1].strip()

        return self.name, self.web, int(self.year), domain, email, password, '', ''

    def process_rows(self) -> collections.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue
                    
                if len(row.split(':')) != 2:
                    continue

                yield self.row_format(row)
