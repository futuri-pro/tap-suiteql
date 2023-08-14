"""Stream type classes for tap-suiteql."""

from singer_sdk import typing as th

from tap_suiteql.client import suiteqlStream

class AccountingBookStream(suiteqlStream):
    '''
    1 records in NetSuite
    '''
    name = "AccountingBook"
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
    name = "AccountingBookSubsidiaries"
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
    name = "AccountingPeriod"
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
    name = "Account"
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


class CustomerStream(suiteqlStream):
    '''
    28,318 records in NetSuite
    '''
    name = "Customer"
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
    name = "Class"
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
    name = "Item"
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



class VendorStream(suiteqlStream):
    '''
    765 vendors in NetSuite
    '''
    name = "Vendor"
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
    name = "VendorType"
    path = "/query/v1/suiteql"
    entity_name = "customlist378"
    metadata_path = "/record/v1/metadata-catalog/customlist378"
    primary_keys = ["id"]
    skip_attributes = ["links"]


class CurrencyStream(suiteqlStream):
    '''
    20 records in NetSuite
    '''
    name = "Currency"
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

"""
class LocationStream(suiteqlStream):
    '''
    19 records in NetSuite
    '''
    name = "Location"
    path = "/query/v1/suiteql"
    entity_name = "location"
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
"""

class DepartmentStream(suiteqlStream):
    '''
    26 records in NetSuite
    '''
    name = "Department"
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
    name = "Entity"
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
    name = "Subsidiary"
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
    name = "JournalEntry"
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
    name = "Employee"
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
    name = "ProductID"
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
    name = "ProductStanding"
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
    name = "PSM"
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
    name = "ContractStatus"
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
    name = "ProductStatus"
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
    name = "AccountHierarchyLevel"
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
    name = "AutomationSystems"
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
    name = "Contract"
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
    name = "ContractItem"
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


