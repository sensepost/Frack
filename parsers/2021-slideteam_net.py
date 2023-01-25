import collections
from parsers import base


class Parse(base.Parser):
    """
        SlideTeam breach data parser
        Source File SHA-1: adc3e5fa5baccd657be89979da97a4415c1cd33b  slideteam.net_1.4m_magento_april2020.csv
        Good Lines: 1,463,526
    """

    name = "None"
    web = "slideteam.net"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                entity_id,website_id,email,group_id,increment_id,store_id,created_at,updated_at,is_active,
                disable_auto_group_change,created_in,prefix,firstname,middlename,lastname,suffix,dob,
                password_hash,rp_token,rp_token_created_at,default_billing,default_shipping,taxvat,
                confirmation,gender,failures_num,first_failure,lock_expires,cid,uuid

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(',')

        email = row[2].strip()
        domain = email.split('@')[1] if '@' in email else ''
        try:
            pw_hash = row[17].strip().split(':')[0]
        except:
            pw_hash = ''
        try:
            salt = row[17].strip().split(':')[1]
        except:
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
