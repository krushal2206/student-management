import xmlrpc.client

data_url = 'http://localhost:8069' # odoo instance url
database = 'my_db' # database name
user = 'admin' # username
password = '1a1061625b74ca7c80a8df9385dbf3883fe14be6' # api key
common_auth = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(data_url))
uid = common_auth.authenticate(database, user, password, {})
print("Connection Successfull. UID",uid)

data_model = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(data_url))
print(data_model)

search_admission_conf_ids = data_model.execute_kw(database, uid, password, 'school.management', 'search',[[['student_name', '=', "Krushal Kalkani"]]])
# search_admission_conf_ids = data_model.execute_kw(database, uid, password, 'students.profile', 'search_count',[[['admission_status', '=', 'Confirmed']]])
# search_admission_conf_ids_limit = data_model.execute_kw(database, uid, password, 'student.management', 'search_count',[[['student_name', '=', 'Kevin']]] , {'limit': 1})
# search_admission_conf_ids_offset = data_model.execute_kw(database, uid, password, 'student.management', 'search',[[['student_name', '=', 'Kevin']]] , {'offset': 2})
print(search_admission_conf_ids)
print("*****************")
# print(search_admission_conf_ids_limit)
# print("*****************")
# print(search_admission_conf_ids_offset)
# print("*****************")
# read_particular_field = data_model.execute_kw(database, uid, password, 'students.profile', 'read',[search_admission_conf_ids], {'fields': ['name', 'standard']})
# print(read_particular_field)
# print("*****************")
# search_and_read = data_model.execute_kw(database, uid, password, 'students.profile', 'search_read',[[['admission_status', '=', 'Confirmed']]], {'fields': ['name', 'standard']})
# print(search_and_read)
# print("*****************")