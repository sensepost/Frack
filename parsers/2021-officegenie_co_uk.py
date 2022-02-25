import collections
from parsers import base


class Parse(base.Parser):
    """
        OfficeGenie.co.uk 2021 breach data parser
        Source File SHA-1: 348632cbd4bcdbfabae387d0d8e3cf955f5396c1  community_users_202104192144.csv
        Good Lines: 4,663
    """

    name = "None"
    web = "OfficeGenie.co.uk"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                1,Chris Marling,"",chris.marling@genieventures.co.uk,"9e0a1ce20b9d864b247110160c9e6578","0000-00-00 00:00:00","2013-03-26 12:05:41",91,editor,"",0

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(',')

        if len(row) == 13:
            email = row[1].strip().replace('\"', '')
            domain = row[1].split('@')[1] if '@' in email else ''
            pw_hash = row[2].strip().replace('\"', '')
        else:
            email = pw_hash = domain = ""

        print(f'{email}:{pw_hash}')

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
