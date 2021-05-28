import collections
from parsers import base


class Parse(base.Parser):
    """
        Vipoferta.bg breach data parser
        Source File SHA-1: a5aa4025e3bcfece9c62a83a7e7b9905edc87ebc  vip_users_front.csv
        Good Lines: 331,573
    """

    name = "None"
    web = "vipoferta.bg"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                id,aff_id,city_id,last_id,site_id,brand_id,facebook_id,registred_by_id,pic,salt,edate,email,
                phone,uname,upass,active,level,flag_fb,last_ip,get_mail,lastname,postdate,firstname,reg_offer,
                utm_medium,utm_source,companyname,flag_finish,last_change,register_ip,user_balans,
                utm_campaign,businessaddress

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(',')

        if len(row) == 33:
            email = row[11].strip()
            domain = email.split('@')[1] if '@' in email else ''
            pw_hash = row[14].strip()
            salt = row[9].strip()
        else:
            email = domain = pw_hash = salt = ''

        return self.name, self.web, int(self.year), domain, email, '', pw_hash, salt

    def process_rows(self) -> collections.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)
