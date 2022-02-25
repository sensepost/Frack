import collections
from parsers import base


class Parse(base.Parser):
    """
        A 123rf.com breach data parser
        Source File SHA-1: 28f439448b7a8237e62847d4df48b95d42c1fec4  123rf.com member.sql
        Good Lines: 8,292,274
    """

    name = "None"
    web = "www.123rf.com"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """

            '036','','882a8cafb7c64a3de1329048debd2469','','osamu','iizuka',
            '238 West 74th Street Apt. 4A','','New York','NY','US','10023',
            '646 468 4097','osmizk@gmail.com','Y','',0.00,1,'','paypal','',
            '50.00','N','2008-09-17 00:00:00','','','','','','','Y','','Y',
            '66.108.27.17','us15',1,1,'',0,'US','NY','','','','','',0,0

            :param r:
            :return:
        """

        row = r.split(',')

        email = row[13].replace('\'', '').strip()
        pw_hash = row[2].replace('\'', '').strip()
        domain = email.split('@')[1] if '@' in email else ''

        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                if not row.startswith(r"INSERT INTO `member`"):
                    continue

                _, values = row.split('VALUES')
                inserts = values.split(r'),(')

                for value_tuple in inserts:
                    yield self.row_format(value_tuple)
