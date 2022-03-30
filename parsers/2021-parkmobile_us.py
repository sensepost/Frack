import collections
from parsers import base


class Parse(base.Parser):
    """
        Parkmobile.us breach data parser
        Source File SHA-1: d06823f1ecdccab5aae1ed79db3d2787a16d9f8b  Parkmobile.us_2021-03-21.9M.csv
        Good Lines: 19,855,817
    """

    name = "None"
    web = "Parkmobile.us"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                "CLIENT_ID","TITLE","INITIALS","FIRST_NAME","LAST_NAME","GENDER","DATE_OF_BIRTH","MOBILE_NUMBER",
                "EMAIL","USER_NAME","PASSWORD","SECOND_PASSWORD","THIRD_PASSWORD","SOCIAL_SECURITY_NUMBER",
                "ADDRESSLINE_1","ZIPCODE","CITY","VRN","DESCRIPTIONS"

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        email = ''
        pw_hash = ''
        row = r.split('","')

        for field in row:
            if '@' in field:
                email = field.replace('\'', '').strip()
            if field.count('$') == 3:
                pw_hash = field.replace('\'', '').strip()
        
        domain = email.split('@')[1] if '@' in email else ''
        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                if len(row.split('","')) != 18:
                    continue

                yield self.row_format(row)
