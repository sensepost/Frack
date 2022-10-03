from parsers import base
import collections


class Parse(base.Parser):
    """
        Exvagos.com breach data parser
        Source File SHA-1: 094e9b51438dc32a8f6567d190c3b60eeb524584  exvagos.com_users.sql
        Good Lines: 2,122,415
    """

    name = "None"
    web = "exvagos.com"
    year = "2022"

    def row_format(self, r: str) -> tuple:
        """
            Header:
                `userid` int(10) unsigned NOT NULL AUTO_INCREMENT,
                `usergroupid` smallint(5) unsigned NOT NULL DEFAULT 0,
                `membergroupids` char(250) NOT NULL DEFAULT '',
                `displaygroupid` smallint(5) unsigned NOT NULL DEFAULT 0,
                `username` varchar(100) NOT NULL DEFAULT '',
                `password` char(32) NOT NULL DEFAULT '',
                `passworddate` date NOT NULL DEFAULT '1000-01-01',
                `email` char(100) NOT NULL DEFAULT '',
                `styleid` smallint(5) unsigned NOT NULL DEFAULT 0,
                `parentemail` char(50) NOT NULL DEFAULT '',
                `homepage` char(100) NOT NULL DEFAULT '',
                `icq` char(20) NOT NULL DEFAULT '',
                `aim` char(20) NOT NULL DEFAULT '',
                `yahoo` char(32) NOT NULL DEFAULT '',
                `msn` char(100) NOT NULL DEFAULT '',
                `skype` char(32) NOT NULL DEFAULT '',
                `showvbcode` smallint(5) unsigned NOT NULL DEFAULT 0,
                `showbirthday` smallint(5) unsigned NOT NULL DEFAULT 2,
                `usertitle` char(250) NOT NULL DEFAULT '',
                `customtitle` smallint(6) NOT NULL DEFAULT 0,
                `joindate` int(10) unsigned NOT NULL DEFAULT 0,
                `daysprune` smallint(6) NOT NULL DEFAULT 0,
                `lastvisit` int(10) unsigned NOT NULL DEFAULT 0,
                `lastactivity` int(10) unsigned NOT NULL DEFAULT 0,
                `lastpost` int(10) unsigned NOT NULL DEFAULT 0,
                `lastpostid` int(10) unsigned NOT NULL DEFAULT 0,
                `posts` int(10) unsigned NOT NULL DEFAULT 0,
                `reputation` int(11) NOT NULL DEFAULT 10,
                `reputationlevelid` int(10) unsigned NOT NULL DEFAULT 1,
                `timezoneoffset` char(4) NOT NULL DEFAULT '',
                `pmpopup` smallint(6) NOT NULL DEFAULT 0,
                `avatarid` smallint(6) NOT NULL DEFAULT 0,
                `avatarrevision` int(10) unsigned NOT NULL DEFAULT 0,
                `profilepicrevision` int(10) unsigned NOT NULL DEFAULT 0,
                `sigpicrevision` int(10) unsigned NOT NULL DEFAULT 0,
                `options` int(10) unsigned NOT NULL DEFAULT 15,
                `birthday` char(10) NOT NULL DEFAULT '',
                `birthday_search` date NOT NULL DEFAULT '1000-01-01',
                `maxposts` smallint(6) NOT NULL DEFAULT -1,
                `startofweek` smallint(6) NOT NULL DEFAULT 1,
                `ipaddress` varchar(45) NOT NULL DEFAULT '',
                `referrerid` int(10) unsigned NOT NULL DEFAULT 0,
                `languageid` smallint(5) unsigned NOT NULL DEFAULT 0,
                `emailstamp` int(10) unsigned NOT NULL DEFAULT 0,
                `threadedmode` smallint(5) unsigned NOT NULL DEFAULT 0,
                `autosubscribe` smallint(6) NOT NULL DEFAULT -1,
                `pmtotal` smallint(5) unsigned NOT NULL DEFAULT 0,
                `pmunread` smallint(5) unsigned NOT NULL DEFAULT 0,
                `salt` char(30) NOT NULL DEFAULT '',
                `ipoints` int(10) unsigned NOT NULL DEFAULT 0,
                `infractions` int(10) unsigned NOT NULL DEFAULT 0,
                `warnings` int(10) unsigned NOT NULL DEFAULT 0,
                `infractiongroupids` varchar(255) NOT NULL DEFAULT '',
                `infractiongroupid` smallint(5) unsigned NOT NULL DEFAULT 0,
                `adminoptions` int(10) unsigned NOT NULL DEFAULT 0,
                `profilevisits` int(10) unsigned NOT NULL DEFAULT 0,
                `friendcount` int(10) unsigned NOT NULL DEFAULT 0,
                `friendreqcount` int(10) unsigned NOT NULL DEFAULT 0,
                `vmunreadcount` int(10) unsigned NOT NULL DEFAULT 0,
                `vmmoderatedcount` int(10) unsigned NOT NULL DEFAULT 0,
                `socgroupinvitecount` int(10) unsigned NOT NULL DEFAULT 0,
                `socgroupreqcount` int(10) unsigned NOT NULL DEFAULT 0,
                `pcunreadcount` int(10) unsigned NOT NULL DEFAULT 0,
                `pcmoderatedcount` int(10) unsigned NOT NULL DEFAULT 0,
                `gmmoderatedcount` int(10) unsigned NOT NULL DEFAULT 0,
                `post_thanks_user_amount` int(10) unsigned NOT NULL DEFAULT 0,
                `post_thanks_thanked_posts` int(10) unsigned NOT NULL DEFAULT 0,
                `post_thanks_thanked_times` int(10) unsigned NOT NULL DEFAULT 0,
                `vbseo_likes_in` int(10) unsigned NOT NULL DEFAULT 0,
                `vbseo_likes_out` int(10) unsigned NOT NULL DEFAULT 0,
                `vbseo_likes_unread` int(10) unsigned NOT NULL DEFAULT 0,
                `invitation` int(10) unsigned NOT NULL DEFAULT 100,
                `caninvitation` tinyint(3) unsigned NOT NULL DEFAULT 1,
            Table Name: user

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(',')
        
        try:
            email = row[8].replace('\'', '').strip()
            pw_hash = row[5].replace('\'', '').strip()
            domain = email.split('@')[1] if '@' in email else ''
            #print(email + ':' + pw_hash)
        except:
            domain = email = pw_hash = ''
        
        
        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)