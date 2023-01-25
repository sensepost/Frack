import collections
from parsers import base


class Parse(base.Parser):
    """
        yavp.pl breach data parser
        Source File SHA-1: 95d1408d433c5839ade43227f0098cec7e1b9b87  yavp.pl_e_p.txt
        Good Lines: 18,585
    """

    name = "None"
    web = "yavp.pl"
    year = "2022"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                kriistel@web.de:chucks2310

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        row = r.split(':')
        try:
            email = row[0]
            domain = row[0].split('@')[1]
            password = row[1].strip()
        except:
            email = domain = password = ''

        return self.name, self.web, int(self.year), domain, email, password, '', ''

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)
