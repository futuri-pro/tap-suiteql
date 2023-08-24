"""Stream type classes for tap-suiteql."""

from singer_sdk import typing as th

from tap_suiteql.client import suiteqlStream

class AccountStream(suiteqlStream):
    '''
    366 records in NetSuite
    '''
    name = "account"
    path = "/query/v1/suiteql"
    entity_name = "account"
    primary_keys = ["id"]
    replication_key = "lastmodifieddate"
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("accountsearchdisplayname", th.StringType),
        th.Property("accountsearchdisplaynamecopy", th.StringType),
        th.Property("acctnumber", th.StringType),
        th.Property("accttype", th.StringType),
        th.Property("billableexpensesacct", th.IntegerType),
        th.Property("cashflowrate", th.StringType),
        th.Property("category1099misc", th.StringType),
        th.Property("class", th.StringType),
        th.Property("currency", th.StringType),
        th.Property("custrecord_acct_bank_account_number", th.StringType),
        th.Property("deferralacct", th.StringType),
        th.Property("department", th.IntegerType),
        th.Property("description", th.StringType),
        th.Property("displaynamewithhierarchy", th.StringType),
        th.Property("eliminate", th.BooleanType),
        th.Property("externalid", th.StringType),
        th.Property("fullname", th.StringType),
        th.Property("generalrate", th.StringType),
        th.Property("includechildren", th.BooleanType),
        th.Property("inventory", th.BooleanType),
        th.Property("isinactive", th.BooleanType),
        th.Property("issummary", th.BooleanType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("location", th.IntegerType),
        th.Property("parent", th.IntegerType),
        th.Property("reconcilewithmatching", th.BooleanType),
        th.Property("revalue", th.BooleanType),
        th.Property("sspecacct", th.StringType),
    ).to_dict()

class AccountingBookStream(suiteqlStream):
    '''
    1 records in NetSuite
    '''
    name = "accountingbook"
    path = "/query/v1/suiteql"
    entity_name = "accountingbook"
    primary_keys = ["id"]
    replication_key = "lastmodifieddate"
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("basebook", th.StringType),
        th.Property("contingentrevenuehandling", th.BooleanType),
        th.Property("effectiveperiod", th.IntegerType),
        th.Property("externalid", th.StringType),
        th.Property("isadjustmentonly", th.BooleanType),
        th.Property("isconsolidated", th.BooleanType),
        th.Property("isprimary", th.BooleanType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("name", th.StringType),
        th.Property("subsidiariesstring", th.StringType),
        th.Property("twosteprevenueallocation", th.BooleanType),
        th.Property("unbilledreceivablegrouping", th.StringType),
    ).to_dict()

class AccountingBookSubsidiariesStream(suiteqlStream):
    '''
    5 records in NetSuite
    '''
    name = "accountingbooksubsidiaries"
    path = "/query/v1/suiteql"
    entity_name = "accountingbooksubsidiaries"
    #primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("accountingbook", th.IntegerType),
        th.Property("status", th.StringType),
        th.Property("subsidiary", th.IntegerType),
    ).to_dict()

class AccountingPeriodStream(suiteqlStream):
    '''
    246 records in NetSuite
    '''
    name = "accountingperiod"
    path = "/query/v1/suiteql"
    entity_name = "accountingperiod"
    primary_keys = ["id"]
    replication_key = "lastmodifieddate"
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("alllocked", th.BooleanType),
        th.Property("allownonglchanges", th.BooleanType),
        th.Property("aplocked", th.BooleanType),
        th.Property("arlocked", th.BooleanType),
        th.Property("closed", th.BooleanType),
        th.Property("closedondate", th.DateType),
        th.Property("enddate", th.DateType),
        th.Property("id", th.IntegerType),
        th.Property("isadjust", th.BooleanType),
        th.Property("isinactive", th.BooleanType),
        th.Property("isposting", th.BooleanType),
        th.Property("isquarter", th.BooleanType),
        th.Property("isyear", th.BooleanType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("parent", th.IntegerType),
        th.Property("periodname", th.StringType),
        th.Property("startdate", th.DateType),
    ).to_dict()


class AccountingPeriodFiscalCalendarsStream(suiteqlStream):
    '''
    246 records in NetSuite
    '''
    name = "accountingperiodfiscalcalendars"
    path = "/query/v1/suiteql"
    entity_name = "accountingperiodfiscalcalendars"
    primary_keys = ["accountingperiod"]
    schema = th.PropertiesList(
        th.Property("accountingperiod", th.IntegerType),
        th.Property("fiscalcalendar", th.IntegerType),
        th.Property("fullname", th.StringType),
        th.Property("parent", th.IntegerType),
    ).to_dict()

class AccountTypeStream(suiteqlStream):
    '''
    20 records in NetSuite
    '''
    name = "accounttype"
    path = "/query/v1/suiteql"
    entity_name = "accounttype"
    primary_keys = ["internalid"]
    schema = th.PropertiesList(
        th.Property("balancesheet", th.BooleanType),
        th.Property("defaultcashflowratetype", th.StringType),
        th.Property("defaultgeneralratetype", th.StringType),
        th.Property("eliminationalgo", th.StringType),
        th.Property("id", th.StringType),
        th.Property("includeinrevaldefault", th.BooleanType),
        th.Property("internalid", th.IntegerType),
        th.Property("left", th.BooleanType),
        th.Property("longname", th.StringType),
        th.Property("seqnum", th.IntegerType),
        th.Property("usercanchangerevaloption", th.BooleanType),
    ).to_dict()

class ClassificationStream(suiteqlStream):
    '''
    33 records in NetSuite
    '''
    name = "classification"
    path = "/query/v1/suiteql"
    entity_name = "classification"
    primary_keys = ["id"]
    replication_key = "lastmodifieddate"
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("isinactive", th.BooleanType),
        th.Property("externalid", th.StringType),
        th.Property("fullname", th.StringType),
        th.Property("includechildren", th.BooleanType),
        th.Property("id", th.IntegerType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("name", th.StringType),
        th.Property("parent", th.IntegerType),
    ).to_dict()

class ConsolidatedExchangeRateStream(suiteqlStream):
    '''
    1750 records in NetSuite
    '''
    name = "consolidatedexchangerate"
    path = "/query/v1/suiteql"
    entity_name = "consolidatedexchangerate"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("accountingbook", th.IntegerType),
        th.Property("averagerate", th.NumberType),
        th.Property("currentrate", th.NumberType),
        th.Property("externalid", th.StringType),
        th.Property("fromcurrency", th.IntegerType),
        th.Property("fromsubsidiary", th.IntegerType),
        th.Property("historicalrate", th.NumberType),
        th.Property("id", th.IntegerType),
        th.Property("postingperiod", th.IntegerType),
        th.Property("tocurrency", th.IntegerType),
        th.Property("tosubsidiary", th.IntegerType),
    ).to_dict()


class CurrencyStream(suiteqlStream):
    '''
    7 records in NetSuite
    '''
    name = "currency"
    path = "/query/v1/suiteql"
    entity_name = "currency"
    primary_keys = ["id"]
    replication_key = "lastmodifieddate"
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("currencyprecision", th.IntegerType),
        th.Property("displaysymbol", th.StringType),
        th.Property("exchangerate", th.NumberType),
        th.Property("id", th.IntegerType),
        th.Property("includeinfxrateupdates", th.BooleanType),
        th.Property("isbasecurrency", th.BooleanType),
        th.Property("isinactive", th.BooleanType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("name", th.StringType),
        th.Property("overridecurrencyformat", th.BooleanType),
        th.Property("symbol", th.StringType),
        th.Property("symbolplacement", th.IntegerType),
    ).to_dict()


class CustomerStream(suiteqlStream):
    '''
    28,318 records in NetSuite
    '''
    name = "customer"
    path = "/query/v1/suiteql"
    entity_name = "customer"
    #metadata_path = "/record/v1/metadata-catalog/customer"
    primary_keys = ["id"]
    skip_attributes = ["links"]
    replication_key = "lastmodifieddate"
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("accountnumber", th.StringType),
        th.Property("alcoholrecipienttype", th.StringType),
        th.Property("altemail", th.StringType),
        th.Property("altname", th.StringType),
        th.Property("altphone", th.StringType),
        th.Property("balancesearch", th.NumberType),
        th.Property("billingratecard", th.IntegerType),
        th.Property("buyingreason", th.IntegerType),
        th.Property("buyingtimeframe", th.IntegerType),
        th.Property("campaignevent", th.IntegerType),
        th.Property("category", th.IntegerType),
        th.Property("comments", th.StringType),
        th.Property("companyname", th.StringType),
        th.Property("contact", th.IntegerType),
        #th.Property("contactlist", th.StringType),
        th.Property("creditholdoverride", th.StringType),
        th.Property("creditlimit", th.NumberType),
        th.Property("cseg_conference", th.IntegerType),
        th.Property("currency", th.IntegerType),
        th.Property("custentity10", th.StringType),
        th.Property("custentity11", th.StringType),
        th.Property("custentity12", th.StringType),
        th.Property("custentity13", th.StringType),
        th.Property("custentity14", th.StringType),
        th.Property("custentity15", th.StringType),
        th.Property("custentity16", th.StringType),
        th.Property("custentity17", th.StringType),
        th.Property("custentity19", th.StringType),
        th.Property("custentity20", th.StringType),
        th.Property("custentity21", th.StringType),
        th.Property("custentity23", th.StringType),
        th.Property("custentity24", th.StringType),
        th.Property("custentity25", th.StringType),
        th.Property("custentity26", th.StringType),
        th.Property("custentity27", th.StringType),
        th.Property("custentity28", th.StringType),
        th.Property("custentity29", th.StringType),
        th.Property("custentity30", th.StringType),
        th.Property("custentity31", th.StringType),
        th.Property("custentity32", th.StringType),
        th.Property("custentity33", th.StringType),
        th.Property("custentity37", th.StringType),
        th.Property("custentity38", th.StringType),
        th.Property("custentity39", th.StringType),
        th.Property("custentity40", th.StringType),
        th.Property("custentity41", th.StringType),
        th.Property("custentity42", th.StringType),
        th.Property("custentity43", th.StringType),
        th.Property("custentity44", th.StringType),
        th.Property("custentity47", th.StringType),
        th.Property("custentity48", th.StringType),
        th.Property("custentity5", th.StringType),
        th.Property("custentity51", th.StringType),
        th.Property("custentity53", th.StringType),
        th.Property("custentity54", th.StringType),
        th.Property("custentity55", th.StringType),
        th.Property("custentity56", th.StringType),
        th.Property("custentity57", th.StringType),
        th.Property("custentity58", th.StringType),
        th.Property("custentity6", th.StringType),
        th.Property("custentity7", th.StringType),
        th.Property("custentity8", th.StringType),
        th.Property("custentity9", th.StringType),
        th.Property("custentity_4599_sg_uen", th.StringType),
        th.Property("custentity_ann_revenue", th.StringType),
        th.Property("custentity_ar_follow_up_date", th.StringType),
        th.Property("custentity_ar_specialist_list", th.StringType),
        th.Property("custentity_atlas_pbcs_category", th.StringType),
        th.Property("custentity_atlas_pbcs_category_2", th.StringType),
        th.Property("custentity_budget_approved", th.StringType),
        th.Property("custentity_buying_time_frame", th.StringType),
        th.Property("custentity_celigo_calendar_enabled", th.StringType),
        th.Property("custentity_celigo_ce_lmd", th.StringType),
        th.Property("custentity_celigo_gmail_msg_record", th.StringType),
        th.Property("custentity_celigo_hubspot_id", th.StringType),
        th.Property("custentity_celigo_hubspot_skip_export", th.StringType),
        th.Property("custentity_collection_notes", th.StringType),
        th.Property("custentity_collection_status", th.StringType),
        th.Property("custentity_company_size", th.StringType),
        th.Property("custentity_contract_item_customer_since", th.StringType),
        th.Property("custentity_contract_item_retention_date", th.StringType),
        th.Property("custentity_cr_ms_active", th.StringType),
        th.Property("custentity_cr_ms_active_date", th.StringType),
        th.Property("custentity_cr_ms_inactive_date", th.StringType),
        th.Property("custentity_customer_channel_tier", th.StringType),
        th.Property("custentity_customer_type", th.StringType),
        th.Property("custentity_date_lsa", th.StringType),
        th.Property("custentity_decision_maker_id", th.StringType),
        th.Property("custentity_dic", th.StringType),
        th.Property("custentity_esc_annual_revenue", th.StringType),
        th.Property("custentity_esc_industry", th.StringType),
        th.Property("custentity_esc_no_of_employees", th.StringType),
        th.Property("custentity_est_budget", th.StringType),
        th.Property("custentity_freshdesk_created_at", th.StringType),
        th.Property("custentity_freshdesk_updated_at", th.StringType),
        th.Property("custentity_hs_analytics_f_ce", th.StringType),
        th.Property("custentity_hs_analytics_f_ce_date", th.StringType),
        th.Property("custentity_hs_analytics_f_v_date", th.StringType),
        th.Property("custentity_hs_analytics_f_v_referrer", th.StringType),
        th.Property("custentity_hs_analytics_f_v_url", th.StringType),
        th.Property("custentity_hs_analytics_l_ce", th.StringType),
        th.Property("custentity_hs_analytics_l_ce_date", th.StringType),
        th.Property("custentity_hs_analytics_l_v_date", th.StringType),
        th.Property("custentity_hs_analytics_l_v_referrer", th.StringType),
        th.Property("custentity_hs_analytics_l_v_url", th.StringType),
        th.Property("custentity_hs_analytics_page_views", th.StringType),
        th.Property("custentity_hs_analytics_source", th.StringType),
        th.Property("custentity_hs_analytics_source_data_1", th.StringType),
        th.Property("custentity_hs_analytics_source_data_2", th.StringType),
        th.Property("custentity_hs_analytics_visits", th.StringType),
        th.Property("custentity_hs_annualrevenue", th.StringType),
        th.Property("custentity_hs_closedate", th.StringType),
        th.Property("custentity_hs_company", th.StringType),
        th.Property("custentity_hs_contact_url", th.StringType),
        th.Property("custentity_hs_country", th.StringType),
        th.Property("custentity_hs_createdate", th.StringType),
        th.Property("custentity_hs_email_bounce", th.StringType),
        th.Property("custentity_hs_email_click", th.StringType),
        th.Property("custentity_hs_email_delivered", th.StringType),
        th.Property("custentity_hs_email_open", th.StringType),
        th.Property("custentity_hs_followercount", th.StringType),
        th.Property("custentity_hs_hubspot_score", th.StringType),
        th.Property("custentity_hs_industry", th.StringType),
        th.Property("custentity_hs_ipaddress", th.StringType),
        th.Property("custentity_hs_lifecyclestage", th.StringType),
        th.Property("custentity_hs_message", th.StringType),
        th.Property("custentity_hs_num_conversions", th.StringType),
        th.Property("custentity_hs_numemployees", th.StringType),
        th.Property("custentity_hs_phone", th.StringType),
        th.Property("custentity_hs_social_facebook_clicks", th.StringType),
        th.Property("custentity_hs_social_last_engagement", th.StringType),
        th.Property("custentity_hs_social_linkedin_clicks", th.StringType),
        th.Property("custentity_hs_social_twitter_clicks", th.StringType),
        th.Property("custentity_hs_twitterhandle", th.StringType),
        th.Property("custentity_hs_twitterprofilephoto", th.StringType),
        th.Property("custentity_hs_vid", th.StringType),
        th.Property("custentity_hs_website", th.StringType),
        th.Property("custentity_ico", th.StringType),
        th.Property("custentity_link_lsa", th.StringType),
        th.Property("custentity_link_name_lsa", th.StringType),
        th.Property("custentity_lockout_notice_date", th.StringType),
        th.Property("custentity_marquee_customer", th.StringType),
        th.Property("custentity_multi_locations", th.StringType),
        th.Property("custentity_my_brn", th.StringType),
        th.Property("custentity_other_sw_considered", th.StringType),
        th.Property("custentity_reference_classification", th.StringType),
        th.Property("custentity_reference_notes", th.StringType),
        th.Property("custentity_reference_status", th.StringType),
        th.Property("custentity_rsc_cashcustomer", th.StringType),
        th.Property("custentity_sii_id", th.StringType),
        th.Property("custentity_sii_id_type", th.StringType),
        th.Property("custentity_stripe_company_name", th.StringType),
        th.Property("custentity_stripe_product", th.StringType),
        th.Property("custentity_stripe_trial_customer", th.StringType),
        th.Property("custentity_sw_switched_from", th.StringType),
        th.Property("custentity_swe_customer_discount", th.StringType),
        th.Property("custentity_sync_data_last_changed", th.StringType),
        th.Property("custentity_tax_contact", th.StringType),
        th.Property("custentity_tax_contact_first", th.StringType),
        th.Property("custentity_tax_contact_last", th.StringType),
        th.Property("custentity_tax_contact_middle", th.StringType),
        th.Property("custentity_tax_reg_no", th.StringType),
        th.Property("custentity_uplift", th.StringType),
        th.Property("custentity_uplift_cap", th.StringType),
        th.Property("custentity_uplift_cap_type", th.StringType),
        th.Property("custentity_uplift_type", th.StringType),
        th.Property("custentity_year_est", th.StringType),
        th.Property("custentityfreshdesk_id", th.StringType),
        th.Property("custentityhs_company_id", th.StringType),
        th.Property("custentityhs_email_first_click", th.StringType),
        th.Property("custentityhs_email_first_open", th.StringType),
        th.Property("custentityhs_email_first_send", th.StringType),
        th.Property("custentityhs_email_last_send", th.StringType),
        th.Property("custentityhs_ip_city", th.StringType),
        th.Property("custentityhs_ip_country", th.StringType),
        th.Property("custentityhs_ip_country_code", th.StringType),
        th.Property("custentityhs_ip_state", th.StringType),
        th.Property("custentityhs_ip_state_code", th.StringType),
        th.Property("custentityhs_last_email_click", th.StringType),
        th.Property("custentityhs_last_email_open", th.StringType),
        th.Property("custentityhs_optedout", th.StringType),
        th.Property("custentityhs_predictive_score", th.StringType),
        th.Property("custentityhs_supress", th.StringType),
        th.Property("dateclosed", th.DateTimeType),
        th.Property("datecreated", th.DateTimeType),
        th.Property("defaultbankaccount", th.IntegerType),
        th.Property("defaultbillingaddress", th.IntegerType),
        th.Property("defaultorderpriority", th.NumberType),
        th.Property("defaultshippingaddress", th.IntegerType),
        th.Property("draccount", th.IntegerType),
        th.Property("duplicate", th.BooleanType),
        th.Property("email", th.StringType),
        th.Property("emailpreference", th.StringType),
        th.Property("emailtransactions", th.BooleanType),
        th.Property("enddate", th.DateType),
        th.Property("entityid", th.StringType),
        th.Property("entitynumber", th.IntegerType),
        th.Property("entitystatus", th.IntegerType),
        th.Property("entitytitle", th.StringType),
        th.Property("estimatedbudget", th.NumberType),
        th.Property("externalid", th.StringType),
        th.Property("fax", th.StringType),
        th.Property("faxtransactions", th.BooleanType),
        th.Property("firstname", th.StringType),
        th.Property("firstorderdate", th.DateType),
        th.Property("firstsaledate", th.DateType),
        th.Property("globalsubscriptionstatus", th.IntegerType),
        th.Property("homephone", th.StringType),
        th.Property("id", th.IntegerType),
        th.Property("isautogeneratedrepresentingentity", th.BooleanType),
        th.Property("isbudgetapproved", th.BooleanType),
        th.Property("isinactive", th.BooleanType),
        th.Property("isperson", th.BooleanType),
        th.Property("language", th.StringType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("lastname", th.StringType),
        th.Property("lastorderdate", th.DateType),
        th.Property("lastsaledate", th.DateType),
        th.Property("leadsource", th.IntegerType),
        th.Property("middlename", th.StringType),
        th.Property("mobilephone", th.StringType),
        th.Property("negativenumberformat", th.IntegerType),
        th.Property("numberformat", th.IntegerType),
        th.Property("oncredithold", th.BooleanType),
        th.Property("overduebalancesearch", th.NumberType),
        th.Property("parent", th.IntegerType),
        th.Property("partner", th.IntegerType),
        th.Property("phone", th.StringType),
        th.Property("prefccprocessor", th.IntegerType),
        th.Property("pricelevel", th.IntegerType),
        th.Property("printoncheckas", th.StringType),
        th.Property("printtransactions", th.BooleanType),
        th.Property("probability", th.StringType),
        th.Property("receivablesaccount", th.IntegerType),
        th.Property("reminderdays", th.IntegerType),
        th.Property("representingsubsidiary", th.IntegerType),
        th.Property("resalenumber", th.StringType),
        th.Property("salesreadiness", th.IntegerType),
        th.Property("salesrep", th.IntegerType),
        th.Property("salutation", th.StringType),
        th.Property("searchstage", th.StringType),
        th.Property("shipcomplete", th.BooleanType),
        th.Property("shippingcarrier", th.StringType),
        th.Property("shippingitem", th.IntegerType),
        th.Property("startdate", th.DateType),
        th.Property("terms", th.IntegerType),
        th.Property("territory", th.IntegerType),
        th.Property("thirdpartyacct", th.StringType),
        th.Property("thirdpartycarrier", th.StringType),
        th.Property("thirdpartycountry", th.StringType),
        th.Property("thirdpartyzipcode", th.StringType),
        th.Property("title", th.StringType),
        th.Property("unbilledorderssearch", th.NumberType),
        th.Property("url", th.StringType),
    ).to_dict()


class DepartmentStream(suiteqlStream):
    '''
    26 records in NetSuite
    '''
    name = "department"
    path = "/query/v1/suiteql"
    entity_name = "department"
    primary_keys = ["id"]
    replication_key = "lastmodifieddate"
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("externalid", th.StringType),
        th.Property("fullname", th.StringType),
        th.Property("id", th.IntegerType),
        th.Property("includechildren", th.BooleanType),
        th.Property("isinactive", th.BooleanType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("name", th.StringType),
        th.Property("parent", th.IntegerType),
    ).to_dict()

class EntityStream(suiteqlStream):
    '''
    63,770 records in NetSuite
    '''
    name = "entity"
    path = "/query/v1/suiteql"
    entity_name = "entity"
    primary_keys = ["id"]
    replication_key = "lastmodifieddate"
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("altemail", th.StringType),
        th.Property("altname", th.StringType),
        th.Property("altphone", th.StringType),
        th.Property("comments", th.StringType),
        th.Property("contact", th.IntegerType),
        th.Property("customer", th.IntegerType),
        th.Property("datecreated", th.DateTimeType),
        th.Property("email", th.StringType),
        th.Property("employee", th.IntegerType),
        th.Property("entityid", th.StringType),
        th.Property("entitynumber", th.IntegerType),
        th.Property("entitytitle", th.StringType),
        th.Property("externalid", th.StringType),
        th.Property("fax", th.StringType),
        th.Property("firstname", th.StringType),
        th.Property("group", th.IntegerType),
        th.Property("homephone", th.StringType),
        th.Property("id", th.IntegerType),
        th.Property("isinactive", th.BooleanType),
        th.Property("isperson", th.BooleanType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("lastname", th.StringType),
        th.Property("middlename", th.StringType),
        th.Property("mobilephone", th.StringType),
        th.Property("othername", th.IntegerType),
        th.Property("parent", th.IntegerType),
        th.Property("partner", th.IntegerType),
        th.Property("phone", th.StringType),
        th.Property("project", th.IntegerType),
        th.Property("salutation", th.StringType),
        th.Property("title", th.StringType),
        th.Property("toplevelparent", th.IntegerType),
        th.Property("vendor", th.IntegerType),
    ).to_dict()

class EntityAddressStream(suiteqlStream):
    '''
    37,645 records in NetSuite
    '''
    name = "entityaddress"
    path = "/query/v1/suiteql"
    entity_name = "entityaddress"
    primary_keys = ["nkey", "recordowner"]
    replication_key = "lastmodifieddate"
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("addr1", th.StringType),
        th.Property("addr2", th.StringType),
        th.Property("addr3", th.StringType),
        th.Property("addressee", th.StringType),
        th.Property("addrphone", th.StringType),
        th.Property("addrtext", th.StringType),
        th.Property("attention", th.StringType),
        th.Property("city", th.StringType),
        th.Property("country", th.StringType),
        th.Property("dropdownstate", th.StringType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("nkey", th.IntegerType),
        th.Property("override", th.BooleanType),
        th.Property("recordowner", th.IntegerType),
        th.Property("state", th.StringType),
        th.Property("zip", th.StringType),
    ).to_dict()

class ItemStream(suiteqlStream):
    '''
    171 items in NetSuite
    '''
    name = "item"
    path = "/query/v1/suiteql"
    entity_name = "item"
    primary_keys = ["id"]
    replication_key = "lastmodifieddate"
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("amortizationperiod", th.StringType),
        th.Property("amortizationtemplate", th.StringType),
        th.Property("atpmethod", th.StringType),
        th.Property("autoexpandkitforrevenuemgmt", th.BooleanType),
        th.Property("averagecost", th.StringType),
        th.Property("billexchratevarianceacct", th.IntegerType),
        th.Property("billingschedule", th.StringType),
        th.Property("billpricevarianceacct", th.IntegerType),
        th.Property("billqtyvarianceacct", th.IntegerType),
        th.Property("class", th.IntegerType),
        th.Property("cost", th.StringType),
        th.Property("costestimate", th.StringType),
        th.Property("costestimatetype", th.StringType),
        th.Property("costingmethod", th.StringType),
        th.Property("costingmethoddisplay", th.StringType),
        th.Property("countryofmanufacture", th.StringType),
        th.Property("createddate", th.DateTimeType),
        th.Property("createexpenseplanson", th.StringType),
        th.Property("createrevenueplanson", th.StringType),
        th.Property("cseg_conference", th.StringType),
        th.Property("custitem1", th.StringType),
        th.Property("custitem2", th.StringType),
        th.Property("custitem_code_of_supply", th.StringType),
        th.Property("custitem_commodity_code", th.StringType),
        th.Property("custitem_end_of_life_date", th.DateType),
        th.Property("custitem_end_of_mtce_date", th.DateType),
        th.Property("custitem_item_category", th.StringType),
        th.Property("custitem_item_pricing_type", th.StringType),
        th.Property("custitem_itr_supplementary_unit", th.StringType),
        th.Property("custitem_itr_supplementary_unit_abbrev", th.StringType),
        th.Property("custitem_maximum_quantity", th.StringType),
        th.Property("custitem_mtce_support_type", th.StringType),
        th.Property("custitem_nature_of_transaction_codes", th.StringType),
        th.Property("custitem_nspbcs_item_planning_cat", th.StringType),
        th.Property("custitem_opt_out_ms", th.BooleanType),
        th.Property("custitem_product_line", th.StringType),
        th.Property("custitem_prompt_payment_discount_item", th.BooleanType),
        th.Property("custitem_quantity_cap", th.StringType),
        th.Property("custitem_quantity_type", th.StringType),
        th.Property("custitem_renew_with", th.StringType),
        th.Property("custitem_renewals_exclusion", th.BooleanType),
        th.Property("custitem_replaced_with", th.StringType),
        th.Property("custitem_swv_cr_item_pricing_option", th.StringType),
        th.Property("custitem_type_of_goods", th.StringType),
        th.Property("custitem_un_number", th.StringType),
        th.Property("deferralaccount", th.IntegerType),
        th.Property("deferredrevenueaccount", th.IntegerType),
        th.Property("deferrevrec", th.BooleanType),
        th.Property("department", th.IntegerType),
        th.Property("description", th.StringType),
        th.Property("directrevenueposting", th.BooleanType),
        th.Property("displayname", th.StringType),
        th.Property("effectivebomcontrol", th.StringType),
        th.Property("enforceminqtyinternally", th.BooleanType),
        th.Property("expenseaccount", th.IntegerType),
        th.Property("expenseamortizationrule", th.StringType),
        th.Property("externalid", th.StringType),
        th.Property("fullname", th.StringType),
        th.Property("fxcost", th.StringType),
        th.Property("gainlossaccount", th.IntegerType),
        th.Property("generateaccruals", th.BooleanType),
        th.Property("handlingcost", th.StringType),
        th.Property("id", th.IntegerType),
        th.Property("includechildren", th.BooleanType),
        th.Property("incomeaccount", th.IntegerType),
        th.Property("intercodefrevaccount", th.IntegerType),
        th.Property("intercoexpenseaccount", th.IntegerType),
        th.Property("intercoincomeaccount", th.IntegerType),
        th.Property("isfulfillable", th.BooleanType),
        th.Property("isinactive", th.BooleanType),
        th.Property("isonline", th.BooleanType),
        th.Property("itemid", th.StringType),
        th.Property("itemrevenuecategory", th.StringType),
        th.Property("itemtype", th.StringType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("lastpurchaseprice", th.StringType),
        th.Property("location", th.IntegerType),
        th.Property("manufacturer", th.StringType),
        th.Property("matchbilltoreceipt", th.BooleanType),
        th.Property("maximumquantity", th.StringType),
        th.Property("minimumquantity", th.StringType),
        th.Property("mpn", th.StringType),
        th.Property("overallquantitypricingtype", th.StringType),
        th.Property("parent", th.IntegerType),
        th.Property("preferredstocklevel", th.StringType),
        th.Property("pricinggroup", th.StringType),
        th.Property("printitems", th.BooleanType),
        th.Property("prodpricevarianceacct", th.StringType),
        th.Property("prodqtyvarianceacct", th.StringType),
        th.Property("purchasedescription", th.StringType),
        th.Property("purchaseorderamount", th.StringType),
        th.Property("purchaseorderquantity", th.StringType),
        th.Property("purchaseorderquantitydiff", th.StringType),
        th.Property("purchasepricevarianceacct", th.StringType),
        th.Property("purchaseunit", th.StringType),
        th.Property("quantityavailable", th.StringType),
        th.Property("quantitybackordered", th.StringType),
        th.Property("quantitycommitted", th.StringType),
        th.Property("quantityonhand", th.StringType),
        th.Property("quantityonorder", th.StringType),
        th.Property("quantitypricingschedule", th.StringType),
        th.Property("receiptamount", th.StringType),
        th.Property("receiptquantity", th.StringType),
        th.Property("receiptquantitydiff", th.StringType),
        th.Property("reorderpoint", th.StringType),
        th.Property("residual", th.StringType),
        th.Property("revenueallocationgroup", th.StringType),
        th.Property("revenuerecognitionrule", th.StringType),
        th.Property("revrecforecastrule", th.StringType),
        th.Property("revreclassfxaccount", th.StringType),
        th.Property("saleunit", th.StringType),
        th.Property("scrapacct", th.StringType),
        th.Property("shipindividually", th.BooleanType),
        th.Property("shippackage", th.StringType),
        th.Property("shippingcost", th.StringType),
        th.Property("stockdescription", th.StringType),
        th.Property("stockunit", th.StringType),
        th.Property("subsidiary", th.StringType),
        th.Property("subtype", th.StringType),
        th.Property("supplyreplenishmentmethod", th.StringType),
        th.Property("totalvalue", th.StringType),
        th.Property("unbuildvarianceaccount", th.StringType),
        th.Property("unitstype", th.StringType),
        th.Property("usecomponentyield", th.BooleanType),
        th.Property("usemarginalrates", th.BooleanType),
        th.Property("vendorname", th.StringType),
        th.Property("vsoedelivered", th.BooleanType),
        th.Property("vsoepermitdiscount", th.StringType),
        th.Property("vsoeprice", th.StringType),
        th.Property("vsoesopgroup", th.StringType),
        th.Property("weight", th.StringType),
        th.Property("weightunit", th.StringType),
        th.Property("weightunits", th.StringType),
        th.Property("wipacct", th.StringType),
        th.Property("wipvarianceacct", th.StringType),
    ).to_dict()


class JobStream(suiteqlStream):
    '''
    0 records in NetSuite
    '''
    name = "job"
    path = "/query/v1/suiteql"
    entity_name = "job"
    primary_keys = ["id"]
    replication_key = "lastmodifieddate"
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("accountnumber", th.StringType),
        th.Property("alternatecontact", th.StringType),
        th.Property("altname", th.StringType),
        th.Property("altphone", th.StringType),
        th.Property("category", th.StringType),
        th.Property("comments", th.StringType),
        th.Property("companyname", th.StringType),
        th.Property("contact", th.StringType),
        th.Property("cseg_conference", th.StringType),
        th.Property("currency", th.StringType),
        th.Property("currencyprecision", th.StringType),
        th.Property("custentity_exec_alert_summary", th.StringType),
        th.Property("custentity_vat_reg_no", th.StringType),
        th.Property("customer", th.StringType),
        th.Property("datecreated", th.DateTimeType),
        th.Property("defaultbillingaddress", th.StringType),
        th.Property("defaultshippingaddress", th.StringType),
        th.Property("email", th.StringType),
        th.Property("emailpreference", th.StringType),
        th.Property("enddate", th.DateType),
        th.Property("entityid", th.StringType),
        th.Property("entitynumber", th.StringType),
        th.Property("entitystatus", th.StringType),
        th.Property("entitytitle", th.StringType),
        th.Property("estimatedrevenue", th.StringType),
        th.Property("externalid", th.StringType),
        th.Property("fax", th.StringType),
        th.Property("id", th.StringType),
        th.Property("isinactive", th.BooleanType),
        th.Property("jobtype", th.StringType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("parent", th.StringType),
        th.Property("percentcomplete", th.StringType),
        th.Property("phone", th.StringType),
        th.Property("primarycontact", th.StringType),
        th.Property("projectedenddate", th.StringType),
        th.Property("revrecforecastrule", th.StringType),
        th.Property("startdate", th.DateType),
        th.Property("usepercentcompleteoverride", th.StringType),
    ).to_dict()


class LocationStream(suiteqlStream):
    '''
    19 records in NetSuite
    '''
    name = "location"
    path = "/query/v1/suiteql"
    entity_name = "location"
    primary_keys = ["id"]
    replication_key = "lastmodifieddate"
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("externalid", th.StringType),
        th.Property("fullname", th.StringType),
        th.Property("id", th.IntegerType),
        th.Property("includechildren", th.StringType),
        th.Property("isinactive", th.StringType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("latitude", th.StringType),
        th.Property("locationtype", th.IntegerType),
        th.Property("longitude", th.StringType),
        th.Property("mainaddress", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("parent", th.IntegerType),
        th.Property("returnaddress", th.StringType),
        th.Property("subsidiary", th.StringType),
        th.Property("tranprefix", th.StringType),
    ).to_dict()


class LocationMainAddressStream(suiteqlStream):
    '''
    37,645 records in NetSuite
    '''
    name = "locationmainaddress"
    path = "/query/v1/suiteql"
    entity_name = "locationmainaddress"
    primary_keys = ["nkey", "recordowner"]
    replication_key = "lastmodifieddate"
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("addr1", th.StringType),
        th.Property("addr2", th.StringType),
        th.Property("addr3", th.StringType),
        th.Property("addressee", th.StringType),
        th.Property("addrphone", th.StringType),
        th.Property("addrtext", th.StringType),
        th.Property("attention", th.StringType),
        th.Property("city", th.StringType),
        th.Property("country", th.StringType),
        th.Property("dropdownstate", th.StringType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("nkey", th.IntegerType),
        th.Property("override", th.BooleanType),
        th.Property("recordowner", th.IntegerType),
        th.Property("state", th.StringType),
        th.Property("zip", th.StringType),
    ).to_dict()

class SubsidiaryStream(suiteqlStream):
    '''
    5 records in NetSuite
    '''
    name = "subsidiary"
    path = "/query/v1/suiteql"
    entity_name = "subsidiary"
    metadata_path = "/record/v1/metadata-catalog/subsidiary"
    primary_keys = ["id"]
    skip_attributes = ["links", "intercoaccount", "traninternalprefix", "custrecord_company_brn", "custrecord_company_uen", "custrecord_nspbcs_epm_application_name", "custrecord_nspbcs_epm_url", "custrecord_nspbcs_epm_username", "custrecord_pt_sub_taxonomy_reference", "custrecord_subsidiary_branch_id", "externalid", "fax", "purchaseorderamount", "purchaseorderquantity", "purchaseorderquantitydiff", "receiptamount", "receiptquantity", "receiptquantitydiff", "representingcustomer", "representingvendor", "returnaddress", "shippingaddress", "ssnortin", "state1taxnumber", "tranprefix" ]
    replication_key = "lastmodifieddate"
    replication_method = "INCREMENTAL"


class TransactionStream(suiteqlStream):
    '''
    1750 records in NetSuite
    '''
    name = "transaction"
    path = "/query/v1/suiteql"
    entity_name = "transaction"
    primary_keys = ["id"]
    replication_key = "lastmodifieddate"
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("abbrevtype", th.StringType),
        th.Property("accountbasednumber", th.StringType),
        th.Property("actionitem", th.StringType),
        th.Property("actualshipdate", th.DateType),
        th.Property("altsalestotal", th.StringType),
        th.Property("approvalstatus", th.IntegerType),
        th.Property("balsegstatus", th.IntegerType),
        th.Property("billingaddress", th.StringType),
        th.Property("billingstatus", th.StringType),
        th.Property("bulkprocsubmission", th.IntegerType),
        th.Property("buyingreason", th.IntegerType),
        th.Property("buyingtimeframe", th.IntegerType),
        th.Property("closedate", th.StringType),
        th.Property("createdby", th.IntegerType),
        th.Property("createddate", th.DateTimeType),
        th.Property("cseg_conference", th.IntegerType),
        th.Property("currency", th.IntegerType),
        th.Property("custbody_4110_customregnum", th.StringType),
        th.Property("custbody_4599_mx_operation_type", th.StringType),
        th.Property("custbody_4599_sg_import_permit_num", th.StringType),
        th.Property("custbody_adjustment_journal", th.StringType),
        th.Property("custbody_bill_to_tier", th.StringType),
        th.Property("custbody_cash_register", th.StringType),
        th.Property("custbody_check_log_error_info", th.StringType),
        th.Property("custbody_check_log_status", th.StringType),
        th.Property("custbody_cli_used", th.StringType),
        th.Property("custbody_comp_title", th.StringType),
        th.Property("custbody_contract_name", th.StringType),
        th.Property("custbody_contract_notes", th.StringType),
        th.Property("custbody_counterparty_vat", th.StringType),
        th.Property("custbody_country_of_origin", th.StringType),
        th.Property("custbody_cr_action_rejected_reason", th.StringType),
        th.Property("custbody_createdfrom_expensify", th.StringType),
        th.Property("custbody_date_lsa", th.DateType),
        th.Property("custbody_date_of_taxable_supply", th.DateType),
        th.Property("custbody_delivery_terms", th.StringType),
        th.Property("custbody_distributor", th.StringType),
        th.Property("custbody_doc_num_summ_invoice", th.StringType),
        th.Property("custbody_document_date", th.DateType),
        th.Property("custbody_end_user_default_ship_address", th.StringType),
        th.Property("custbody_end_user_email_address", th.StringType),
        th.Property("custbody_end_user", th.StringType),
        th.Property("custbody_esc_campaign_category", th.StringType),
        th.Property("custbody_establishment_code", th.StringType),
        th.Property("custbody_exclusivity", th.StringType),
        th.Property("custbody_ftr_manualprocessing", th.StringType),
        th.Property("custbody_futuri_title", th.StringType),
        th.Property("custbody_hidden_field", th.StringType),
        th.Property("custbody_is_renewal_rejected", th.StringType),
        th.Property("custbody_itr_doc_number", th.StringType),
        th.Property("custbody_itr_nexus", th.StringType),
        th.Property("custbody_link_lsa", th.StringType),
        th.Property("custbody_link_name_lsa", th.StringType),
        th.Property("custbody_manual_renewal", th.StringType),
        th.Property("custbody_mode_of_transport", th.StringType),
        th.Property("custbody_my_import_declaration_num", th.StringType),
        th.Property("custbody_nexus_notc", th.StringType),
        th.Property("custbody_nondeductible_processed", th.StringType),
        th.Property("custbody_nondeductible_ref_genjrnl", th.StringType),
        th.Property("custbody_notc", th.StringType),
        th.Property("custbody_order_type", th.StringType),
        th.Property("custbody_refno_originvoice", th.StringType),
        th.Property("custbody_regime_code_of_supply", th.StringType),
        th.Property("custbody_regime_code", th.StringType),
        th.Property("custbody_renewal_terms", th.StringType),
        th.Property("custbody_report_timestamp", th.StringType),
        th.Property("custbody_reseller", th.StringType),
        th.Property("custbody_rsc_500mktact", th.StringType),
        th.Property("custbody_rsc_aprvrnwlsauto", th.StringType),
        th.Property("custbody_rsc_cntrcttmplt", th.StringType),
        th.Property("custbody_rsc_compsignedby", th.StringType),
        th.Property("custbody_rsc_compsigneddate", th.DateType),
        th.Property("custbody_rsc_contract_renew_stat", th.StringType),
        th.Property("custbody_rsc_contract_status", th.StringType),
        th.Property("custbody_rsc_ftrsignedby", th.StringType),
        th.Property("custbody_rsc_ftrsigneddate", th.DateType),
        th.Property("custbody_rsc_manualrenew", th.StringType),
        th.Property("custbody_rsc_nextbilldate", th.DateType),
        th.Property("custbody_rsc_paymentmethod", th.StringType),
        th.Property("custbody_rsc_platid", th.StringType),
        th.Property("custbody_rsc_tncclause", th.StringType),
        th.Property("custbody_rssc_compsgndby", th.StringType),
        th.Property("custbody_rssc_specterms", th.StringType),
        th.Property("custbody_scn_subscription_first_inv", th.StringType),
        th.Property("custbody_ship_to_tier", th.StringType),
        th.Property("custbody_sii_accounting_date", th.DateType),
        th.Property("custbody_sii_article_61d", th.StringType),
        th.Property("custbody_sii_article_72_73", th.StringType),
        th.Property("custbody_sii_code_issued_inv", th.StringType),
        th.Property("custbody_sii_code", th.StringType),
        th.Property("custbody_sii_correction_type", th.StringType),
        th.Property("custbody_sii_exempt_details", th.StringType),
        th.Property("custbody_sii_external_reference", th.StringType),
        th.Property("custbody_sii_intra_txn_type", th.StringType),
        th.Property("custbody_sii_invoice_date", th.DateType),
        th.Property("custbody_sii_is_third_party", th.StringType),
        th.Property("custbody_sii_issued_inv_type", th.StringType),
        th.Property("custbody_sii_land_register", th.StringType),
        th.Property("custbody_sii_not_reported_in_time", th.StringType),
        th.Property("custbody_sii_operation_date", th.DateType),
        th.Property("custbody_sii_orig_bill", th.StringType),
        th.Property("custbody_sii_orig_invoice", th.StringType),
        th.Property("custbody_sii_property_location", th.StringType),
        th.Property("custbody_sii_received_inv_type", th.StringType),
        th.Property("custbody_sii_ref_no", th.StringType),
        th.Property("custbody_sii_registration_code", th.StringType),
        th.Property("custbody_sii_registration_msg", th.StringType),
        th.Property("custbody_sii_registration_status", th.StringType),
        th.Property("custbody_sii_spcl_scheme_code_purchase", th.StringType),
        th.Property("custbody_sii_spcl_scheme_code_sales", th.StringType),
        th.Property("custbody_stc_amount_after_discount", th.StringType),
        th.Property("custbody_stc_payment_transaction_id", th.StringType),
        th.Property("custbody_stc_tax_after_discount", th.StringType),
        th.Property("custbody_stc_total_after_discount", th.StringType),
        th.Property("custbody_suitesync_authorization_code", th.StringType),
        th.Property("custbody_swe_contract_id_hidden", th.StringType),
        th.Property("custbody_swe_from_contract", th.StringType),
        th.Property("custbody_swe_has_renewal_items", th.StringType),
        th.Property("custbody_swe_rma_header_end_date", th.DateType),
        th.Property("custbody_swe_rma_header_start_date", th.DateType),
        th.Property("custbody_tran_term_in_months", th.StringType),
        th.Property("custbody_transaction_region", th.StringType),
        th.Property("custbody1", th.StringType),
        th.Property("custbody2", th.StringType),
        th.Property("custbody3", th.StringType),
        th.Property("custbody4", th.StringType),
        th.Property("custbody5", th.StringType),
        th.Property("custbody6", th.StringType),
        th.Property("custbody7", th.StringType),
        th.Property("custbody8", th.StringType),
        th.Property("custbody9", th.StringType),
        th.Property("custbody10", th.DateType),
        th.Property("custbody11", th.StringType),
        th.Property("custbody12", th.DateType),
        th.Property("custbody13", th.StringType),
        th.Property("custbody14", th.StringType),
        th.Property("custbody15", th.StringType),
        th.Property("custbody16", th.StringType),
        th.Property("custbody17", th.DateType),
        th.Property("custbody18", th.DateType),
        th.Property("custbody19", th.DateType),
        th.Property("custbody20", th.DateType),
        th.Property("custbody21", th.DateType),
        th.Property("custbody22", th.DateType),
        th.Property("custbody23", th.DateType),
        th.Property("custbody24", th.DateType),
        th.Property("custbody25", th.DateType),
        th.Property("custbody26", th.StringType),
        th.Property("custbody27", th.StringType),
        th.Property("custbody28", th.StringType),
        th.Property("custbody29", th.StringType),
        th.Property("custbody30", th.StringType),
        th.Property("custbodyrsc_businesstype", th.StringType),
        #th.Property("customtype", th.StringType),
        th.Property("daysopen", th.StringType),
        th.Property("daysoverduesearch", th.StringType),
        th.Property("duedate", th.DateType),
        th.Property("email", th.StringType),
        th.Property("employee", th.IntegerType),
        th.Property("enddate", th.DateType),
        th.Property("entity", th.IntegerType),
        th.Property("entitystatus", th.IntegerType),
        th.Property("estgrossprofit", th.StringType),
        th.Property("estgrossprofitpercent", th.StringType),
        th.Property("estimatedbudget", th.StringType),
        th.Property("exchangerate", th.StringType),
        th.Property("expectedclosedate", th.DateType),
        th.Property("externalid", th.StringType),
        th.Property("fax", th.StringType),
        th.Property("firmed", th.StringType),
        th.Property("foreignamountpaid", th.StringType),
        th.Property("foreignamountunpaid", th.StringType),
        th.Property("foreignpaymentamountunused", th.StringType),
        th.Property("foreignpaymentamountused", th.StringType),
        th.Property("foreigntotal", th.StringType),
        th.Property("fulfillmenttype", th.StringType),
        th.Property("fxaltsalestotal", th.StringType),
        th.Property("fxnetaltsalestotal", th.StringType),
        th.Property("id", th.IntegerType, required=True),
        th.Property("includeinforecast", th.StringType),
        th.Property("incoterm", th.StringType),
        th.Property("intercostatus", th.StringType),
        th.Property("intercotransaction", th.StringType),
        th.Property("isbudgetapproved", th.StringType),
        th.Property("isfinchrg", th.StringType),
        th.Property("isreversal", th.StringType),
        th.Property("journaltype", th.StringType),
        th.Property("lastmodifiedby", th.IntegerType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("leadsource", th.StringType),
        th.Property("memdoc", th.StringType),
        th.Property("memo", th.StringType),
        th.Property("message", th.StringType),
        th.Property("netaltsalestotal", th.StringType),
        th.Property("nextapprover", th.StringType),
        th.Property("nextbilldate", th.DateType),
        th.Property("nexus", th.StringType),
        th.Property("number", th.NumberType),
        th.Property("opportunity", th.IntegerType),
        th.Property("ordpicked", th.StringType),
        th.Property("ordreceived", th.StringType),
        th.Property("otherrefnum", th.StringType),
        th.Property("partner", th.IntegerType),
        th.Property("paymenthold", th.StringType),
        th.Property("paymentmethod", th.IntegerType),
        th.Property("paymentoption", th.IntegerType),
        th.Property("posting", th.StringType),
        th.Property("postingperiod", th.IntegerType),
        th.Property("printedpickingticket", th.StringType),
        th.Property("probability", th.StringType),
        th.Property("projectedtotal", th.StringType),
        th.Property("rangehigh", th.StringType),
        th.Property("rangelow", th.StringType),
        th.Property("recordtype", th.StringType),
        th.Property("reversal", th.StringType),
        th.Property("reversaldate", th.DateType),
        th.Property("reversaldefer", th.StringType),
        th.Property("revision", th.StringType),
        th.Property("salesreadiness", th.StringType),
        th.Property("shipcarrier", th.StringType),
        th.Property("shipcomplete", th.StringType),
        th.Property("shipdate", th.DateType),
        th.Property("shippingaddress", th.StringType),
        th.Property("source", th.StringType),
        th.Property("startdate", th.DateType),
        th.Property("status", th.StringType),
        th.Property("terms", th.StringType),
        th.Property("title", th.StringType),
        th.Property("tosubsidiary", th.IntegerType),
        th.Property("totalcostestimate", th.StringType),
        th.Property("trandate", th.DateType),
        th.Property("trandisplayname", th.StringType),
        th.Property("tranid", th.StringType),
        th.Property("tranisvsoebundle", th.StringType),
        th.Property("type", th.StringType),
        th.Property("typebaseddocumentnumber", th.StringType),
        th.Property("userevenuearrangement", th.StringType),
        th.Property("visibletocustomer", th.StringType),
        th.Property("void", th.StringType),
        th.Property("voided", th.StringType),
        th.Property("website", th.StringType),
        th.Property("weightedtotal", th.StringType),
        th.Property("winlossreason", th.IntegerType),
    ).to_dict()


class TransactionAccountingLineStream(suiteqlStream):
    '''
    1750 records in NetSuite
    '''
    name = "transactionaccountingline"
    path = "/query/v1/suiteql"
    entity_name = "transactionaccountingline"
    primary_keys = ["transaction", "transactionline"]
    replication_key = "lastmodifieddate"
    is_sorted = True
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("account", th.IntegerType),
        th.Property("accountingbook", th.IntegerType),
        th.Property("amount", th.NumberType),
        th.Property("amountlinked", th.NumberType),
        #th.Property("amountpaid", th.NumberType),
        #th.Property("amountunpaid", th.NumberType),
        #th.Property("credit", th.NumberType),
        #th.Property("debit", th.NumberType),
        th.Property("exchangerate", th.NumberType),
        th.Property("glauditnumber", th.StringType),
        th.Property("glauditnumberdate", th.DateType),
        #th.Property("glauditnumbersequence", th.IntegerType),
        #th.Property("glauditnumbersetby", th.IntegerType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("netamount", th.NumberType),
        #th.Property("paymentamountunused", th.NumberType),
        #th.Property("paymentamountused", th.NumberType),
        th.Property("posting", th.BooleanType),
        th.Property("processedbyrevcommit", th.BooleanType),
        th.Property("transaction", th.IntegerType, required=True),
        th.Property("transactionline", th.IntegerType, required=True),
    ).to_dict()

class TransactionLineStream(suiteqlStream):
    name = "transactionline"
    path = "/query/v1/suiteql"
    entity_name = "transactionline"
    primary_keys = ["id", "transaction"]
    replication_key = "linelastmodifieddate"
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("accountinglinetype", th.StringType),
        th.Property("actualshipdate", th.DateType),
        th.Property("amortizationenddate", th.DateType),
        th.Property("amortizationresidual", th.StringType),
        th.Property("amortizationsched", th.StringType),
        th.Property("amortizstartdate", th.StringType),
        th.Property("billeddate", th.DateType),
        th.Property("billingschedule", th.IntegerType),
        th.Property("billvariancestatus", th.StringType),
        th.Property("category", th.IntegerType),
        th.Property("class", th.IntegerType),
        th.Property("cleared", th.BooleanType),
        th.Property("cleareddate", th.DateType),
        th.Property("closedate", th.StringType),
        th.Property("commitinventory", th.StringType),
        th.Property("commitmentfirm", th.BooleanType),
        th.Property("costestimate", th.NumberType),
        th.Property("costestimaterate", th.NumberType),
        th.Property("costestimatetype", th.StringType),
        th.Property("createdfrom", th.StringType),
        th.Property("creditforeignamount", th.NumberType),
        th.Property("cseg_conference", th.StringType),
        th.Property("custcol1", th.DateType),
        th.Property("custcol10", th.StringType),
        th.Property("custcol11", th.StringType),
        th.Property("custcol12", th.StringType),
        th.Property("custcol13", th.DateType),
        th.Property("custcol14", th.StringType),
        th.Property("custcol15", th.StringType),
        th.Property("custcol16", th.StringType),
        th.Property("custcol17", th.StringType),
        th.Property("custcol18", th.StringType),
        th.Property("custcol19", th.StringType),
        th.Property("custcol2", th.DateType),
        th.Property("custcol20", th.StringType),
        th.Property("custcol21", th.StringType),
        th.Property("custcol22", th.DateType),
        th.Property("custcol23", th.DateType),
        th.Property("custcol24", th.StringType),
        th.Property("custcol25", th.StringType),
        th.Property("custcol26", th.StringType),
        th.Property("custcol27", th.StringType),
        th.Property("custcol28", th.StringType),
        th.Property("custcol29", th.StringType),
        th.Property("custcol3", th.StringType),
        th.Property("custcol30", th.StringType),
        th.Property("custcol32", th.BooleanType),
        th.Property("custcol33", th.BooleanType),
        th.Property("custcol34", th.StringType),
        th.Property("custcol35", th.StringType),
        th.Property("custcol4", th.StringType),
        th.Property("custcol5", th.StringType),
        th.Property("custcol6", th.StringType),
        th.Property("custcol8", th.StringType),
        th.Property("custcol9", th.StringType),
        th.Property("custcol_5892_eutriangulation", th.BooleanType),
        th.Property("custcol_adjustment_field", th.StringType),
        th.Property("custcol_adjustment_tax_code", th.StringType),
        th.Property("custcol_billqty", th.StringType),
        th.Property("custcol_celigo_hubspot_line_id", th.StringType),
        th.Property("custcol_classline", th.StringType),
        th.Property("custcol_counterparty_vat", th.StringType),
        th.Property("custcol_country_of_origin_code", th.StringType),
        th.Property("custcol_country_of_origin_name", th.StringType),
        th.Property("custcol_customer_type", th.StringType),
        th.Property("custcol_departmentline", th.StringType),
        th.Property("custcol_emirate", th.StringType),
        th.Property("custcol_establishment_code", th.StringType),
        th.Property("custcol_expense_code_of_supply", th.StringType),
        th.Property("custcol_expense_url", th.StringType),
        th.Property("custcol_from_ci_id", th.StringType),
        th.Property("custcol_inline_discount", th.StringType),
        th.Property("custcol_list_rate", th.StringType),
        th.Property("custcol_location", th.StringType),
        th.Property("custcol_mtce_support_percent", th.StringType),
        th.Property("custcol_mtce_support_type", th.StringType),
        th.Property("custcol_nature_of_transaction_codes", th.StringType),
        th.Property("custcol_nondeductible_account", th.StringType),
        th.Property("custcol_opt_out_ms", th.BooleanType),
        th.Property("custcol_original_quantity", th.StringType),
        th.Property("custcol_renewal_reset_data", th.StringType),
        th.Property("custcol_renewals_exclusion", th.BooleanType),
        th.Property("custcol_rsc_accthielevel", th.StringType),
        th.Property("custcol_rsc_prodid", th.StringType),
        th.Property("custcol_sii_annual_prorate", th.StringType),
        th.Property("custcol_sii_exempt_line_details", th.StringType),
        th.Property("custcol_sii_service_date", th.DateType),
        th.Property("custcol_statistical_procedure_purc", th.StringType),
        th.Property("custcol_statistical_procedure_sale", th.StringType),
        th.Property("custcol_statistical_value", th.StringType),
        th.Property("custcol_statistical_value_base_curr", th.StringType),
        th.Property("custcol_suitesync_rev_rec_end", th.DateType),
        th.Property("custcol_suitesync_rev_rec_start", th.DateType),
        th.Property("custcol_swe_contract_end_date", th.DateType),
        th.Property("custcol_swe_contract_item_term_months", th.StringType),
        th.Property("custcol_swe_contract_start_date", th.DateType),
        th.Property("custcol_swe_ms_basis_amount", th.StringType),
        th.Property("custcol_swe_orig_list_rate", th.StringType),
        th.Property("custcol_swe_orig_price_level", th.StringType),
        th.Property("custcol_swe_price_level", th.StringType),
        th.Property("custcol_swv_ci_uplift", th.StringType),
        th.Property("custcol_swv_cr_ms_pricing_option", th.StringType),
        th.Property("custcol_termline", th.StringType),
        th.Property("custcol_vendor", th.StringType),
        th.Property("debitforeignamount", th.NumberType),
        th.Property("department", th.IntegerType),
        th.Property("documentnumber", th.StringType),
        th.Property("donotdisplayline", th.BooleanType),
        th.Property("eliminate", th.BooleanType),
        th.Property("entity", th.IntegerType),
        th.Property("estgrossprofit", th.NumberType),
        th.Property("estgrossprofitpercent", th.NumberType),
        th.Property("estimatedamount", th.NumberType),
        th.Property("expectedreceiptdate", th.DateType),
        th.Property("expenseaccount", th.IntegerType),
        th.Property("foreignamount", th.NumberType),
        th.Property("foreignamountpaid", th.NumberType),
        th.Property("foreignamountunpaid", th.NumberType),
        th.Property("foreignpaymentamountunused", th.NumberType),
        th.Property("foreignpaymentamountused", th.NumberType),
        th.Property("fulfillable", th.BooleanType),
        th.Property("fxamountlinked", th.NumberType),
        th.Property("fxvsoeprice", th.NumberType),
        th.Property("id", th.IntegerType, required=True),
        th.Property("invsoebundle", th.BooleanType),
        th.Property("isbillable", th.BooleanType),
        th.Property("isclosed", th.BooleanType),
        th.Property("iscogs", th.BooleanType),
        th.Property("iscustomglline", th.BooleanType),
        th.Property("isfullyshipped", th.BooleanType),
        th.Property("isfxvariance", th.BooleanType),
        th.Property("isinventoryaffecting", th.BooleanType),
        th.Property("isrevrectransaction", th.BooleanType),
        th.Property("item", th.IntegerType),
        th.Property("itemtype", th.StringType),
        th.Property("linelastmodifieddate", th.DateTimeType),
        th.Property("linesequencenumber", th.IntegerType),
        th.Property("location", th.IntegerType),
        th.Property("mainline", th.BooleanType),
        th.Property("matchbilltoreceipt", th.BooleanType),
        th.Property("memo", th.StringType),
        th.Property("needsrevenueelement", th.BooleanType),
        th.Property("netamount", th.NumberType),
        th.Property("oldcommitmentfirm", th.BooleanType),
        th.Property("orderpriority", th.StringType),
        th.Property("paymentmethod", th.IntegerType),
        th.Property("price", th.IntegerType),
        th.Property("processedbyrevcommit", th.BooleanType),
        th.Property("quantity", th.StringType),
        th.Property("quantitybackordered", th.StringType),
        th.Property("quantitybilled", th.StringType),
        th.Property("quantitycommitted", th.StringType),
        th.Property("quantityrejected", th.StringType),
        th.Property("quantityshiprecv", th.StringType),
        th.Property("rate", th.StringType),
        th.Property("rateamount", th.StringType),
        th.Property("ratepercent", th.StringType),
        th.Property("requestnote", th.StringType),
        th.Property("revenueelement", th.StringType),
        th.Property("subsidiary", th.IntegerType, required=True),
        th.Property("taxline", th.BooleanType),
        th.Property("transaction", th.IntegerType, required=True),
        th.Property("transactiondiscount", th.BooleanType),
        th.Property("transactionlinetype", th.StringType),
        th.Property("uniquekey", th.IntegerType, required=True),
        th.Property("units", th.StringType),
        th.Property("vsoedelivered", th.BooleanType),
        th.Property("vsoeisestimate", th.BooleanType),
        th.Property("vsoepermitdiscount", th.StringType),
        th.Property("vsoeprice", th.StringType),
        th.Property("vsoesopgroup", th.StringType),
    ).to_dict()

"""
class TransactionLineStream(suiteqlStream):
    name = "transactionline"
    path = "/query/v1/suiteql"
    entity_name = "transactionline"
    primary_keys = ["id", "transaction"]
    replication_key = "linelastmodifieddate"
    replication_method = "INCREMENTAL"
    schema = th.PropertiesList(
        th.Property("accountinglinetype", th.StringType),
        th.Property("actualshipdate", th.DateType),
        th.Property("amortizationenddate", th.DateType),
        th.Property("amortizationresidual", th.StringType),
        th.Property("amortizationsched", th.IntegerType),
        th.Property("amortizstartdate", th.StringType),
        th.Property("billeddate", th.DateType),
        th.Property("billingschedule", th.IntegerType),
        th.Property("billvariancestatus", th.StringType),
        th.Property("category", th.IntegerType),
        th.Property("class", th.StringType),
        th.Property("cleared", th.BooleanType),
        th.Property("cleareddate", th.DateType),
        th.Property("closedate", th.StringType),
        th.Property("commitinventory", th.IntegerType),
        th.Property("commitmentfirm", th.BooleanType),
        th.Property("costestimate", th.NumberType),
        th.Property("costestimaterate", th.NumberType),
        th.Property("costestimatetype", th.StringType),
        th.Property("createdfrom", th.IntegerType),
        th.Property("creditforeignamount", th.NumberType),
        th.Property("cseg_conference", th.IntegerType),
        th.Property("custcol1", th.DateType),
        th.Property("custcol10", th.IntegerType),
        th.Property("custcol11", th.IntegerType),
        th.Property("custcol12", th.IntegerType),
        th.Property("custcol13", th.DateType),
        th.Property("custcol14", th.IntegerType),
        th.Property("custcol15", th.IntegerType),
        th.Property("custcol16", th.StringType),
        th.Property("custcol17", th.NumberType),
        th.Property("custcol18", th.NumberType),
        th.Property("custcol19", th.NumberType),
        th.Property("custcol2", th.DateType),
        th.Property("custcol20", th.StringType),
        th.Property("custcol21", th.StringType),
        th.Property("custcol22", th.DateType),
        th.Property("custcol23", th.DateType),
        th.Property("custcol24", th.StringType),
        th.Property("custcol25", th.IntegerType),
        th.Property("custcol26", th.IntegerType),
        th.Property("custcol27", th.IntegerType),
        th.Property("custcol28", th.StringType),
        th.Property("custcol29", th.StringType),
        th.Property("custcol3", th.IntegerType),
        th.Property("custcol30", th.IntegerType),
        th.Property("custcol32", th.BooleanType),
        th.Property("custcol33", th.BooleanType),
        th.Property("custcol34", th.StringType),
        th.Property("custcol35", th.NumberType),
        th.Property("custcol4", th.StringType),
        th.Property("custcol5", th.IntegerType),
        th.Property("custcol6", th.IntegerType),
        th.Property("custcol8", th.IntegerType),
        th.Property("custcol9", th.StringType),
        th.Property("custcol_5892_eutriangulation", th.BooleanType),
        th.Property("custcol_adjustment_field", th.StringType),
        th.Property("custcol_adjustment_tax_code", th.IntegerType),
        th.Property("custcol_billqty", th.NumberType),
        th.Property("custcol_celigo_hubspot_line_id", th.StringType),
        th.Property("custcol_classline", th.IntegerType),
        th.Property("custcol_counterparty_vat", th.StringType),
        th.Property("custcol_country_of_origin_code", th.StringType),
        th.Property("custcol_country_of_origin_name", th.StringType),
        th.Property("custcol_customer_type", th.IntegerType),
        th.Property("custcol_departmentline", th.IntegerType),
        th.Property("custcol_emirate", th.IntegerType),
        th.Property("custcol_establishment_code", th.StringType),
        th.Property("custcol_expense_code_of_supply", th.IntegerType),
        th.Property("custcol_expense_url", th.StringType),
        th.Property("custcol_from_ci_id", th.StringType),
        th.Property("custcol_inline_discount", th.StringType),
        th.Property("custcol_list_rate", th.StringType),
        th.Property("custcol_location", th.StringType),
        th.Property("custcol_mtce_support_percent", th.StringType),
        th.Property("custcol_mtce_support_type", th.StringType),
        th.Property("custcol_nature_of_transaction_codes", th.StringType),
        th.Property("custcol_nondeductible_account", th.StringType),
        th.Property("custcol_opt_out_ms", th.BooleanType),
        th.Property("custcol_original_quantity", th.StringType),
        th.Property("custcol_renewal_reset_data", th.StringType),
        th.Property("custcol_renewals_exclusion", th.BooleanType),
        th.Property("custcol_rsc_accthielevel", th.IntegerType),
        th.Property("custcol_rsc_prodid", th.IntegerType),
        th.Property("custcol_sii_annual_prorate", th.NumberType),
        th.Property("custcol_sii_exempt_line_details", th.IntegerType),
        th.Property("custcol_sii_service_date", th.DateType),
        th.Property("custcol_statistical_procedure_purc", th.IntegerType),
        th.Property("custcol_statistical_procedure_sale", th.IntegerType),
        th.Property("custcol_statistical_value", th.NumberType),
        th.Property("custcol_statistical_value_base_curr", th.NumberType),
        th.Property("custcol_suitesync_rev_rec_end", th.DateType),
        th.Property("custcol_suitesync_rev_rec_start", th.DateType),
        th.Property("custcol_swe_contract_end_date", th.DateType),
        th.Property("custcol_swe_contract_item_term_months", th.NumberType),
        th.Property("custcol_swe_contract_start_date", th.DateType),
        th.Property("custcol_swe_ms_basis_amount", th.NumberType),
        th.Property("custcol_swe_orig_list_rate", th.NumberType),
        th.Property("custcol_swe_orig_price_level", th.IntegerType),
        th.Property("custcol_swe_price_level", th.IntegerType),
        th.Property("custcol_swv_ci_uplift", th.NumberType),
        th.Property("custcol_swv_cr_ms_pricing_option", th.IntegerType),
        th.Property("custcol_termline", th.IntegerType),
        th.Property("custcol_vendor", th.IntegerType),
        th.Property("debitforeignamount", th.NumberType),
        th.Property("department", th.IntegerType),
        th.Property("documentnumber", th.StringType),
        th.Property("donotdisplayline", th.BooleanType),
        th.Property("eliminate", th.BooleanType),
        th.Property("entity", th.IntegerType),
        th.Property("estgrossprofit", th.NumberType),
        th.Property("estgrossprofitpercent", th.NumberType),
        th.Property("estimatedamount", th.NumberType),
        th.Property("expectedreceiptdate", th.DateType),
        th.Property("expenseaccount", th.IntegerType),
        th.Property("foreignamount", th.NumberType),
        th.Property("foreignamountpaid", th.NumberType),
        th.Property("foreignamountunpaid", th.NumberType),
        th.Property("foreignpaymentamountunused", th.NumberType),
        th.Property("foreignpaymentamountused", th.NumberType),
        th.Property("fulfillable", th.BooleanType),
        th.Property("fxamountlinked", th.NumberType),
        th.Property("fxvsoeprice", th.NumberType),
        th.Property("id", th.IntegerType, required=True),
        th.Property("invsoebundle", th.BooleanType),
        th.Property("isbillable", th.BooleanType),
        th.Property("isclosed", th.BooleanType),
        th.Property("iscogs", th.BooleanType),
        th.Property("iscustomglline", th.BooleanType),
        th.Property("isfullyshipped", th.BooleanType),
        th.Property("isfxvariance", th.BooleanType),
        th.Property("isinventoryaffecting", th.BooleanType),
        th.Property("isrevrectransaction", th.BooleanType),
        th.Property("item", th.StringType),
        th.Property("itemtype", th.IntegerType),
        th.Property("linelastmodifieddate", th.DateTimeType),
        th.Property("linesequencenumber", th.IntegerType),
        th.Property("location", th.IntegerType),
        th.Property("mainline", th.BooleanType),
        th.Property("matchbilltoreceipt", th.BooleanType),
        th.Property("memo", th.StringType),
        th.Property("needsrevenueelement", th.BooleanType),
        th.Property("netamount", th.NumberType),
        th.Property("oldcommitmentfirm", th.BooleanType),
        th.Property("orderpriority", th.NumberType),
        th.Property("paymentmethod", th.IntegerType),
        th.Property("price", th.IntegerType),
        th.Property("processedbyrevcommit", th.BooleanType),
        th.Property("quantity", th.NumberType),
        th.Property("quantitybackordered", th.NumberType),
        th.Property("quantitybilled", th.NumberType),
        th.Property("quantitycommitted", th.NumberType),
        th.Property("quantityrejected", th.NumberType),
        th.Property("quantityshiprecv", th.NumberType),
        th.Property("rate", th.NumberType),
        th.Property("rateamount", th.NumberType),
        th.Property("ratepercent", th.NumberType),
        th.Property("requestnote", th.StringType),
        th.Property("revenueelement", th.IntegerType),
        th.Property("subsidiary", th.IntegerType, required=True),
        th.Property("taxline", th.BooleanType),
        th.Property("transaction", th.IntegerType, required=True),
        th.Property("transactiondiscount", th.BooleanType),
        th.Property("transactionlinetype", th.StringType),
        th.Property("uniquekey", th.IntegerType, required=True),
        th.Property("units", th.IntegerType),
        th.Property("vsoedelivered", th.BooleanType),
        th.Property("vsoeisestimate", th.BooleanType),
        th.Property("vsoepermitdiscount", th.StringType),
        th.Property("vsoeprice", th.NumberType),
        th.Property("vsoesopgroup", th.StringType),
    ).to_dict()
"""


class VendorStream(suiteqlStream):
    '''
    765 vendors in NetSuite
    '''
    name = "vendor"
    path = "/query/v1/suiteql"
    entity_name = "vendor"
    metadata_path = "/record/v1/metadata-catalog/vendor"
    primary_keys = ["id"]
    skip_attributes = ["links"]
    replication_key = "lastmodifieddate"
    replication_method = "INCREMENTAL"


class VendorCategoryStream(suiteqlStream):
    '''
    33 records in NetSuite
    '''
    name = "vendorcategory"
    path = "/query/v1/suiteql"
    entity_name = "vendorcategory"
    primary_keys = ["id"]
    #replication_key = "lastmodifieddate"
    schema = th.PropertiesList(
        th.Property("isinactive", th.BooleanType),
        th.Property("externalid", th.StringType),
        th.Property("istaxagency", th.BooleanType),
        th.Property("id", th.StringType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("name", th.StringType),
    ).to_dict()

class VendorTypeStream(suiteqlStream):
    '''
    12 vendor types in NetSuite
    '''
    name = "vendortype"
    path = "/query/v1/suiteql"
    entity_name = "customlist378"
    metadata_path = "/record/v1/metadata-catalog/customlist378"
    primary_keys = ["id"]
    skip_attributes = ["links"]



"""

class InvoiceStream(suiteqlStream):
    '''
    188,577 records in NetSuite
    '''
    name = "Invoice"
    entity_name = "transaction"
    path = "/query/v1/suiteql"
    metadata_path = "/record/v1/metadata-catalog/invoice"
    stream_type = (
        "CustInvc"  # When stream_type from transaction you should declare stream_type
    )
    primary_keys = ["id"]
    skip_attributes = ["links"]
    replication_key = "lastmodifieddate"
"""


class JournalEntryStream(suiteqlStream):
    '''
    27,806 records in NetSuite
    '''
    name = "journalentries"
    entity_name = "transaction"
    path = "/query/v1/suiteql"
    metadata_path = "/record/v1/metadata-catalog/journalentry"
    stream_type = (
        "Journal"  # When stream_type from transaction you should declare stream_type
    )
    primary_keys = ["id"]
    skip_attributes = ["links"]
    replication_key = "lastmodifieddate"


class EmployeeStream(suiteqlStream):
    '''
    130 records in NetSuite
    '''
    name = "employees"
    path = "/query/v1/suiteql"
    entity_name = "employee"
    metadata_path = "/record/v1/metadata-catalog/employee"
    primary_keys = ["id"]
    skip_attributes = ["links", "basewage", "basewagetype", "billingclass", "billpay", "bonustarget", "bonustargetcomment", "bonustargetpayfrequency", "bonustargettype", "commissionpaymentpreference", "compensationcurrency", "defaultjobresourcerole", "directdeposit", "eligibleforcommission", "employeeftestatus", "enabledeductionlimits", "inheritiprules", "ipaddressrule", "isjobmanager", "isjobresource", "job", "jobemploymentcategory", "laborcategory", "laborcost", "lastpaiddate", "overtimepolicy", "payfrequency", "rate", "salesrole", "startdatetimeoffcalc", "targetutilization", "terminationcategory", "terminationdetails", "terminationreason", "terminationregretted", "timeoffplan", "useperquest", "usetimedata", "workassignment", "workplace"]
    replication_key = "lastmodifieddate"
    replication_method = "INCREMENTAL"



class ProductIDStream(suiteqlStream):
    '''
    20 records in NetSuite
    '''
    name = "productids"
    path = "/query/v1/suiteql"
    entity_name = "customlist368"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("isinactive", th.BooleanType),
        th.Property("name", th.StringType),
        th.Property("recordid", th.StringType),
        th.Property("scriptid", th.StringType),
    ).to_dict()

class ProductStandingStream(suiteqlStream):
    '''
    20 records in NetSuite
    '''
    name = "productstanding"
    path = "/query/v1/suiteql"
    entity_name = "customlist248"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("isinactive", th.BooleanType),
        th.Property("name", th.StringType),
        th.Property("recordid", th.StringType),
        th.Property("scriptid", th.StringType),
    ).to_dict()

class PSMStream(suiteqlStream):
    '''
    20 records in NetSuite
    '''
    name = "psms"
    path = "/query/v1/suiteql"
    entity_name = "customlist245"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("isinactive", th.BooleanType),
        th.Property("name", th.StringType),
        th.Property("recordid", th.StringType),
        th.Property("scriptid", th.StringType),
    ).to_dict()

class ContractStatusStream(suiteqlStream):
    '''
    20 records in NetSuite
    '''
    name = "contractstatus"
    path = "/query/v1/suiteql"
    entity_name = "customlist254"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("isinactive", th.BooleanType),
        th.Property("name", th.StringType),
        th.Property("recordid", th.StringType),
        th.Property("scriptid", th.StringType),
    ).to_dict()

class ProductStatusStream(suiteqlStream):
    '''
    20 records in NetSuite
    '''
    name = "productstatus"
    path = "/query/v1/suiteql"
    entity_name = "customlist247"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("isinactive", th.BooleanType),
        th.Property("name", th.StringType),
        th.Property("recordid", th.StringType),
        th.Property("scriptid", th.StringType),
    ).to_dict()


class AccountHierarchyLevelStream(suiteqlStream):
    '''
    20 records in NetSuite
    '''
    name = "accounthierarchylevels"
    path = "/query/v1/suiteql"
    entity_name = "customlist220"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("isinactive", th.BooleanType),
        th.Property("name", th.StringType),
        th.Property("recordid", th.StringType),
        th.Property("scriptid", th.StringType),
    ).to_dict()


class AutomationSystemsStream(suiteqlStream):
    '''
    24 records in NetSuite
    '''
    name = "automationsystems"
    path = "/query/v1/suiteql"
    entity_name = "customlist227"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("isinactive", th.BooleanType),
        th.Property("name", th.StringType),
        th.Property("recordid", th.StringType),
        th.Property("scriptid", th.StringType),
    ).to_dict()



class ContractStream(suiteqlStream):
    '''
    3,651 contracts in NetSuite
    '''
    name = "contracts"
    path = "/query/v1/suiteql"
    entity_name = "customrecord_contracts"
    metadata_path = "/record/v1/metadata-catalog/customrecord_contracts"
    primary_keys = ["id"]
    skip_attributes = ["links"]
    replication_key = "lastmodified"
    replication_method = "INCREMENTAL"


class ContractItemStream(suiteqlStream):
    '''
    13,465 contract items in NetSuite
    '''
    name = "contractitems"
    path = "/query/v1/suiteql"
    entity_name = "customrecord_contract_item"
    metadata_path = "/record/v1/metadata-catalog/customrecord_contract_item"
    primary_keys = ["id"]
    skip_attributes = ["links"]
    replication_key = "lastmodified"
    replication_method = "INCREMENTAL"
