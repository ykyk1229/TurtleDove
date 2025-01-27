from rest_framework.routers import DefaultRouter
from .views import ZabbixHostStatusViewset, ProductHostStatusViewset, ZabbixHostListViewset

zabbix_router = DefaultRouter()
zabbix_router.register(r'zabbixStatus', ZabbixHostStatusViewset, base_name="zabbixStatus")
zabbix_router.register(r'zabbixProduct', ProductHostStatusViewset, base_name="zabbixProduct")
zabbix_router.register(r'zabbixHostList', ZabbixHostListViewset, base_name="zabbixHostList")
