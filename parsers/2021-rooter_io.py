from parsers import base
import collections


class Parse(base.Parser):
    """
        Rooter.io 2015 breach data parser
        Source File SHA-1: 337826c1dab3547cd1c528318ca7798ca5ab8aea  rooter.sql
        Good Lines: 518,079
    """

    name = "None"
    web = "rooter.io"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            Header: CREATE TABLE `sports_fan` (
                `id` int(11) NOT NULL AUTO_INCREMENT,
                `device_id` varchar(512) COLLATE utf8_unicode_ci DEFAULT NULL,
                `device_spec` varchar(512) COLLATE utf8_unicode_ci DEFAULT NULL,
                `app_version` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
                `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
                `is_celeb` tinyint(1) NOT NULL DEFAULT '0',
                `email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
                `mobile` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
                `status` varchar(45) CHARACTER SET utf8 DEFAULT NULL COMMENT 'created, verified, banned , etc.',
                `photo` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
                `location` point NOT NULL COMMENT 'last updated location of the user. ',
                `state_id` int(11) DEFAULT NULL,
                `reputation` float(4,2) DEFAULT '0.00',
                `city` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
                `password` varchar(200) CHARACTER SET utf8 DEFAULT NULL,
                `mobile_verified` tinyint(1) DEFAULT '0',
                `email_verified` tinyint(1) DEFAULT '0',
                `device_type` varchar(45) COLLATE utf8_unicode_ci DEFAULT 'android',
                `push_id` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
                `total_points` int(11) NOT NULL DEFAULT '0',
                `gems` int(11) NOT NULL DEFAULT '0',
                `sendbird_access_token` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
                `demo_game_played` tinyint(1) DEFAULT '0',
                `demo_fantasy_played` tinyint(1) DEFAULT '0',
                `invited_by` int(11) DEFAULT NULL,
                `third_party_campaign` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
                `country_code` varchar(3) COLLATE utf8_unicode_ci DEFAULT 'IN',
                `locale` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
                `communication_email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
                `banned` tinyint(1) NOT NULL DEFAULT '0',
                `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
                `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                `deleted` tinyint(1) DEFAULT '0',
                `gender` enum('Male','Female','Other') COLLATE utf8_unicode_ci DEFAULT NULL,
                `age` date DEFAULT NULL,
            Table Name: sports_fan

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        pw_hash = ''
        password = ''
        salt = ''

        row = r.split(',')

        #for x in range(1, len(row)):
        #    print(f'{x}: ' + row[x])
        #exit()

        try:
            email = row[29].replace('\'', '').strip()
            pw_hash = row[15].replace('\'', '').strip()
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

                if not row.startswith(r"INSERT INTO `sports_fan` VALUES"):
                    continue

                _, values = row.split('VALUES')
                inserts = values.split(r'),(')

                for value_tuple in inserts:
                    yield self.row_format(value_tuple)