import collections
from parsers import base


class Parse(base.Parser):
    """
        royalenfield.com breach data parser
        Source File SHA-1: a7ba8c856ff1966ca0fee9a835ff660c98806024  49.205.181.100.re-node-db.users(royalenfield.com).json
        Good Lines: 279,962
    """

    name = "None"
    web = "royalenfield.com"
    year = "2022"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                {'_id':·ObjectId('5bacc2e59bb8962504a6e13a'),·'locality':·{'country':·'in',·'language':·'en'},·'addr
                │ essInfo':·{'address':·'Retubowli·Tolichowki·St.anns·College·Lane·',·'city':·'Not·Available',·'state'
                │ :·'Not·Available',·'country':·'Not·Available',·'pinCode':·'500021'},·'socialNetworkUrls':·{'facebook
                │ ':·None,·'googlePlus':·None,·'instagram':·None,·'twitter':·None},·'previousUserId':·13,·'fname':·'Da
                │ n',·'lname':·'Khan',·'gender':·'12',·'phoneNo':·'4830437220',·'bikename':·None,·'city':·'Not·Availab
                │ le',·'aboutMe':·'',·'profilePicture':·'/node/assets/User/ProfileImage/profile_image_dummy.jpg',·'cov
                │ erImage':·'/node/assets/User/coverImage/cover-image.jpg',·'dob':·'Sun·May·17·1987·05:30:00·GMT+0530·
                │ (India·Standard·Time)',·'ownBike':·None,·'reviewCreated':·[],·'mobileVerified':·False,·'emailVerifie
                │ d':·False,·'otp':·None,·'emailToken':·None,·'isRoyalEnfieldOwner':·'False·····',·'bikeOwned':·[],·'r
                │ idesCreated':·[],·'tripStoriesCreated':·[],·'ridesJoined':·[],·'discussionJoined':·[],·'favouriteQuo
                │ te':·None,·'favouriteRideExperience':·None,·'userType':·'user',·'loginStatus':·False,·'jwtAccessToke
                │ n':·None,·'userInterest':·None,·'userUrl':·'/content/royal-enfield/in/en/home/users/user-profiles.ht
                │ ml?userid=5bacc2e59bb8962504a6e13a',·'email':·'uradorablefriend1@yahoo.co.in',·'password':·'apUufzii
                │ 1cI=',·'ownedBikeInfo':·[],·'listofTags':·[],·'__v':·0}

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        pw_hash = ''
        password = ''
        salt = ''

        row = r.split(',')

        #for x in range(1, len(row)):
        #    print(f'{x}: ' + row[x])
        #exit()

        try:
            email = row[42].split(' ')[2].strip("'") 
            try:
                domain = email.split('@')[1]
            except:
                domain = ''
            pw_hash = row[43].split(' ')[2].strip("'")
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

                yield self.row_format(row)
