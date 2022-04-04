import collections

from parsers import base


class Parse(base.Parser):
    """
        streeteasy.com breach data parser
        Source File SHA-1: 963b0e61938b50bea1a3abb1a6c3cabf2fff40b2  streeteasy.sql
        Good Lines: 988,174
    """

    name = "None"
    web = "streeteasy.com"
    year = "2019"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                1000014,nycnat,0b9f0305192bd8e8f85d007bf94425c554fe9263,1ba605f162d825074e534df4f431467ba8013706,
                nat@tribeca.com,Natalie Cuchel,1,lists,d3663a00e4d63cf5,2015-09-29 12:12:57,2005-11-08 17:35:39,
                2015-12-18 12:32:46,2015-09-01 12:12:57,0,,--- n:email_saved_items: truen:save_options: {}nn:building: 773n:comment_count: 
                4n:listings_order: price_ascn,4376,1,0,,-1,2008-01-29,2014-02-12,natalie,,0,1,1,0,0,0,0,,sales,0,,R,0,1,,,,,1,1

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        password = ''
        salt = ''

        row = r.split(',')

        try:
            email = row[4]
            try:
                domain = row[4].split('@')[1]
            except:
                domain = ''
            pw_hash = row[3].strip()
        except:
            email = domain = pw_hash = ''
        
        #print(f'{email}:{password}')
        #print(f'{email}:{pw_hash}')

        return self.name, self.web, int(self.year), domain, email, password, pw_hash, salt

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)
