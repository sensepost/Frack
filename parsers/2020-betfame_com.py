import collections
from parsers import base


class Parse(base.Parser):
    """
        betfame.com breach data parser
        Source File SHA-1: a46f38b084ace950b79ba3498f393071d1ce216b  user.csv
        Good Lines: 13,662
    """

    name = "None"
    web = "betfame.com"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                id,country_id,middle_name,affiliate_id,identity_token,zip,dob,city,type,state,email,
                phone,gender,online,status,loginIP,picname,country,campaign,currency,password,address1,
                address2,photo_img,last_name,user_name,is_mobile,bonuscode,bookmaker,lastLogin,first_name,
                isApproved,user_token,verify_email,totalCredits,social_email,created_date,affiliatecode,
                activationCode,socialmediatype,complete_profile,newsletter_status,first_depositReward,
                first_registerReward,last_active_timestamp

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        row = r.split(',')
        if len(row) == 45:
            try:
                email = row[10]
                domain = email.split('@')[1]
                passwd = row[20].strip()
            except:
                email = domain = passwd = ''    
        else:
            email = domain = passwd = ''

        return self.name, self.web, int(self.year), domain, email, passwd, '', ''

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)
