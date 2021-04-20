from parsers import base
import collections


class Parse(base.Parser):
    """
        WishBone.com 2021 breach data parser
        Source File SHA-1: e938ab6a93d48ba64179adcb7871767b8bf0cde4  users.sql
        Good Lines: 9,082,166
    """

    name = "None"
    web = "wishbone.com"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            Header: `uid` int(10) NOT NULL AUTO_INCREMENT,
                `username` varchar(100) DEFAULT NULL,
                `email` varchar(255) DEFAULT NULL,
                `name` varchar(500) DEFAULT NULL,
                `mobile_number` varchar(20) DEFAULT NULL,
                `country_code` varchar(3) NOT NULL DEFAULT 'US',
                `fbid` varchar(255) NOT NULL,
                `access_token` text NOT NULL,
                `auth_token` varchar(100) NOT NULL,
                `ip` varchar(30) NOT NULL,
                `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                `twitter_id` varchar(255) DEFAULT '0',
                `twitter_access_token` text,
                `twitter_access_secret` text,
                `gender` varchar(10) DEFAULT NULL,
                `date_of_birth` date NOT NULL DEFAULT '0000-00-00',
                `password` varchar(200) DEFAULT NULL,
                `image` varchar(1000) DEFAULT NULL,
                `follower_count` int(45) DEFAULT '0',
                `device_token` text,
                `android_device_token` text,
                `is_admin` int(1) DEFAULT '0',
                `timezone` varchar(100) NOT NULL DEFAULT 'America/Los_Angeles',
                `displaying_post_date` date DEFAULT NULL,
                `is_device_active` tinyint(1) NOT NULL DEFAULT '0',
                `shared_for_date` varchar(15) NOT NULL DEFAULT '0000-00-00' COMMENT 'YYYY-MM-DD-SESSION',
                `show_second_session_date` date NOT NULL DEFAULT '0000-00-00',
                `apple_idfa` text,
                `google_advertiser_id` text,
                `stickers_left` int(10) NOT NULL DEFAULT '5',
                `deleted_at` timestamp NULL DEFAULT NULL,
                `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            Table Name: Users

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(',')

        if len(row) == 32:
                email = row[2].replace('\'', '').strip()
                pw_hash = row[16].replace('\'', '').strip()
                domain = email.split('@')[1] if '@' in email else ''
        else:
            email = pw_hash = domain = ""

        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                if not row.startswith(r"INSERT INTO `Users` VALUES"):
                    continue

                _, values = row.split('VALUES')
                inserts = values.split(r'),(')

                for value_tuple in inserts:
                    yield self.row_format(value_tuple)