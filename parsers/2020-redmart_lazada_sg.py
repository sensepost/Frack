import collections

from parsers import base


class Parse(base.Parser):
    """
        redmart.lazada.sg breach data parser
        Source File SHA-1: 07afd4d1f5aac2d142397f779ac26ee9bb2d9c12  Redmart.lazada.sg.txt
        Good Lines: 919,526
    """

    name = "None"
    web = "redmart.lazada.sg"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                "aladdin's.sale@gmail.com":Ashikali1787
                "gegeorgetvuk'@gmail.com":George1957
                "i'm.caboose@gmail.com":anhha123

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        pw_hash = ''
        password = ''
        salt = ''

        row = r.split(':')

        try:
            email = row[0].strip('"')
            try:
                domain = row[0].split('@')[1].strip('"')
            except:
                domain = ''
            password = row[1].strip()
        except:
            email = domain = password = ''
        
        #print(f'{email}:{password}')
        #print(f'{email}:{pw_hash}')

        return self.name, self.web, int(self.year), domain, email, password, pw_hash, salt

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)
