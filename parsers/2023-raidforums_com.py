from parsers import base
import collections


class Parse(base.Parser):
    """
        raidforums.com breach data parser
        90af7467d429c11f3d7d34f934f77ed1fdde96da  raidforums.com.sql
        Good Lines: 478,515
    """

    name = "None"
    web = "raidforums.com"
    year = "2023"

    def row_format(self, r: str) -> tuple:
        """
            CREATE TABLE `mybb_users` (
                `uid` int(10) unsigned NOT NULL AUTO_INCREMENT,
                `username` varchar(120) NOT NULL DEFAULT '',
                `password` varchar(500) DEFAULT NULL,
                `salt` varchar(10) NOT NULL DEFAULT '',
                `loginkey` varchar(50) NOT NULL DEFAULT '',
                `email` varchar(220) NOT NULL DEFAULT '',
                `postnum` int(10) unsigned NOT NULL DEFAULT 0,
                `threadnum` int(10) unsigned NOT NULL DEFAULT 0,
                `avatar` varchar(200) NOT NULL DEFAULT '',
                `avatardimensions` varchar(10) NOT NULL DEFAULT '',
                `avatartype` varchar(10) NOT NULL DEFAULT '0',
                `usergroup` smallint(5) unsigned NOT NULL DEFAULT 0,
                `additionalgroups` varchar(200) NOT NULL DEFAULT '',
                `displaygroup` smallint(5) unsigned NOT NULL DEFAULT 0,
                `usertitle` varchar(250) NOT NULL DEFAULT '',
                `regdate` int(10) unsigned NOT NULL DEFAULT 0,
                `lastactive` int(10) unsigned NOT NULL DEFAULT 0,
                `lastvisit` int(10) unsigned NOT NULL DEFAULT 0,
                `lastpost` int(10) unsigned NOT NULL DEFAULT 0,
                `website` varchar(200) NOT NULL DEFAULT '',
                `icq` varchar(50) NOT NULL DEFAULT '',
                `skype` varchar(75) NOT NULL DEFAULT '',
                `google` varchar(75) NOT NULL DEFAULT '',
                `birthday` varchar(15) NOT NULL DEFAULT '',
                `birthdayprivacy` varchar(4) NOT NULL DEFAULT 'all',
                `signature` text NOT NULL,
                `allownotices` tinyint(1) NOT NULL DEFAULT 0,
                `hideemail` tinyint(1) NOT NULL DEFAULT 0,
                `subscriptionmethod` tinyint(1) NOT NULL DEFAULT 0,
                `invisible` tinyint(1) NOT NULL DEFAULT 0,
                `receivepms` tinyint(1) NOT NULL DEFAULT 0,
                `receivefrombuddy` tinyint(1) NOT NULL DEFAULT 0,
                `pmnotice` tinyint(1) NOT NULL DEFAULT 0,
                `pmnotify` tinyint(1) NOT NULL DEFAULT 0,
                `buddyrequestspm` tinyint(1) NOT NULL DEFAULT 1,
                `buddyrequestsauto` tinyint(1) NOT NULL DEFAULT 0,
                `threadmode` varchar(8) NOT NULL DEFAULT '',
                `showimages` tinyint(1) NOT NULL DEFAULT 1,
                `showvideos` tinyint(1) NOT NULL DEFAULT 1,
                `showsigs` tinyint(1) NOT NULL DEFAULT 0,
                `showavatars` tinyint(1) NOT NULL DEFAULT 0,
                `showquickreply` tinyint(1) NOT NULL DEFAULT 0,
                `showredirect` tinyint(1) NOT NULL DEFAULT 0,
                `ppp` smallint(6) unsigned NOT NULL DEFAULT 0,
                `tpp` smallint(6) unsigned NOT NULL DEFAULT 0,
                `daysprune` smallint(6) unsigned NOT NULL DEFAULT 0,
                `dateformat` varchar(4) NOT NULL DEFAULT '',
                `timeformat` varchar(4) NOT NULL DEFAULT '',
                `timezone` varchar(5) NOT NULL DEFAULT '',
                `dst` int(1) NOT NULL DEFAULT 0,
                `dstcorrection` int(1) NOT NULL DEFAULT 0,
                `buddylist` text NOT NULL,
                `ignorelist` text NOT NULL,
                `style` smallint(5) unsigned NOT NULL DEFAULT 0,
                `away` int(1) NOT NULL DEFAULT 0,
                `awaydate` int(10) unsigned NOT NULL DEFAULT 0,
                `returndate` varchar(15) NOT NULL DEFAULT '',
                `awayreason` varchar(200) NOT NULL DEFAULT '',
                `pmfolders` text NOT NULL,
                `notepad` text NOT NULL,
                `referrer` int(10) unsigned NOT NULL DEFAULT 0,
                `referrals` int(10) unsigned NOT NULL DEFAULT 0,
                `reputation` int(11) NOT NULL DEFAULT 0,
                `regip` varbinary(16) NOT NULL DEFAULT '',
                `lastip` varbinary(16) NOT NULL DEFAULT '',
                `language` varchar(50) NOT NULL DEFAULT '',
                `timeonline` int(10) unsigned NOT NULL DEFAULT 0,
                `showcodebuttons` tinyint(1) NOT NULL DEFAULT 0,
                `totalpms` int(10) unsigned NOT NULL DEFAULT 0,
                `unreadpms` int(10) unsigned NOT NULL DEFAULT 0,
                `warningpoints` int(3) unsigned NOT NULL DEFAULT 0,
                `moderateposts` int(1) NOT NULL DEFAULT 0,
                `moderationtime` int(10) unsigned NOT NULL DEFAULT 0,
                `suspendposting` int(1) NOT NULL DEFAULT 0,
                `suspensiontime` int(10) unsigned NOT NULL DEFAULT 0,
                `suspendsignature` int(1) NOT NULL DEFAULT 0,
                `suspendsigtime` int(10) unsigned NOT NULL DEFAULT 0,
                `coppauser` tinyint(1) NOT NULL DEFAULT 0,
                `classicpostbit` tinyint(1) NOT NULL DEFAULT 0,
                `loginattempts` smallint(2) unsigned NOT NULL DEFAULT 1,
                `usernotes` text NOT NULL,
                `sourceeditor` tinyint(1) NOT NULL DEFAULT 0,
                `myalerts_disabled_alert_types` text NOT NULL,
                `newpoints` decimal(16,2) NOT NULL DEFAULT 0.00,
                `newpoints_items` text NOT NULL,
                `ougc_awards` text NOT NULL,
                `password_algorithm` varchar(30) NOT NULL DEFAULT '',
                `password_encryption` smallint(5) NOT NULL DEFAULT 0,
                `password_downgraded` varchar(500) NOT NULL DEFAULT '',
                `loginlockoutexpiry` int(11) NOT NULL DEFAULT 0,
                `secret` varchar(16) NOT NULL DEFAULT '',
                `ougc_awards_owner` tinyint(1) NOT NULL DEFAULT 0,
                `socials` text NOT NULL,
                `postbitbg` varchar(200) NOT NULL DEFAULT '',
                `showsafelinks` tinyint(1) NOT NULL DEFAULT 1,
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
            pw_hash = row[2].replace('\'', '').strip()
            salt = row[3].replace('\'', '').strip()
            domain = email.split('@')[1] if '@' in email else ''
        except:
            email = domain = password = pw_hash = ''

        #print(f'{email}:{password}')
        #print(f'{email}:{pw_hash}:{salt}')

        return self.name, self.web, int(self.year), domain, email, password, pw_hash, salt

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)