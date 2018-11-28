from xmlrpc.client import ServerProxy

port = '8011'
URL = 'http://localhost:{}'.format(port)
db = 'CAPACITACION_BAK'
user = 'admin'
password = 'x'


uid = ServerProxy('{}/xmlrpc/2/common'.format(URL)).authenticate(db,user,password,{})
odoo = ServerProxy('{}/xmlrpc/2/object'.format(URL))
context={'lang': 'es_CR', 'tz': 'America/Costa_Rica', 'uid': uid}
"""
Hacemos el llamado a la funcion search_read el cual es uno de los metodos del ORM
"""
installed_modules = odoo.execute_kw(
    db,
    uid,
    password,
    'ir.module.module',
    'search_read',
    [[('state','=','installed')],['name']],
    {'context': context}
)
for module in installed_modules:
    print(module['name'])

"""Diccionario para crear un nuevo registro"""
# new_tecnico = {
#     'name':'Andres',
#     'birth':'1995-10-01',
#     'licencia_id':1,
#     'active':True,
#     'days_add':4
# }
# data_tecnico = odoo.execute_kw(
#     db,
#     uid,
#     password,
#     'tecnico',
#     'create',
#     [new_tecnico], {'context': context})


"""
Hacemos el llamado a la funcion search_read consultando la tabla tecnico
"""
# data_tecnico = odoo.execute_kw(db,uid,password,'tecnico','search_read', [[],['name','age']], {'context': context})
# data_tecnico = odoo.execute_kw(db,uid,password,'tecnico','search_read', [[],['name','age']], {'context': context})
#
# for module in data_tecnico:
#     # print(module['name'])
#     print(module)


"""
Documentacion
https://www.odoo.com/documentation/11.0/webservices/odoo.html
"""
