from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

result = gateway.entry_point.startListener("/Users/oliverwidder/Documents/dev/erp_doc/erpnext/code/restaurant/doctype/restaurant/restaurant.py")
print(result)
