import collections
from parsers import base


class Parse(base.Parser):
    """
        TryOnCourse breach data parser
        Source File SHA-1: 021406e14a596bc765a5cc629270a4e45acad8a2  tryoncourse.csv
        Good Lines: 23,410
    """

    name = "None"
    web = "tryoncourse.com"
    year = "2022"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                id,firstname,lastname,email,altemail,password,chathandle,avatar,publicInfo,phone,cellnumber,
                userLevel,notes,heardabout,nocontact,tradingRoomOptions,referUserId,isDuplicate,acceptedDisclaimer,
                bio,business,geoip,created_at,updated_at,sms_country,merchantId,is_login,free_Account

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(',')

        try:
            email = row[3].strip()
            domain = email.split('@')[1] if '@' in email else ''
        except:
            email = domain = ''
        try:
            pw_hash = row[5].strip()
        except:
            pw_hash = ''
        
        salt = ''
        #print(email + ':' + pw_hash + ':' + salt)

        return self.name, self.web, int(self.year), domain, email, '', pw_hash, salt

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)
