from parsers import base
import collections
import json


class Parse(base.Parser):
    """
        nulled.ch 2020 breach data parser
        Source File SHA-1: 4c6c58d35d8db2ce974ee8b5264bc8ff6d53c846  nulledch.json
        Good Lines: 35,697
    """

    name = "None"
    web = "nulled.ch"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            Header: 

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        email = r['email']
        pw_hash = r['hash']
        salt = r['salt']
        domain = email.split('@')[1] if '@' in email else ''

        return self.name, self.web, int(self.year), domain, email, '', pw_hash, salt

    def process_rows(self) -> collections.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as json_file:
            data = json.load(json_file)
            for row in data:
                if row is None:
                    continue
                
                yield self.row_format(row)