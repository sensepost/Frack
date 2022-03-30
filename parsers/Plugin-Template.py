from parsers import base
import collections


class Parse(base.Parser):
    """
        <website>.com 2020 breach data parser
        Source File SHA-1: 97248cc3aa42dd3a6bd6b80df88a6d26b630c294
        Good Lines:
    """

    name = "None"
    web = "appen.com"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            Header: id | name | email | encrypted_password | reset_password_token | reset_password_sent_at |
            remember_created_at | sign_in_count | current_sign_in_at | last_sign_in_at | current_sign_in_ip |  
            last_sign_in_ip | failed_attempts | unlock_token | locked_at | authentication_token | salt |
            created_at | updated_at | email_verified_at | email_verification_sent_at | email_verification_token | 
            unverified_email | phone_number | company | email_subscriber | title | roles_updated_at | quick_sign_up | 
            internal_contributor_created_at | external_contributor_created_at | requestor_created_at | 
            resend_verification_email_count | identity_id | disabled_at | terms_of_service_accepted_at |
            current_team_id | api_team_id

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split('|')

        email = row[2].strip()
        pw_hash = row[3].strip()
        salt = row[16].strip()
        domain = email.split('@')[1] if '@' in email else ''

        return self.name, self.web, int(self.year), domain, email, '', pw_hash, salt

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue
                
                if len(row.split('|')) != 38:
                    print("x", end='', flush=True)
                    continue

                yield self.row_format(row)
