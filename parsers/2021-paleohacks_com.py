import collections
from parsers import base


class Parse(base.Parser):
    """
        PaleoHacks breach data parser
        Source File SHA-1: 58bc9c604899a8a218b60d4daf194d5e6db538d2  users.csv
        Good Lines: 59,878
    """

    name = "None"
    web = "paleohacks.com"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                id,name,legacy,email,encrypted_password,reset_password_token,reset_password_sent_at,
                remember_created_at,sign_in_count,current_sign_in_at,last_sign_in_at,current_sign_in_ip,
                last_sign_in_ip,confirmation_token,confirmed_at,confirmation_sent_at,unconfirmed_email,
                username,role,description,company,website,location,born_on,created_at,updated_at,slug,
                enabled,page_title,meta_description,invitation_token,invitation_created_at,invitation_sent_at,
                invitation_accepted_at,invitation_limit,invited_by_id,invited_by_type,ah_email_id,ah_auth_id,
                legacy_password,provider,uid,avatar,about_me,blocked,reputation,sash_id,level,inactive_at,
                legacy_slug,stack_exchange_legacy_id,legacy_password_restored_at,cached_points

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
            pw_hash = row[4].strip()
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
