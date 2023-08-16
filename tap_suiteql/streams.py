"""Stream type classes for tap-suiteql."""

from singer_sdk import typing as th

from tap_suiteql.client import suiteqlStream

class AccountingBookStream(suiteqlStream):
    '''
    1 records in NetSuite
    '''
    name = "accounting_books"
    path = "/query/v1/suiteql"
    entity_name = "accountingbook"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("basebook", th.StringType),
        th.Property("contingentrevenuehandling", th.StringType),
        th.Property("effectiveperiod", th.StringType),
        th.Property("externalid", th.StringType),
        th.Property("isadjustmentonly", th.StringType),
        th.Property("isconsolidated", th.StringType),
        th.Property("isprimary", th.StringType),
        th.Property("lastmodifieddate", th.StringType),
        th.Property("name", th.StringType),
        th.Property("subsidiariesstring", th.StringType),
        th.Property("twosteprevenueallocation", th.StringType),
        th.Property("unbilledreceivablegrouping", th.StringType),
    ).to_dict()

class AccountingBookSubsidiariesStream(suiteqlStream):
    '''
    1 records in NetSuite
    '''
    name = "accountingbooksubsidiaries"
    path = "/query/v1/suiteql"
    entity_name = "accountingbooksubsidiaries"
    #primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("accountingbook", th.StringType),
        th.Property("status", th.StringType),
        th.Property("subsidiary", th.StringType),
    ).to_dict()



class AccountingPeriodStream(suiteqlStream):
    '''
    246 records in NetSuite
    '''
    name = "accounting_periods"
    path = "/query/v1/suiteql"
    entity_name = "accountingperiod"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("alllocked", th.BooleanType),
        th.Property("allownonglchanges", th.BooleanType),
        th.Property("aplocked", th.BooleanType),
        th.Property("arlocked", th.BooleanType),
        th.Property("closed", th.BooleanType),
        th.Property("closedondate", th.DateType),
        th.Property("enddate", th.DateType),
        th.Property("id", th.StringType),
        th.Property("isadjust", th.BooleanType),
        th.Property("isinactive", th.BooleanType),
        th.Property("isposting", th.BooleanType),
        th.Property("isquarter", th.BooleanType),
        th.Property("isyear", th.BooleanType),
        th.Property("lastmodifieddate", th.DateType),
        th.Property("parent", th.StringType),
        th.Property("periodname", th.StringType),
        th.Property("startdate", th.DateType),
    ).to_dict()


class AccountStream(suiteqlStream):
    '''
    366 records in NetSuite
    '''
    name = "accounts"
    path = "/query/v1/suiteql"
    entity_name = "account"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("accountsearchdisplayname", th.StringType),
        th.Property("accountsearchdisplaynamecopy", th.StringType),
        th.Property("acctnumber", th.StringType),
        th.Property("accttype", th.StringType),
        th.Property("billableexpensesacct", th.StringType),
        th.Property("cashflowrate", th.StringType),
        th.Property("category1099misc", th.StringType),
        th.Property("class", th.StringType),
        th.Property("currency", th.StringType),
        th.Property("custrecord_acct_bank_account_number", th.StringType),
        th.Property("deferralacct", th.StringType),
        th.Property("department", th.StringType),
        th.Property("description", th.StringType),
        th.Property("displaynamewithhierarchy", th.StringType),
        th.Property("eliminate", th.StringType),
        th.Property("externalid", th.StringType),
        th.Property("fullname", th.StringType),
        th.Property("generalrate", th.StringType),
        th.Property("includechildren", th.StringType),
        th.Property("inventory", th.StringType),
        th.Property("isinactive", th.StringType),
        th.Property("issummary", th.StringType),
        th.Property("lastmodifieddate", th.StringType),
        th.Property("location", th.StringType),
        th.Property("parent", th.StringType),
        th.Property("reconcilewithmatching", th.StringType),
        th.Property("revalue", th.StringType),
        th.Property("sspecacct", th.StringType),
    ).to_dict()

class ConsolidatedExchangeRateStream(suiteqlStream):
    '''
    1750 records in NetSuite
    '''
    name = "consolidated_exchange_rates"
    path = "/query/v1/suiteql"
    entity_name = "consolidatedexchangerate"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("accountingbook", th.StringType),
        th.Property("averagerate", th.StringType),
        th.Property("currentrate", th.StringType),
        th.Property("externalid", th.StringType),
        th.Property("fromcurrency", th.StringType),
        th.Property("fromsubsidiary", th.StringType),
        th.Property("historicalrate", th.StringType),
        th.Property("id", th.StringType),
        th.Property("postingperiod", th.StringType),
        th.Property("tocurrency", th.StringType),
        th.Property("tosubsidiary", th.StringType),
    ).to_dict()


class CustomerStream(suiteqlStream):
    '''
    28,318 records in NetSuite
    '''
    name = "customers"
    path = "/query/v1/suiteql"
    entity_name = "customer"
    metadata_path = "/record/v1/metadata-catalog/customer"
    primary_keys = ["id"]
    skip_attributes = ["links"]
    replication_key = "lastmodifieddate"


class ClassStream(suiteqlStream):
    '''
    33 records in NetSuite
    '''
    name = "classes"
    path = "/query/v1/suiteql"
    entity_name = "classification"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("isinactive", th.BooleanType),
        th.Property("externalid", th.StringType),
        th.Property("fullname", th.StringType),
        th.Property("includechildren", th.BooleanType),
        th.Property("id", th.StringType),
        th.Property("lastmodifiedate", th.DateType),
        th.Property("name", th.StringType),
        th.Property("parent", th.StringType),
    ).to_dict()

"""
class ItemStream(suiteqlStream):
    '''
    27,806 records in NetSuite
    '''
    name = "Item"
    entity_name = "generalizeditem"
    path = "/query/v1/suiteql"
    metadata_path = "/record/v1/metadata-catalog/noninventorysaleitem"
    stream_type = (
        "Journal"  # When stream_type from transaction you should declare stream_type
    )
    primary_keys = ["id"]
    skip_attributes = ["links"]
    replication_key = "lastmodifieddate"

"""
class ItemStream(suiteqlStream):
    '''
    169 items in NetSuite
    '''
    name = "items"
    path = "/query/v1/suiteql"
    entity_name = "item"
    primary_keys = ["id"]
    replication_key = "lastmodifieddate"
    schema = th.PropertiesList(
        th.Property("amortizationperiod", th.StringType),
        th.Property("amortizationtemplate", th.StringType),
        th.Property("atpmethod", th.StringType),
        th.Property("autoexpandkitforrevenuemgmt", th.StringType),
        th.Property("averagecost", th.StringType),
        th.Property("billexchratevarianceacct", th.StringType),
        th.Property("billingschedule", th.StringType),
        th.Property("billpricevarianceacct", th.StringType),
        th.Property("billqtyvarianceacct", th.StringType),
        th.Property("class", th.StringType),
        th.Property("cost", th.StringType),
        th.Property("costestimate", th.StringType),
        th.Property("costestimatetype", th.StringType),
        th.Property("costingmethod", th.StringType),
        th.Property("costingmethoddisplay", th.StringType),
        th.Property("countryofmanufacture", th.StringType),
        th.Property("createddate", th.StringType),
        th.Property("createexpenseplanson", th.StringType),
        th.Property("createrevenueplanson", th.StringType),
        th.Property("cseg_conference", th.StringType),
        th.Property("custitem1", th.StringType),
        th.Property("custitem2", th.StringType),
        th.Property("custitem_code_of_supply", th.StringType),
        th.Property("custitem_commodity_code", th.StringType),
        th.Property("custitem_end_of_life_date", th.StringType),
        th.Property("custitem_end_of_mtce_date", th.StringType),
        th.Property("custitem_item_category", th.StringType),
        th.Property("custitem_item_pricing_type", th.StringType),
        th.Property("custitem_itr_supplementary_unit", th.StringType),
        th.Property("custitem_itr_supplementary_unit_abbrev", th.StringType),
        th.Property("custitem_maximum_quantity", th.StringType),
        th.Property("custitem_mtce_support_type", th.StringType),
        th.Property("custitem_nature_of_transaction_codes", th.StringType),
        th.Property("custitem_nspbcs_item_planning_cat", th.StringType),
        th.Property("custitem_opt_out_ms", th.StringType),
        th.Property("custitem_product_line", th.StringType),
        th.Property("custitem_prompt_payment_discount_item", th.StringType),
        th.Property("custitem_quantity_cap", th.StringType),
        th.Property("custitem_quantity_type", th.StringType),
        th.Property("custitem_renew_with", th.StringType),
        th.Property("custitem_renewals_exclusion", th.StringType),
        th.Property("custitem_replaced_with", th.StringType),
        th.Property("custitem_swv_cr_item_pricing_option", th.StringType),
        th.Property("custitem_type_of_goods", th.StringType),
        th.Property("custitem_un_number", th.StringType),
        th.Property("deferralaccount", th.StringType),
        th.Property("deferredrevenueaccount", th.StringType),
        th.Property("deferrevrec", th.StringType),
        th.Property("department", th.StringType),
        th.Property("description", th.StringType),
        th.Property("directrevenueposting", th.StringType),
        th.Property("displayname", th.StringType),
        th.Property("effectivebomcontrol", th.StringType),
        th.Property("enforceminqtyinternally", th.StringType),
        th.Property("expenseaccount", th.StringType),
        th.Property("expenseamortizationrule", th.StringType),
        th.Property("externalid", th.StringType),
        th.Property("fullname", th.StringType),
        th.Property("fxcost", th.StringType),
        th.Property("gainlossaccount", th.StringType),
        th.Property("generateaccruals", th.StringType),
        th.Property("handlingcost", th.StringType),
        th.Property("id", th.StringType),
        th.Property("includechildren", th.StringType),
        th.Property("incomeaccount", th.StringType),
        th.Property("intercodefrevaccount", th.StringType),
        th.Property("intercoexpenseaccount", th.StringType),
        th.Property("intercoincomeaccount", th.StringType),
        th.Property("isfulfillable", th.StringType),
        th.Property("isinactive", th.StringType),
        th.Property("isonline", th.StringType),
        th.Property("itemid", th.StringType),
        th.Property("itemrevenuecategory", th.StringType),
        th.Property("itemtype", th.StringType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("lastpurchaseprice", th.StringType),
        th.Property("location", th.StringType),
        th.Property("manufacturer", th.StringType),
        th.Property("matchbilltoreceipt", th.StringType),
        th.Property("maximumquantity", th.StringType),
        th.Property("minimumquantity", th.StringType),
        th.Property("mpn", th.StringType),
        th.Property("overallquantitypricingtype", th.StringType),
        th.Property("parent", th.StringType),
        th.Property("preferredstocklevel", th.StringType),
        th.Property("pricinggroup", th.StringType),
        th.Property("printitems", th.StringType),
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
        th.Property("shipindividually", th.StringType),
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
        th.Property("usecomponentyield", th.StringType),
        th.Property("usemarginalrates", th.StringType),
        th.Property("vendorname", th.StringType),
        th.Property("vsoedelivered", th.StringType),
        th.Property("vsoepermitdiscount", th.StringType),
        th.Property("vsoeprice", th.StringType),
        th.Property("vsoesopgroup", th.StringType),
        th.Property("weight", th.StringType),
        th.Property("weightunit", th.StringType),
        th.Property("weightunits", th.StringType),
        th.Property("wipacct", th.StringType),
        th.Property("wipvarianceacct", th.StringType),
    ).to_dict()


class LocationStream(suiteqlStream):
    '''
    1750 records in NetSuite
    '''
    name = "locations"
    path = "/query/v1/suiteql"
    entity_name = "location"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("externalid", th.StringType),
        th.Property("fullname", th.StringType),
        th.Property("id", th.StringType),
        th.Property("includechildren", th.StringType),
        th.Property("isinactive", th.StringType),
        th.Property("lastmodifieddate", th.StringType),
        th.Property("latitude", th.StringType),
        th.Property("locationtype", th.StringType),
        th.Property("longitude", th.StringType),
        th.Property("mainaddress", th.StringType),
        th.Property("name", th.StringType),
        th.Property("parent", th.StringType),
        th.Property("returnaddress", th.StringType),
        th.Property("subsidiary", th.StringType),
        th.Property("tranprefix", th.StringType),
    ).to_dict()


class TransactionLineStream(suiteqlStream):
    '''
    1750 records in NetSuite
    '''
    name = "transaction_lines"
    path = "/query/v1/suiteql"
    entity_name = "transactionline"
    primary_keys = ["uniquekey"]
    replication_key = "linelastmodifieddate"
    schema = th.PropertiesList(
        th.Property("accountinglinetype", th.StringType),
        th.Property("actualshipdate", th.DateType),
        th.Property("amortizationenddate", th.DateType),
        th.Property("amortizationresidual", th.StringType),
        th.Property("amortizationsched", th.StringType),
        th.Property("amortizstartdate", th.StringType),
        th.Property("billeddate", th.DateType),
        th.Property("billingschedule", th.StringType),
        th.Property("billvariancestatus", th.StringType),
        th.Property("category", th.StringType),
        th.Property("class", th.StringType),
        th.Property("cleared", th.BooleanType),
        th.Property("cleareddate", th.DateType),
        th.Property("closedate", th.StringType),
        th.Property("commitinventory", th.StringType),
        th.Property("commitmentfirm", th.StringType),
        th.Property("costestimate", th.StringType),
        th.Property("costestimaterate", th.StringType),
        th.Property("costestimatetype", th.StringType),
        th.Property("createdfrom", th.StringType),
        th.Property("creditforeignamount", th.StringType),
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
        th.Property("debitforeignamount", th.StringType),
        th.Property("department", th.StringType),
        th.Property("documentnumber", th.StringType),
        th.Property("donotdisplayline", th.BooleanType),
        th.Property("eliminate", th.BooleanType),
        th.Property("entity", th.StringType),
        th.Property("estgrossprofit", th.StringType),
        th.Property("estgrossprofitpercent", th.StringType),
        th.Property("estimatedamount", th.StringType),
        th.Property("expectedreceiptdate", th.DateType),
        th.Property("expenseaccount", th.StringType),
        th.Property("foreignamount", th.StringType),
        th.Property("foreignamountpaid", th.StringType),
        th.Property("foreignamountunpaid", th.StringType),
        th.Property("foreignpaymentamountunused", th.StringType),
        th.Property("foreignpaymentamountused", th.StringType),
        th.Property("fulfillable", th.BooleanType),
        th.Property("fxamountlinked", th.StringType),
        th.Property("fxvsoeprice", th.StringType),
        th.Property("id", th.StringType),
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
        th.Property("itemtype", th.StringType),
        th.Property("linelastmodifieddate", th.DateTimeType),
        th.Property("linesequencenumber", th.StringType),
        th.Property("location", th.StringType),
        th.Property("mainline", th.BooleanType),
        th.Property("matchbilltoreceipt", th.BooleanType),
        th.Property("memo", th.StringType),
        th.Property("needsrevenueelement", th.BooleanType),
        th.Property("netamount", th.StringType),
        th.Property("oldcommitmentfirm", th.BooleanType),
        th.Property("orderpriority", th.StringType),
        th.Property("paymentmethod", th.StringType),
        th.Property("price", th.StringType),
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
        th.Property("subsidiary", th.StringType),
        th.Property("taxline", th.BooleanType),
        th.Property("transaction", th.StringType),
        th.Property("transactiondiscount", th.BooleanType),
        th.Property("transactionlinetype", th.StringType),
        th.Property("uniquekey", th.StringType),
        th.Property("units", th.StringType),
        th.Property("vsoedelivered", th.BooleanType),
        th.Property("vsoeisestimate", th.BooleanType),
        th.Property("vsoepermitdiscount", th.StringType),
        th.Property("vsoeprice", th.StringType),
        th.Property("vsoesopgroup", th.StringType),
    ).to_dict()

class TransactionStream(suiteqlStream):
    '''
    1750 records in NetSuite
    '''
    name = "transactions"
    path = "/query/v1/suiteql"
    entity_name = "transaction"
    primary_keys = ["id"]
    replication_key = "lastmodifieddate"
    schema = th.PropertiesList(
        th.Property("abbrevtype", th.StringType),
        th.Property("accountbasednumber", th.StringType),
        th.Property("actionitem", th.StringType),
        th.Property("actualshipdate", th.DateType),
        th.Property("altsalestotal", th.StringType),
        th.Property("approvalstatus", th.StringType),
        th.Property("balsegstatus", th.StringType),
        th.Property("billingaddress", th.StringType),
        th.Property("billingstatus", th.StringType),
        th.Property("bulkprocsubmission", th.StringType),
        th.Property("buyingreason", th.StringType),
        th.Property("buyingtimeframe", th.StringType),
        th.Property("closedate", th.StringType),
        th.Property("createdby", th.StringType),
        th.Property("createddate", th.DateTimeType),
        th.Property("cseg_conference", th.StringType),
        th.Property("currency", th.StringType),
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
        th.Property("customtype", th.StringType),
        th.Property("daysopen", th.StringType),
        th.Property("daysoverduesearch", th.StringType),
        th.Property("duedate", th.DateType),
        th.Property("email", th.StringType),
        th.Property("employee", th.StringType),
        th.Property("enddate", th.DateType),
        th.Property("entity", th.StringType),
        th.Property("entitystatus", th.StringType),
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
        th.Property("id", th.StringType),
        th.Property("includeinforecast", th.StringType),
        th.Property("incoterm", th.StringType),
        th.Property("intercostatus", th.StringType),
        th.Property("intercotransaction", th.StringType),
        th.Property("isbudgetapproved", th.StringType),
        th.Property("isfinchrg", th.StringType),
        th.Property("isreversal", th.StringType),
        th.Property("journaltype", th.StringType),
        th.Property("lastmodifiedby", th.StringType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("leadsource", th.StringType),
        th.Property("memdoc", th.StringType),
        th.Property("memo", th.StringType),
        th.Property("message", th.StringType),
        th.Property("netaltsalestotal", th.StringType),
        th.Property("nextapprover", th.StringType),
        th.Property("nextbilldate", th.DateType),
        th.Property("nexus", th.StringType),
        th.Property("number", th.StringType),
        th.Property("opportunity", th.StringType),
        th.Property("ordpicked", th.StringType),
        th.Property("ordreceived", th.StringType),
        th.Property("otherrefnum", th.StringType),
        th.Property("partner", th.StringType),
        th.Property("paymenthold", th.StringType),
        th.Property("paymentmethod", th.StringType),
        th.Property("paymentoption", th.StringType),
        th.Property("posting", th.StringType),
        th.Property("postingperiod", th.StringType),
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
        th.Property("tosubsidiary", th.StringType),
        th.Property("totalcostestimate", th.StringType),
        th.Property("trandate", th.DateType),
        th.Property("trandisplayname", th.StringType),
        th.Property("tranid", th.StringType),
        th.Property("tranisvsoebundle", th.StringType),
        th.Property("number", th.StringType),
        th.Property("type", th.StringType),
        th.Property("typebaseddocumentnumber", th.StringType),
        th.Property("userevenuearrangement", th.StringType),
        th.Property("visibletocustomer", th.StringType),
        th.Property("void", th.StringType),
        th.Property("voided", th.StringType),
        th.Property("website", th.StringType),
        th.Property("weightedtotal", th.StringType),
        th.Property("winlossreason", th.StringType),
    ).to_dict()



class VendorStream(suiteqlStream):
    '''
    765 vendors in NetSuite
    '''
    name = "vendors"
    path = "/query/v1/suiteql"
    entity_name = "vendor"
    metadata_path = "/record/v1/metadata-catalog/vendor"
    primary_keys = ["id"]
    skip_attributes = ["links"]
    replication_key = "lastmodifieddate"

class VendorTypeStream(suiteqlStream):
    '''
    12 vendor types in NetSuite
    '''
    name = "vendor_types"
    path = "/query/v1/suiteql"
    entity_name = "customlist378"
    metadata_path = "/record/v1/metadata-catalog/customlist378"
    primary_keys = ["id"]
    skip_attributes = ["links"]


class CurrencyStream(suiteqlStream):
    '''
    20 records in NetSuite
    '''
    name = "currencies"
    path = "/query/v1/suiteql"
    entity_name = "currency"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("currencyprecision", th.StringType),
        th.Property("displaysymbol", th.StringType),
        th.Property("exchangerate", th.StringType),
        th.Property("id", th.StringType),
        th.Property("includeinfxrateupdates", th.BooleanType),
        th.Property("isbasecurrency", th.BooleanType),
        th.Property("isinactive", th.BooleanType),
        th.Property("lastmodifieddate", th.DateType),
        th.Property("name", th.StringType),
        th.Property("overridecurrencyformat", th.BooleanType),
        th.Property("symbol", th.StringType),
        th.Property("symbolplacement", th.StringType),
    ).to_dict()


class DepartmentStream(suiteqlStream):
    '''
    26 records in NetSuite
    '''
    name = "departments"
    path = "/query/v1/suiteql"
    entity_name = "department"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("externalid", th.StringType),
        th.Property("fullname", th.StringType),
        th.Property("id", th.StringType),
        th.Property("includechildren", th.BooleanType),
        th.Property("isinactive", th.BooleanType),
        th.Property("lastmodifieddate", th.DateType),
        th.Property("name", th.StringType),
        th.Property("parent", th.StringType),
    ).to_dict()

class EntityStream(suiteqlStream):
    '''
    65000 records in NetSuite
    '''
    name = "entities"
    path = "/query/v1/suiteql"
    entity_name = "entity"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("altemail", th.StringType),
        th.Property("altname", th.StringType),
        th.Property("altphone", th.StringType),
        th.Property("comments", th.StringType),
        th.Property("contact", th.StringType),
        th.Property("customer", th.StringType),
        th.Property("datecreated", th.StringType),
        th.Property("email", th.StringType),
        th.Property("employee", th.StringType),
        th.Property("entityid", th.StringType),
        th.Property("entitynumber", th.StringType),
        th.Property("entitytitle", th.StringType),
        th.Property("externalid", th.StringType),
        th.Property("fax", th.StringType),
        th.Property("firstname", th.StringType),
        th.Property("group", th.StringType),
        th.Property("homephone", th.StringType),
        th.Property("id", th.StringType),
        th.Property("isinactive", th.StringType),
        th.Property("isperson", th.StringType),
        th.Property("lastmodifieddate", th.StringType),
        th.Property("lastname", th.StringType),
        th.Property("middlename", th.StringType),
        th.Property("mobilephone", th.StringType),
        th.Property("othername", th.StringType),
        th.Property("parent", th.StringType),
        th.Property("partner", th.StringType),
        th.Property("phone", th.StringType),
        th.Property("project", th.StringType),
        th.Property("salutation", th.StringType),
        th.Property("title", th.StringType),
        th.Property("toplevelparent", th.StringType),
        th.Property("vendor", th.StringType),
    ).to_dict()

class SubsidiaryStream(suiteqlStream):
    '''
    26 records in NetSuite
    '''
    name = "subsidiaries"
    path = "/query/v1/suiteql"
    entity_name = "subsidiary"
    metadata_path = "/record/v1/metadata-catalog/subsidiary"
    primary_keys = ["id"]
    skip_attributes = ["links", "intercoaccount", "traninternalprefix", "custrecord_company_brn", "custrecord_company_uen", "custrecord_nspbcs_epm_application_name", "custrecord_nspbcs_epm_url", "custrecord_nspbcs_epm_username", "custrecord_pt_sub_taxonomy_reference", "custrecord_subsidiary_branch_id", "externalid", "fax", "purchaseorderamount", "purchaseorderquantity", "purchaseorderquantitydiff", "receiptamount", "receiptquantity", "receiptquantitydiff", "representingcustomer", "representingvendor", "returnaddress", "shippingaddress", "ssnortin", "state1taxnumber", "tranprefix" ]
    replication_key = "lastmodifieddate"


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



"""

class ConsolidatedExchangeRateStream(suiteqlStream):
    '''
    1,750 records in NetSuite
    '''
    name = "ConsolidatedExchangeRate"
    path = "/query/v1/suiteql"
    metadata_path = "/record/v1/metadata-catalog/consolidatedexchangerate"
    primary_keys = ["id"]
    skip_attributes = ["links"]
    replication_key = "lastmodifieddate"


class ExpenseAccountStream(suiteqlStream):
    '''
    1,505,779 records in NetSuite
    '''
    name = "ExpenseAccount"
    entity_name = "transaction"
    path = "/query/v1/suiteql"
    metadata_path = "/record/v1/metadata-catalog/transactionline"
    stream_type = (
        "CustInvc"  # When stream_type from transaction you should declare stream_type
    )
    primary_keys = ["id"]
    skip_attributes = ["links"]
    replication_key = "lastmodifieddate"



class SubscriptionLineStream(suiteqlStream):
    name = "SubscriptionLine"
    path = "/query/v1/suiteql"
    metadata_path = "/record/v1/metadata-catalog/subscriptionline"
    primary_keys = ["id"]
    skip_attributes = ["links"]
    replication_key = "lastmodifieddate"


class SubscriptionPriceIntervalStream(suiteqlStream):
    name = "SubscriptionPriceInterval"
    path = "/query/v1/suiteql"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("catalogtype", th.StringType),
        th.Property("chargetype", th.StringType),
        th.Property("enddate", th.DateTimeType),
        th.Property("frequency", th.StringType),
        th.Property("id", th.StringType),
        th.Property("item", th.StringType),
        th.Property("linenumber", th.StringType),
        th.Property("priceplan", th.StringType),
        th.Property("prorateby", th.StringType),
        th.Property("proratebyoption", th.StringType),
        th.Property("quantity", th.StringType),
        th.Property("recurringamount", th.StringType),
        th.Property("repeatevery", th.StringType),
        th.Property("startdate", th.DateTimeType),
        th.Property("startoffsetvalue", th.StringType),
        th.Property("status", th.StringType),
        th.Property("subscription", th.StringType),
        th.Property("discount", th.StringType),
        th.Property("discountamount", th.StringType),
        th.Property("discountpercent", th.StringType),
    ).to_dict()


class SubscriptionPlanStream(suiteqlStream):
    name = "SubscriptionPlan"
    path = "/query/v1/suiteql"
    metadata_path = "/record/v1/metadata-catalog/subscriptionplan"
    primary_keys = ["id"]
    replication_key = "lastmodifieddate"
    skip_attributes = [
        "links",
        "incomeAccount",
    ]  # should match metadata endpoint attribute name



class CustomerPaymentStream(suiteqlStream):
    '''
    177,921 records in NetSuite
    '''
    name = "CustomerPayment"
    path = "/query/v1/suiteql"
    entity_name = "transaction"
    stream_type = "CustPymt"
    primary_keys = ["id"]
    replication_key = "lastmodifieddate"
    schema = th.PropertiesList(
        th.Property("abbrevtype", th.StringType),
        th.Property("balsegstatus", th.StringType),
        th.Property("billingstatus", th.StringType),
        th.Property("closedate", th.DateTimeType),
        th.Property("createdby", th.StringType),
        th.Property("createddate", th.DateTimeType),
        th.Property("currency", th.StringType),
        th.Property("daysopen", th.StringType),
        th.Property("entity", th.StringType),
        th.Property("exchangerate", th.StringType),
        th.Property("foreignpaymentamountunused", th.StringType),
        th.Property("foreignpaymentamountused", th.StringType),
        th.Property("foreigntotal", th.StringType),
        th.Property("id", th.StringType),
        th.Property("includeinforecast", th.StringType),
        th.Property("isfinchrg", th.StringType),
        th.Property("isreversal", th.StringType),
        th.Property("lastmodifiedby", th.StringType),
        th.Property("lastmodifieddate", th.DateTimeType),
        th.Property("legacytax", th.StringType),
        th.Property("number", th.StringType),
        th.Property("onetime", th.StringType),
        th.Property("ordpicked", th.StringType),
        th.Property("paymenthold", th.StringType),
        th.Property("posting", th.StringType),
        th.Property("postingperiod", th.StringType),
        th.Property("printedpickingticket", th.StringType),
        th.Property("recordtype", th.StringType),
        th.Property("recurannually", th.StringType),
        th.Property("recurmonthly", th.StringType),
        th.Property("recurquarterly", th.StringType),
        th.Property("recurweekly", th.StringType),
        th.Property("status", th.StringType),
        th.Property("taxdetailsoverride", th.StringType),
        th.Property("taxpointdateoverride", th.StringType),
        th.Property("taxregoverride", th.StringType),
        th.Property("trandate", th.DateTimeType),
        th.Property("trandisplayname", th.StringType),
        th.Property("tranid", th.StringType),
        th.Property("transactionnumber", th.StringType),
        th.Property("type", th.StringType),
        th.Property("typebaseddocumentnumber", th.StringType),
        th.Property("userevenuearrangement", th.StringType),
        th.Property("visibletocustomer", th.StringType),
        th.Property("void", th.StringType),
        th.Property("voided", th.StringType),
    ).to_dict()
"""


