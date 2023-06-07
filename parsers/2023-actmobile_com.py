from parsers import base
import collections


class Parse(base.Parser):
    """
        Actmobile.com breach data parser
        2dcb08330d61166541af4229ba54cd815919d050  ActMobile.com.parsed4.txt
        Good Lines: 1,675,015
    """

    name = "None"
    web = "actmobile.com"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            {"_id":{"$oid":"504e5fe7313ea25b9b00004b"},"last_name":"","url_logging_enabled":false,"is_mobileuser":true,"is_staff":false,"config_profile_id":null,"dp_cycle_start_date":{"$date":"2015-07-08T06:00:53.804Z"},"date_joined":{"$date":"2012-01-09T20:00:10.000Z"},"first_name":"","group":"default","created_by":null,"role_id":{"$oid":"53f35ee80f303b3fe92dc722"},"is_superuser":false,"last_login":{"$date":"2012-01-09T20:00:10.000Z"},"stripe_id":"","email":"chip@actmobile.com","username":"chip@actmobile.com","is_active":true,"organization":"default","password":"sha1$1fdd4$0a2b81071e11b0a2e04ab1defad0bbdde51ebc80","is_portaluser":false,"user_data_plan_id":null,"dp_cycle_end_date":{"$date":"2015-07-08T06:00:53.804Z"},"last_seen":null}
        """
        pw_hash = ''
        password = ''
        salt = ''

        row = r.split(':')

        #for x in range(0, len(row)):
        #    print(f'{x}: ' + row[x])
        #exit()

        try:
            email = row[0].replace('\'', '').strip()
            pw_hash = row[1].replace('\'', '').strip()
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