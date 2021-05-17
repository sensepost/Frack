import collections
from abc import ABC, abstractmethod

import pyorc
import re

class Parser(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def web(self):
        pass

    @property
    @abstractmethod
    def year(self):
        pass

    # static structure for pyorc files
    pyorc_struct = ("struct<"
                    "breach:string,site:string,year:int,domain:string,email:string,"
                    "password:string,hash:string,salt:string"
                    ">")

    def __init__(self, ifname: str):
        """
            Init a new breach parser
            :param ifname:
        """

        self.source = ifname

    def get_orc_name(self) -> str:
        """
            Returns the file name used for the resultant orc file
        """

        return f'{self.year}.{self.web}.{self.name}.orc'

    @staticmethod
    def validate_data(r: tuple) -> bool:
        """
            Validate the data is descent.

                (name,website,year,domain,email,password,hash,salt)

            :return:
        """
        # Regex for validating an E-Mail address
        email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

        if len(r) < 8:
            return False

        _, _, _, domain, email, password, hash, _ = r

        if ( not re.search(email_regex, email)):
            return False

        if password == '' and hash == '':
            return False
        
        if (hash != '') and (password != '') and (len(hash) < 16): # The shortest hash in general use is the MYSQL3 (16 chars)
            print(f'Error Hash: {hash}')
            return False

        if domain == '':
            return False

        return True

    def process(self):
        """
            Process a breach, writing the formatted results to a .orc file

            :return:
        """

        e_count, s_count = 0, 0

        with open(self.get_orc_name(), 'wb') as data_dst:
            with pyorc.Writer(data_dst, self.pyorc_struct) as writer:
                print("Processing", end='', flush=True)
                for row in self.process_rows():
                    if not self.validate_data(row):
                        e_count += 1
                        continue

                    writer.write(row)
                    s_count += 1

                    # Print status on screen every 10000 lines to save a bit of time,
                    # and to confirm it's still doing something.
                    if (s_count % 10000) == 0:
                        print('.', end='', flush=True)

        print(f'\nDone! Bad Lines: {e_count}, Good Lines: {s_count}')
        print(f'File written to: {self.get_orc_name()}')

    @abstractmethod
    def process_rows(self) -> collections.Iterable[tuple]:
        """
            Yields processed & formatted rows from the dump returning a tuple
            with fields:

                (name,website,year,domain,email,password,hash,salt)
        """

        pass
