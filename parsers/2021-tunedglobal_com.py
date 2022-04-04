import collections

from parsers import base


class Parse(base.Parser):
    """
        tunedglobal.com breach data parser
        Source File SHA-1: c0e89bcfa835910c2b0a3ae748995473375d438f  music_users.sql
        Good Lines: 464,251
    """

    name = "None"
    web = "tunedglobal.com"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                user_id├──┤member_id├──┤group_id├──┤login├──┤password├──┤firstname├──┤surname├──┤email├──┤address1├─
                │ ─┤address2├──┤suburb├──┤city├──┤state├──┤postcode├──┤country├──┤region├──┤phone_BH├──┤phone_AH├──┤we
                │ bsite├──┤reg_datetime├──┤active├──┤opted_in├──┤allow_playlist├──┤allow_stream├──┤device_id├──┤client
                │ _usercode├──┤pwd_question├──┤pwd_answer├──┤last_updated├──┤parental_pin├──┤allow_explicit├──┤test_us
                │ er├──┤referrer├──┤social_login├──┤

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        row = r.split('\t')

        try:
            email = row[8]
            try:
                domain = row[8].split('@')[1]
            except:
                domain = ''
            password = row[5].strip()
        except:
            email = domain = password = ''
        
        #print(f'{email}:{password}')

        return self.name, self.web, int(self.year), domain, email, password, '', ''

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)
