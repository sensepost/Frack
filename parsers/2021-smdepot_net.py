from parsers import base
import collections


class Parse(base.Parser):
    """
        smdepot.net 2021 breach data parser
        Source File SHA-1: 8a35c58495ff2e4920fda189d1024d7d711aa2b3  Smdepot.net 2021.sql
        Good Lines: 322
    """

    name = "None"
    web = "smdepot.net"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            Header:   ID_MEMBER mediumint(8) unsigned NOT NULL auto_increment,
                memberName varchar(80) NOT NULL default '',
                dateRegistered int(10) unsigned NOT NULL default 0,
                posts mediumint(8) unsigned NOT NULL default 0,
                ID_GROUP smallint(5) unsigned NOT NULL default 0,
                lngfile tinytext NOT NULL,
                lastLogin int(10) unsigned NOT NULL default 0,
                realName tinytext NOT NULL,
                instantMessages smallint(5) NOT NULL default 0,
                unreadMessages smallint(5) NOT NULL default 0,
                pm_ignore_list text NOT NULL,
                passwd varchar(64) NOT NULL default '',
                emailAddress tinytext NOT NULL,
                personalText tinytext NOT NULL,
                gender tinyint(4) unsigned NOT NULL default 0,
                birthdate date NOT NULL default '0001-01-01',
                websiteTitle tinytext NOT NULL,
                websiteUrl tinytext NOT NULL,
                location tinytext NOT NULL,
                ICQ tinytext NOT NULL,
                AIM varchar(16) NOT NULL default '',
                YIM varchar(32) NOT NULL default '',
                MSN tinytext NOT NULL,
                hideEmail tinyint(4) NOT NULL default 0,
                showOnline tinyint(4) NOT NULL default 1,
                timeFormat varchar(80) NOT NULL default '',
                signature text NOT NULL,
                timeOffset float NOT NULL default 0,
                avatar tinytext NOT NULL,
                pm_email_notify tinyint(4) NOT NULL default 0,
                karmaBad smallint(5) unsigned NOT NULL default 0,
                karmaGood smallint(5) unsigned NOT NULL default 0,
                usertitle tinytext NOT NULL,
                notifyAnnouncements tinyint(4) NOT NULL default 1,
                notifyOnce tinyint(4) NOT NULL default 1,
                memberIP tinytext NOT NULL,
                secretQuestion tinytext NOT NULL,
                secretAnswer varchar(64) NOT NULL default '',
                ID_THEME tinyint(4) unsigned NOT NULL default 0,
                is_activated tinyint(3) unsigned NOT NULL default 1,
                validation_code varchar(10) NOT NULL default '',
                ID_MSG_LAST_VISIT int(10) unsigned NOT NULL default 0,
                additionalGroups tinytext NOT NULL,
                smileySet varchar(48) NOT NULL default '',
                ID_POST_GROUP smallint(5) unsigned NOT NULL default 0,
                totalTimeLoggedIn int(10) unsigned NOT NULL default 0,
                passwordSalt varchar(5) NOT NULL default '',
                messageLabels text NOT NULL,
                buddy_list text NOT NULL,
                notifySendBody tinyint(4) NOT NULL default 0,
                notifyTypes tinyint(4) NOT NULL default 2,
                memberIP2 tinytext NOT NULL,
                PRIMARY KEY (ID_MEMBER),
                KEY memberName (memberName(30)),
                KEY dateRegistered (dateRegistered),
                KEY ID_GROUP (ID_GROUP),
                KEY birthdate (birthdate),
                KEY posts (posts),
                KEY lastLogin (lastLogin),
                KEY ID_POST_GROUP (ID_POST_GROUP),
                KEY lngfile (lngfile(24))
            Table Name: smf_members

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(',')
        if len(row) == 53:
                email = row[12].replace('\'', '').strip()
                pw_hash = row[11].replace('\'', '').strip()
                domain = email.split('@')[1] if '@' in email else ''
        else:
            email = pw_hash = domain = ""

        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)