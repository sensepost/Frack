from parsers import base
import collections


class Parse(base.Parser):
    """
        MeetMindful.com 2021 breach data parser
        Source File SHA-1: 32899271f14797127fe8e57b13d78237f1b211fb  mindful
        Good Lines: 1,270,930
    """

    name = "None"
    web = "meetmindful.com"
    year = "2021"

    def row_format(self, r: str) -> tuple:
        """
            Header: "id" | "first_name" | "last_name" | "username" | "email" | "birthday" | "city" | "state" | "zip" | "sex" | "dating_status" | 
            "sex_interested_in" | "height" | "last_active" | "password_digest" | "authentication_token" | "created_at" | "updated_at" | 
            "latitude" | "longitude" | "status" | "confirmation_token" | "confirmed_at" | "password_reset_token" | "primary_photo_id" | 
            "failed_logins_count" | "locked_at" | "search_preference_distance" | "search_preference_age_min" | "search_preference_age_max" | 
            "search_preference_children" | "search_preference_education" | "search_preference_religion" | "search_preference_drugs" | 
            "search_preference_alcohol" | "search_preference_cigarettes" | "stripe_customer_id" | "plan_type" | "country" | "cancelled_at" | 
            "last_failed_payment" | "facebook_user_id" | "facebook_access_token" | "mixpanel_distinct_id" | "signup_ip" | "last_active_ip" | 
            "last_platform" | "last_nps_vote_at" | "plan_id" | "last_invoice" | "review_code" | "local_match_count" | "whitelist_fl" | 
            "profile_score" | "locale_id" | "promotional_status" | "promotional_count" | "referral_code" | "search_preference_mindful_living_practices" | 
            "needs_moderation_fl" | "needs_moderation_reason" | "ip_country" | "sendgrid_id" | "search_preference_diet" | "timezone" | 
            "affiliate_id" | "became_active_at" | "last_app_review_at" | "search_preference_status" | "search_preference_activity" | 
            "search_preference_profile" | "search_preference_relationship_types" | "search_preference_height" | "active_until_at" | 
            "email_validated_fl" | "email_preferences" | "last_os" | "search_preference_height_min" | "search_preference_height_max" | 
            "user_detail_id" | "initial_referring_domain" | "grid_view_enabled" | "joined_meetmindful_light_at" | "match_recipe_id" | 
            "region_id" | "search_preference_diet_deserialized" | "search_preference_religion_deserialized" | "search_preference_education_deserialized" | 
            "search_preference_children_deserialized" | "sex_temp" | "sex_interested_temp" | "sex_identity_other" | "profile_updated_at" | 
            "push_preferences" | "last_client_version" | "google_analytics_client_id"
        
           name,website,year,domain,email,password,hash,salt

            :param r:
            :return:
        """

        row = r.split(' | ')
        email = ""
        pw_hash = ""

        for field in row:
            if '@' in field:
                email = field.strip()
            if field.count('$') == 3:
                pw_hash = field.strip()

        domain = email.split('@')[1] if '@' in email else ''
        return self.name, self.web, int(self.year), domain, email, '', pw_hash, ''

    def process_rows(self) -> collections.abc.Iterable[tuple]:
        with open(self.source, 'r', encoding='utf-8', errors='ignore') as source:
            for row in source:
                if row is None:
                    continue

                if len(row.split(' | ')) < 96:
                    continue

                yield self.row_format(row)