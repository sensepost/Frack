import collections
from parsers import base


class Parse(base.Parser):
    """
        Demo breach data parser
        Source File SHA-1: 20c3e09f188b79aa7737cd5566ad20fe7caf4dbf  fake.sql
        Good Lines: 99999
    """

    name = "None"
    web = "www.iamuptonogood.com"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """

            :param r:
            :return:
        """
        row = r.split(',')

        email = row[0].replace('\'', '').strip()
        pw_hash = row[1].replace('\'', '').strip()
        domain = email.split('@')[1] if '@' in email else ''

        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                if not row.startswith(r'INSERT INTO "fake"'):
                    continue

                _, values = row.split('VALUES')
                inserts = values.split(r'), (')

                for value_tuple in inserts:
                    yield self.row_format(value_tuple)
