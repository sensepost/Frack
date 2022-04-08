import collections
from parsers import base


class Parse(base.Parser):
    """
        blankmediagames.com breach data parser
        Source File SHA-1: 4f65d5836db9d7aaad23f9252f70041f0f473a82     BlankMediaGames.sql
        Good Lines: 7,777,534
    """

    name = "None"
    web = "blankmediagames.com"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                ACE887:mwebera4@aol.com:10.189.252.5:$H$9lyQSOv4Lch/dVR9lK0IaoX/JfvWbp1
                Werekill:cmwebster@valdosta.edu:10.189.252.5:$H$9BD/1W8F47VkNHwRoOghzHI1cp0iw21
                DeezNutzR4U:arnoux@mweb.co.za:10.189.252.5:$H$9n0OKt1YDVzaza6eoU9ED.zplcpFjc0

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        pw_hash = ''
        password = ''
        salt = ''

        row = r.split(':')

        #for x in range(1, len(row)):
        #    print(f'{x}: ' + row[x])
        #exit()

        try:
            email = row[1].strip()
            try:
                domain = email.split('@')[1]
            except:
                domain = ''
            pw_hash = row[3].strip()
        except:
            email = domain = password = pw_hash = ''
        
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
