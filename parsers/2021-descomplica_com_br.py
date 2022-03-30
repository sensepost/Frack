import collections
from parsers import base


class Parse(base.Parser):
    """
        Descomplica.com.br breach data parser
        Source File SHA-1: 109777393cb7a8a9158fee05b981844663e8420a  users.sql
        Good Lines: 4,242,371
    """

    name = "None"
    web = "descomplica.com.br"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                ('2019-07-30 22:08:06.8330000','987339301lih@gmail.com',0,0,0,'2019-07-30 22:08:06.8500000',
                '2019-07-30 22:08:06.8500000','2019-07-30 22:08:06.8500000','2019-07-30 22:08:06.8500000',
                'AOtyXM/L9x9YMtpNdRs3TcRU8uq7ra21ig0DFftzMNvyBKgsV9FHMKVFughR+wXrwg==',0,NULL,NULL,0,
                'https://accounts.descomplica.com.br/?checkoutPath={coupon=VD_ENEMINTENSIVOPOWER_238.8_28062019}&cat=vestibulares'),

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(',')

        if len(row) == 16:
            email = row[1].replace('\'', '').strip()
            domain = email.split('@')[1] if '@' in email else ''
            pw_hash = row[1].replace('\'', '').strip()
        else:
            email = domain = pw_hash = ''

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
