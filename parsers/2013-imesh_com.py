import collections
from parsers import base


class Parse(base.Parser):
    """
        iMesh.com breach data parser
        Source File SHA-1: a394d54457f4b7450d3afb348794e6d10f6bcbb5  2013-iMesh.com_44kk_[+8kk_new_records].txt
        Good Lines: 43,879,389
    """

    name = "None"
    web = "iMesh.com"
    year = "2013"

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
