import collections, json
from parsers import base


class Parse(base.Parser):
    """
        A Pixlr.com 2020 breach data parser
        Source File SHA-1: 893a5be2a01ef7256f679e2ce2a6a4555295bd9d  pixlr.json
        Good Lines: 452,909
    """

    name = "None"
    web = "pixlr.com"
    year = "2020"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                {"_id":{"$oid":"4cf73f88eddc6c0876002c53"},"agreements":[{"name":"LICENSE AND SERVICES AGREEMENT",
                "version":1.0,"time":{"$date":"2019-11-04T16:00:00.000Z"}},{"name":"TERMS OF USE","version":1.0,
                "time":{"$date":"2019-11-04T16:00:00.000Z"}},{"name":"PRIVACY POLICY","version":1.0,"time":{"$date":"2019-11-04T16:00:00.000Z"}}],
                "country":"US","email":"elenam3tr@yahoo.com","name":"elena",
                "password":"c3ef09d91febc17dfc0c8ad1b050b0e9893fd0603eef85d82d18ff23add9c3bc65d01d45b03a06fc416ebb2c8a67b028fdf6a2d9e08d3545a92e24769a2b598d",
                "region":"North America","sendgrid_list_id":"ZWxlbmFtM3RyQHlhaG9vLmNvbQ==","tokens":{"flickr":"72157625511929186-23ad07d8e7a0b7b1"},
                "updatedAt":{"$date":"2020-08-11T03:55:07.597Z"},"__v":1,"admin":[],"admin_dbr":[],"createdAt":{"$date":"2020-08-11T03:55:07.597Z"}}

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        email = pw_hash = domain = ''

        data = json.loads(r)

        try:
            email = data['email']
            pw_hash = data['password']
            domain = email.split('@')[1] if '@' in email else ''
        except:
            pass

        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.Iterable[tuple]:
        """
            Returns rows for the caller to process
        """

        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                yield self.row_format(row)