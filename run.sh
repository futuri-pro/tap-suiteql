#!/bin/bash

cd /home/ubuntu/dagster-meltano/

source venv/bin/activate

cd /home/ubuntu/dagster-meltano/meltano-project/tap-suiteql/


/home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev --log-level=debug elt tap-suiteql --state-id all_except_transactions --exclude "trans*"."*" target-postgres

# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id account --select "account"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id accountingbook --select "accountingbook"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id accountingbooksubsidiaries --select "accountingbooksubsidiaries"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id accountingperiod --select "accountingperiod"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id accountingperiodfiscalcalendars --select "accountingperiodfiscalcalendars"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id accounttype --select "accounttype"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id classification --select "classification"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id consolidatedexchangerate --select "consolidatedexchangerate"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id currency --select "currency"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id customers --select "customers"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id department --select "department"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id entity --select "entity"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id entityaddress --select "entityaddress"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id item --select "item"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id job --select "job"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id location --select "location"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id locationmainaddress --select "locationmainaddress"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id subsidiary --select "subsidiary"."*" target-postgres

# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id vendor --select "vendor"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id vendorcategory --select "vendorcategory"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id vendortype --select "vendortype"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id journalentries --select "journalentries"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id employee --select "employee"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id productids --select "productids"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id productstanding --select "productstanding"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id psms --select "psms"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id contractstatus --select "contractstatus"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id productstatus --select "productstatus"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id accounthierarchylevels --select "accounthierarchylevels"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id automationsystems --select "automationsystems"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id contracts --select "contracts"."*" target-postgres
# /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id contractitems --select "contractitems"."*" target-postgres


TAP_SUITEQL_START_DATE="2023-08-15T00:00:00Z" /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id transaction --select "transaction"."*" target-postgres
TAP_SUITEQL_START_DATE="2023-08-15T00:00:00Z" /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id transactionaccountingline --select "transactionaccountingline"."*" target-postgres
TAP_SUITEQL_START_DATE="2023-08-15T00:00:00Z" /home/ubuntu/dagster-meltano/venv/bin/meltano --environment=dev  --log-level=debug elt tap-suiteql --state-id transactionline --select "transactionline"."*" target-postgres