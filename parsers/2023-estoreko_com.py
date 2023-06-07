from parsers import base
import collections


class Parse(base.Parser):
    """
        Estoreko.com breach data parser
        44ee7889c7e211affa74777c65ba763328cc2c42  revupas_users.sql
        Good Lines: 516,530
    """

    name = "None"
    web = "estoreko.com"
    year = "2023"

    def row_format(self, r: str) -> tuple:
        """
            CREATE TABLE `users` (
                `id` int(10) UNSIGNED NOT NULL,
                `first_name` varchar(160) COLLATE utf8_unicode_ci NOT NULL,
                `last_name` varchar(160) COLLATE utf8_unicode_ci NOT NULL,
                `username` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
                `email` varchar(160) COLLATE utf8_unicode_ci NOT NULL,
                `password` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
                `sex` enum('Mr','Mrs','Ms') COLLATE utf8_unicode_ci NOT NULL DEFAULT 'Mr',
                `mem_type` enum('0','1','2','3') COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
                `country` varchar(3) COLLATE utf8_unicode_ci NOT NULL,
                `sponsor` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
                `user_ip` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
                `avatar` varchar(255) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'default.jpg',
                `mobile` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
                `regMethod` enum('0','1','2','3','4') COLLATE utf8_unicode_ci NOT NULL DEFAULT '1',
                `confirmed` tinyint(1) NOT NULL DEFAULT '0',
                `blocked` tinyint(1) NOT NULL DEFAULT '0',
                `confirmation_code` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
                `created_at` timestamp NULL DEFAULT NULL,
                `updated_at` timestamp NULL DEFAULT NULL,
                `remember_token` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL
        """
        pw_hash = ''
        password = ''
        salt = ''

        row = r.split(',')

        #for x in range(0, len(row)):
        #    print(f'{x}: ' + row[x])
        #exit()

        try:
            email = row[4].replace('\'', '').strip()
            pw_hash = row[5].replace('\'', '').strip()
            domain = email.split('@')[1] if '@' in email else ''
            #print(f'{email}:{password}')
            #print(f'{email}:{pw_hash}')
        except:
            email = domain = password = pw_hash = ''

        return self.name, self.web, int(self.year), domain, email, password, pw_hash, salt

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)