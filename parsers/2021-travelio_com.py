import collections

from parsers import base


class Parse(base.Parser):
    """
        travelio.com breach data parser
        Source File SHA-1: 39b91b82ecc7ad02fe6d04db9eb76c6b3d7f7c0e  TRAVELIO.csv
        Good Lines: 327,963
    """

    name = "None"
    web = "travelio.com"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            sample:
                __v,_id,accountBank,accountName,accountNumber,addedBookCount,address,agentCode,appleAuth,
                bankAccountInfo.accountName,bankAccountInfo.accountNumber,bankAccountInfo.bank,birthdate,
                blockReason,cashbackProcessed,ccInfo.cardEx,ccInfo.cardHolderName,ccInfo.maskedCC,ccInfo.midtransToken,
                ccInfo.midtransTokenEx,ccInfo.xenditToken,ccPromoCache,chance,country,createdFrom,currPhone,
                dateCreated,dateMigrated,dateModified,email,failedBidsCount,fbAuth.accessToken,fbAuth.expirationDate,
                fbAuth.fbId,firstPhoneConfirmation,genId,gender,gojekAuth,haveBooked,haveUpdateName,helloLioInvite,
                idNumber,idPhoto,isAmbassador,isTravelioAgentPatner,lastAttemptRequestOTP,lastFailedDate,lastLogin,
                log,name,newTravelioPurchaseSharedFb,newTravelioPurchaseSharedTw,npwp,npwpPhoto,organization,otherPhones,
                otp,otpExpired,password,phone,picture,point,prefLang,purchaseShared,purchaseSharedFb,purchaseSharedTw,
                pushNotifications,recentProperties,referralCode,requestOTPAttempt,resetKey,resetKeyAt,sbConnect,sbId,
                status,tapCommission,tapCommissionUnfurnished,uid,usedCCPromos,usedCoupons,usedReferralCode,utmCampaign,
                utmMedium,utmSource,wheelOfGiftsPurchaseShared,wheelOfGiftsTicket,wheelOfGiftsTicketUsage,wishlists

           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """
        pw_hash = ''
        password = ''
        salt = ''

        row = r.split(',')

        try:
            email = row[29]
            try:
                domain = row[29].split('@')[1]
            except:
                domain = ''
            pw_hash = row[58].strip()
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
