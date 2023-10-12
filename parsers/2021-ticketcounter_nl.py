import collections

from parsers import base


class Parse(base.Parser):
    """
        ticketcounter.nl breach data parser
        Source File SHA-1: c87c1251ecc9d4bad3a5f082337484688420278f  TicketCounter.nl.csv
        Good Lines: 94,076
    """

    name = "None"
    web = "ticketcounter.nl"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                C_FirstName,C_MiddleName,C_LastName,C_Gender,C_Mail,C_PasswordHash,C_LastPasswords,C_PhoneNumber,
                C_VatNumber,C_CompanyName,C_BankAccountNumber,C_BankAccountCityName,A_street,A_HouseNumber,
                A_ExtraAddressLine,A_PostalCode,A_CityName,A_StateName,A_CountryName,A_lat,A_lon,R_IPAddress,
                R_PaymentMethod,R_DiscountTitle,P_Method,P_CardNumber,P_Amount,P_Brand,C_DOB

                email,hash

            :param r:
            :return:
        """
        # Note: The pw_last field is a random hash - Not the users last password
        pw_hash = ''
        password = ''
        salt = ''

        
        row = r.split(',')

        try:
            email = row[4]
            try:
                domain = row[4].split('@')[1]
            except:
                domain = ''
            pw_hash = row[5].strip()
        except:
            email = domain = password = pw_hash = ''
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
                # Ignore header row
                if row.split(',')[0] == "C_FirstName":
                    continue

                yield self.row_format(row)
