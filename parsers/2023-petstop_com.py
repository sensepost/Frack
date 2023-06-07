from parsers import base
import collections


class Parse(base.Parser):
    """
        Petstop.com breach data parser
        6c7b90d59b2c2610d5f9e617613408fd4be5bb4f  PETSTOP_FULL.sql
        Good Lines: 45,153
    """

    name = "None"
    web = "petstop.com"
    year = "2023"

    def row_format(self, r: str) -> tuple:
        """
            18037-CREATE TABLE `users` (
            18038-  `id` bigint(20) NOT NULL,
            18039-  `username` varchar(60) NOT NULL,
            18040-  `password` varchar(128) DEFAULT NULL,
            18041-  `name` varchar(256) DEFAULT NULL,
            18042-  `email` varchar(256) DEFAULT NULL,
            18043-  `last_login_timestamp` bigint(20) DEFAULT NULL,
            18044-  PRIMARY KEY (`id`),
            18045-  UNIQUE KEY `users_ak` (`username`)
            18046-) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
        except:
            email = domain = password = pw_hash = ''

        #print(f'{email}:{password}')
        #print(f'{email}:{pw_hash}')

        return self.name, self.web, int(self.year), domain, email, password, pw_hash, salt

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        print('\nPlease wait. It takes a while to get to the data.', flush=True)
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                if not row.startswith(r"INSERT INTO `users` VALUES"):
                    continue

                _, values = row.split('VALUES')
                inserts = values.split(r'),(')

                for value_tuple in inserts:
                    yield self.row_format(value_tuple)