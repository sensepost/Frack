from parsers import base
import collections


class Parse(base.Parser):
    """
        NitroPDF.com 2021 breach data parser
        Source File SHA-1: 50dbf53333ef77ef59cd170be4c33931e613b8d9  nitrocloud.tsv
        Good Lines: 76,856,990
    """

    name = "None"
    web = "www.nitropdf.com"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            Header: id bigint NOT NULL,
                tmp_admin boolean DEFAULT false,
                agreed boolean NOT NULL,
                created timestamp without time zone,
                email character varying(255) NOT NULL,
                firstname character varying(255),
                lastname character varying(255),
                password character varying(255),
                passwordreset character varying(255),
                verified boolean NOT NULL,
                avatar character varying(255),
                settings integer DEFAULT 0 NOT NULL,
                source character varying(255),
                notifications integer DEFAULT 0 NOT NULL,
                status character varying(255) DEFAULT 'ACTIVE'::character varying NOT NULL,
                secret character varying(255) DEFAULT '123abc'::character varying NOT NULL,
                confirmed_client_access boolean DEFAULT false NOT NULL,
                account_id bigint NOT NULL,
                timezone character varying(255),
                dateformat character varying(255),
                verify_remind timestamp(6) without time zone,
                desktop_version character varying(255),
                locale character varying(10),
                prompts integer DEFAULT 0 NOT NULL,
                title character varying(255),
                company character varying(255),
                sem_id bigint,
                updated_at timestamp without time zone,
                tos_pp_accepted_at timestamp without time zone,
                remote_ip character varying(50)
            Table Name: users.user_credential

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split('\t')

        email = row[4].replace('\'', '').strip()
        pw_hash = row[7].replace('\'', '').strip()
        domain = email.split('@')[1] if '@' in email else ''

        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                if len(row.split('\t')) < 29:
                    continue

                yield self.row_format(row)