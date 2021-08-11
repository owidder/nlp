from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

result = gateway.entry_point.startListener("/Users/oliverwidder/Documents/dev/erp_doc/axelor-open-suite/axelor-business-project/src/main/java/com/axelor/apps/businessproject/web/ProjectFolderController.java")
print(result)

