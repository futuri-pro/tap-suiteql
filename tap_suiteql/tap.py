"""suiteql tap class."""
import json
import os
from typing import Any, List

from singer_sdk import Tap
from singer_sdk import typing as th

from tap_suiteql.query_builder import QueryBuilder  # JSON schema typing helpers
from tap_suiteql.schema_builder import SchemaBuilder
from tap_suiteql.streams import (
    AccountHierarchyLevelStream,
    AccountStream,
    AccountingBookStream,
    AccountingBookSubsidiariesStream,
    AccountingPeriodStream,
    AccountingPeriodFiscalCalendarsStream,
    AccountTypeStream,
    AutomationSystemsStream,
    ClassificationStream,
    ConsolidatedExchangeRateStream,
    ContractStatusStream,
    ContractStream,
    CurrencyStream,
    ContractItemStream,
    CustomerStream,
    DepartmentStream,
    EmployeeStream,
    EntityStream,
    EntityAddressStream,
    #InvoiceStream,
    ItemStream,
    JournalEntryStream,
    LocationStream,
    LocationMainAddressStream,
    PSMStream,
    ProductIDStream,
    ProductStandingStream,
    ProductStatusStream,
    SubsidiaryStream,
    TransactionStream,
    TransactionLineStream,
    VendorStream,
    VendorCategoryStream,
    VendorTypeStream,
)

STREAM_TYPES = {
    "AccountHierarchyLevel": AccountHierarchyLevelStream,
    "Account": AccountStream,
    "AccountingBook": AccountingBookStream,
    "AccountingBookSubsidiaries": AccountingBookSubsidiariesStream,
    "AccountingPeriod": AccountingPeriodStream,
    "AccountingPeriodFiscalCalendars": AccountingPeriodFiscalCalendarsStream,
    "AccountType": AccountTypeStream,
    "AutomationSystems": AutomationSystemsStream,
    "Classification": ClassificationStream,
    "ConsolidatedExchangeRate": ConsolidatedExchangeRateStream,
    "ContractStatus": ContractStatusStream,
    "Contract": ContractStream,
    "Currency": CurrencyStream,
    "ContractItem": ContractItemStream,
    "Customer": CustomerStream,
    "Department": DepartmentStream,
    "Employee": EmployeeStream,
    "Entity": EntityStream,
    "EntityAddress": EntityAddressStream,
    #"Invoice": InvoiceStream,
    "Item": ItemStream,
    "JournalEntry": JournalEntryStream,
    "Location": LocationStream,
    "LocationMainAddress": LocationMainAddressStream,
    "PSM": PSMStream,
    "ProductID": ProductIDStream,
    "ProductStanding": ProductStandingStream,
    "ProductStatus": ProductStatusStream,
    "Subsidiary": SubsidiaryStream,
    "Transaction": TransactionStream,
    "TransactionLine": TransactionLineStream,
    "Vendor": VendorStream,
    "VendorCategory": VendorCategoryStream,
    "VendorType": VendorTypeStream,
}

class Tapsuiteql(Tap):
    """suiteql tap class."""

    name = "tap-suiteql"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "start_date",
            th.StringType,
            required=True,
        ),
        th.Property(
            "consumer_secret",
            th.StringType,
            required=True,
        ),
        th.Property(
            "consumer_key",
            th.StringType,
            required=True,
        ),
        th.Property(
            "token_id",
            th.StringType,
            required=True,
        ),
        th.Property(
            "token_secret",
            th.StringType,
            required=True,
        ),
        th.Property(
            "account_id",
            th.StringType,
            required=True,
        ),
        th.Property(
            "base_url",
            th.StringType,
            description="The url for the API service",
            required=True,
        ),
    ).to_dict()

    def get_stream_types(self) -> List[Any]:
        stream_types: Any = []
        select_statement = json.loads(os.environ.get("TAP_SUITEQL__SELECT", '["*.*"]'))

        if select_statement == ["*.*"]:
            stream_types = STREAM_TYPES.values()
        else:
            stream_types = [
                STREAM_TYPES.get(s.replace(".*", "")) for s in select_statement
            ]

        return stream_types

    def discover_streams(self) -> List[Any]:
        """Return a list of discovered streams."""

        stream_classes: List[Any] = []

        for stream_class in self.get_stream_types():
            schema = SchemaBuilder(stream_class(tap=self)).schema()
            body_query = QueryBuilder(stream_class(tap=self, schema=schema)).query()

            stream_classes.append(
                stream_class(tap=self, schema=schema, body_query=body_query)
            )

        return stream_classes
