from parsers import base
import collections


class Parse(base.Parser):
    """
        Thingiverse.com 2020 breach data parser
        Source File SHA-1: d6206521db1aebb8ccc628ee9c6f49142daf5ce4 thingiverse.com.sql
        Good Lines: 2,079,128
        
        sed -n '152656437,154736144p' thingiverse.com.sql > parse.txt
        152656437:/*!40000 ALTER TABLE `users` DISABLE KEYS */;
        154736144:/*!40000 ALTER TABLE `users` ENABLE KEYS */;

    """

    name = "None"
    web = "thingiverse.com"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            Header:   `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
            `username` varchar(32) NOT NULL,
            `first_name` varchar(32) DEFAULT NULL,
            `last_name` varchar(32) DEFAULT NULL,
            `email` varchar(255) NOT NULL,
            `pass_hash` varchar(60) DEFAULT NULL,
            `pass_reset_hash` varchar(100) DEFAULT NULL,
            `pass_reset_expires_on` datetime DEFAULT NULL,
            `bio` text NOT NULL,
            `image_id` int(11) unsigned NOT NULL DEFAULT '0',
            `location` varchar(255) NOT NULL,
            `last_active` datetime NOT NULL,
            `registered_on` datetime NOT NULL,
            `is_admin` tinyint(1) NOT NULL DEFAULT '0',
            `default_license` varchar(255) NOT NULL DEFAULT 'cc-sa',
            `email_new_comments` tinyint(1) NOT NULL DEFAULT '1',
            `email_new_derivatives` tinyint(1) NOT NULL DEFAULT '1',
            `email_on_featured` tinyint(1) NOT NULL DEFAULT '1',
            `email_new_instances` tinyint(1) NOT NULL DEFAULT '1',
            `email_new_instance_comments` tinyint(1) NOT NULL DEFAULT '1',
            `email_new_grouptopic_comments` tinyint(1) NOT NULL DEFAULT '1',
            `can_change_username` tinyint(1) NOT NULL DEFAULT '1',
            `flattr_id` varchar(255) DEFAULT NULL,
            `is_curator` tinyint(1) NOT NULL DEFAULT '0',
            `is_moderator` tinyint(1) NOT NULL DEFAULT '0',
            `features` bigint(20) unsigned NOT NULL DEFAULT '0',
            `cover_id` int(11) unsigned DEFAULT '0',
            `website` varchar(255) DEFAULT '',
            `premade_cover` int(11) DEFAULT '0',
            `country` varchar(255) DEFAULT NULL,
            `industry` varchar(255) DEFAULT NULL,
            `verification_hash` varchar(32) DEFAULT NULL,
            `site_theme` varchar(10) DEFAULT 'mb',
            `is_super_admin` tinyint(1) unsigned DEFAULT '0',
            `birthday` datetime DEFAULT NULL,
            `avatar_url` text,
            `needs_moderation` tinyint(1) unsigned NOT NULL DEFAULT '0',
            `verification_hash_expires_on` datetime DEFAULT NULL,
            Table Name: users

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(',')
        
        try:
            email = row[4].replace('\'', '').strip()
            pw_hash = row[5].replace('\'', '').strip()
            domain = email.split('@')[1] if '@' in email else ''
        except:
            domain = email = pw_hash = ''
        
        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)