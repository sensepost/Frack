from parsers import base
import collections


class Parse(base.Parser):
    """
        Herb.com 2019 breach data parser
        Source File SHA-1: f787e785cfd7e64f2d170c0a4c66533e75c85df6  hotelurbano.sql
        Good Lines: 6,113,438
        NOTE: This file contains a substantial amount of hashes that's NULL.
    """

    name = "None"
    web = "Herb.com"
    year = "2019"

    def row_format(self, r: str) -> tuple:
        """
            (20739360,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Eduardo','Bachiao','eduardobachiaoheitor13@gmail.com',
            'bb137143fc5ce07bc5719aed241a5d27',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,
            0.00,0,NULL,'2019-03-13 18:20:50','2019-03-13 21:20:50',0,'10.12.3.116',0,NULL,NULL,0,NULL,NULL,NULL,1)

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(',')

        if len(row) == 44:
            email = row[12].strip().replace('\'', '')
            pw_hash = row[13].strip().replace('\'', '')
            domain = email.split('@')[1] if '@' in email else ''
        else:
            email = pw_hash = domain = ""

        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                if not row.startswith(r"INSERT INTO `usuario` VALUES"):
                    continue

                inserts = row.split(r'),(')

                for value_tuple in inserts:
                    yield self.row_format(value_tuple)