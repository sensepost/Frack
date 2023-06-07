from parsers import base
import collections


class Parse(base.Parser):
    """
        Youtech.fr breach data parser
        b5db4c2f4a7463ac7fc88a621176ee376b21b7ba  youtech.fr.sql
        Good Lines: 8,173
    """

    name = "None"
    web = "youtech.fr"
    year = "2023"

    def row_format(self, r: str) -> tuple:
        """
            44920-CREATE TABLE `ps_customer` (
                44921-`firstname` `lastname` `email` `passwd` `birthday` `ip_registration`
                44922-  `newsletter_date_add` datetime DEFAULT NULL,
                44923-  `optin` tinyint(1) unsigned NOT NULL DEFAULT '0',
                44924-  `secure_key` varchar(32) NOT NULL DEFAULT '-1',
                44925-  `note` text,
                44926-  `active` tinyint(1) unsigned NOT NULL DEFAULT '0',
                44927-  `is_guest` tinyint(1) NOT NULL DEFAULT '0',
                44928-  `deleted` tinyint(1) NOT NULL DEFAULT '0',
                44929-  `date_add` datetime NOT NULL,
                44930-  `date_upd` datetime NOT NULL,
                44931-  PRIMARY KEY (`id_customer`),
                44932-  KEY `customer_email` (`email`),
                44933-  KEY `customer_login` (`email`,`passwd`),
                44934-  KEY `id_customer_passwd` (`id_customer`,`passwd`),
                44935-  KEY `id_gender` (`id_gender`)
        """
        pw_hash = ''
        password = ''
        salt = ''

        row = r.split(',')

        #for x in range(0, len(row)):
        #    print(f'{x}: ' + row[x])
        #exit()

        try:
            email = row[5].replace('\'', '').strip()
            pw_hash = row[6].replace('\'', '').strip()
            salt = row[13].replace('\'', '').strip()
            domain = email.split('@')[1] if '@' in email else ''
            
        except:
            email = domain = password = pw_hash = ''

        #print(f'{email}:{password}')
        #print(f'{email}:{pw_hash}')

        return self.name, self.web, int(self.year), domain, email, password, pw_hash, salt

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)