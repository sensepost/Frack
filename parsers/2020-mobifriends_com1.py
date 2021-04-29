import collections
from parsers import base


class Parse(base.Parser):
    """
        MobiFriends.com breach data parser
        Source File SHA-1: 74e5468872c80fbc02f7f87bdddd8e582761fc9e  MobiFriends.com_DataBase.txt
        Good Lines: 127,217
    """

    name = "None"
    web = "mobifriends.com"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                mobifriends.noblogposts@mobifriends.com:adgjlmo7
                txavego@hotmail.com:morfeo2

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(':')

        email = row[0]
        domain = row[0].split('@')[1]
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

                yield self.row_format(row)
