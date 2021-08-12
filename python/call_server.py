from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

print("----------- js -------------")
result = gateway.entry_point.startListener("/Users/oliverwidder/Documents/dev/erp_doc/metafresh/code/frontend/src/containers/Calendar.js")
print(result)

print("----------- php -------------")
result = gateway.entry_point.startListener("/Users/oliverwidder/Documents/dev/erp_doc/dolibarr/scripts/contracts/email_expire_services_to_customers.php")
print(result)

print("----------- py -------------")
result = gateway.entry_point.startListener("/Users/oliverwidder/Documents/dev/erp_doc/erpnext/code/healthcare/doctype/clinical_procedure/clinical_procedure.py")
print(result)

print("----------- java -------------")
result = gateway.entry_point.startListener("/Users/oliverwidder/Documents/dev/erp_doc/axelor-open-suite/axelor-business-project/src/main/java/com/axelor/apps/businessproject/web/ProjectFolderController.java")
print(result)
