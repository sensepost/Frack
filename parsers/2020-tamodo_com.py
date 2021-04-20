from parsers import base
import collections


class Parse(base.Parser):
    """
        Tamodo.com 2020 breach data parser
        Source File SHA-1: c8a2ee7508fb3bce0a3aab8a2244757b0540f0c7  103.205.96.158.affiliate_master_dev.users.txt
        Good Lines: 440,110
    """

    name = "None"
    web = "tamodo.com"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            Sample: {'_id': 318375, 'firstName': 'Le', 'lastName': 'Han', 'fullName': 'Le Han', 'email': 'nhamaythaotran@gmail.com', 
            'referredBy': 265782, 'password': '$2a$10$.Zfmytr3ZWmDz5T6zt884eykmwYmq46rcHAJ8iNBSpu/8GisKMxH2', 'status': 'INACTIVE',
            'country': 238, 'inviter': 265782, 'relationUserIds': [], 'code': '229035202', 'level': 11, 
            'createdAt': datetime.datetime(2020, 2, 18, 8, 51, 56), 'role': 'PUBLISHER', 'address': '', 'gender': 'MALE', 
            'identity': '', 'otpTs': datetime.datetime(2020, 2, 19, 3, 33, 18, 421000), 
            'updatedAt': datetime.datetime(2020, 2, 19, 3, 33, 18, 430000)}

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(':')

        # Data later in the dataset shifts the positions of the fields we want,
        # So we iterate through the fields. If it contains an @, we've got an e-mail.
        # If it contains 3x $'s, it's a hash.
        for field in row:
            if '@' in field:
                email = field.split(',')[0].replace('\'', '').replace(' ', '').strip()
            if field.count('$') == 3:
                pw_hash = field.split(',')[0].replace('\'', '').replace(' ', '').strip()
                
        domain = email.split('@')[1] if '@' in email else ''
        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue
                              
                yield self.row_format(row)