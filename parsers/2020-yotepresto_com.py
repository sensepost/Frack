import collections
from parsers import base


class Parse(base.Parser):
    """
        yotepresto.com breach data parser
        Source File SHA-1: 65e987e701d19ce2b85a8ea2203a0fbe7e18eb71  yotepresto_users.csv
        Good Lines: 1,437,441
    """

    name = "None"
    web = "yotepresto.com"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                odraudek99@gmail.com,$2a$11$HO813//puYoChLENsGZS5e1IRV2B3KDrQ/eKL6hx7.YV4XDEt/95a
                ds.gzz@hotmail.com,$2a$11$eADNORkmmxN/OaifSvajt.1nGKL6A9WLxMWgHV4W.ZCRAsm2tWifa
                jm6836465@gmail.com,$2a$11$en/L1LScQH/P0xgxbK/5Je16g76vNwROBDC5jm.hwnDlDwHsdHjzC
                auditivo_latino@hotmail.com,$2a$11$W2JlRqWepKFKTFFvQkFXVO8nJ2oTJyW9AypzV4IOgEFJIYPd/I5Xe
                kuki_mefisto@hotmail.com,$2a$11$XBb3rQUPmcyCP/523aMcN.ev80dK971St0uFs8mPEcnrnfFgULdh.

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        pw_hash = ''
        password = ''
        salt = ''

        row = r.split(',')

        #for x in range(1, len(row)):
        #    print(f'{x}: ' + row[x])
        #exit()

        try:
            email = row[0]
            try:
                domain = email.split('@')[1]
            except:
                domain = ''
            pw_hash = row[1]
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
