from parsers import base
import collections


class Parse(base.Parser):
    """
        Patreon.com 2015 breach data parser
        Source File SHA-1: a60acd81dd95c51bedfc056e4caeda86b70ed0d0  patreon.sql
        Good Lines: 2,209,954
    """

    name = "None"
    web = "www.patreon.com"
    year = "2015"

    def row_format(self, r: str) -> tuple:
        """
            Header: `UID` int(10) unsigned NOT NULL AUTO_INCREMENT,
              `Email` varchar(128) DEFAULT NULL,
              `FName` varchar(64) DEFAULT NULL,
              `LName` varchar(64) DEFAULT NULL,
              `Password` varchar(64) DEFAULT NULL,
              `Created` datetime NOT NULL,
              `FBID` bigint(16) unsigned DEFAULT NULL,
              `ImageUrl` varchar(128) DEFAULT NULL,
              `ThumbUrl` varchar(128) DEFAULT NULL,
              `photo_key` varchar(128) DEFAULT NULL,
              `thumbnail_key` varchar(128) DEFAULT NULL,
              `Gender` tinyint(4) NOT NULL DEFAULT '0',
              `Status` tinyint(4) NOT NULL DEFAULT '0',
              `Vanity` varchar(64) DEFAULT NULL,
              `About` text,
              `Youtube` varchar(64) DEFAULT NULL,
              `Twitter` varchar(64) DEFAULT NULL,
              `Facebook` varchar(64) DEFAULT NULL,
              `is_suspended` tinyint(3) unsigned NOT NULL DEFAULT '0',
              `is_deleted` tinyint(3) unsigned NOT NULL DEFAULT '0',
              `is_nuked` tinyint(3) unsigned NOT NULL DEFAULT '0',
              `is_admin` tinyint(4) DEFAULT '0',
              `two_factor_enabled` tinyint(4) DEFAULT '0'
            Table Name: tblUsers

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(',')

        email = row[1].replace('\'', '').strip()
        pw_hash = row[4].replace('\'', '').strip()
        domain = email.split('@')[1] if '@' in email else ''

        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.Iterable[tuple]:
        print('\nPlease wait. It takes a while to get to the data.', flush=True)
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                if not row.startswith(r"INSERT INTO `tblUsers` VALUES"):
                    continue

                _, values = row.split('VALUES')
                inserts = values.split(r'),(')

                for value_tuple in inserts:
                    yield self.row_format(value_tuple)