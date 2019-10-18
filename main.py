import netbrain_restful_lib
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""Define global variables"""
user = "AAAAAAAAA"
pwd = "BBBBBBBB"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
nb_url = "https://demo6.netbraintech.com"
base_url = "https://demo6.netbraintech.com/ServicesAPI/API"

"""login and get token"""
token = netbrain_restful_lib.loginSession(nb_url, user, pwd)

"""get tenant list and print it"""
tenantList = netbrain_restful_lib.getTenants(nb_url, token)
print(tenantList)

"""Assign tenantId to Initial Tenant and print it"""
CurrentTenant = tenantList[0]
tenantId = CurrentTenant['tenantId']
print (tenantId)

"""Get Domains List, find 'Demo6' and assign it"""
domainList = netbrain_restful_lib.getDomains(nb_url, token, tenantId)
print(domainList)
for domain in domainList:
    if 'Demo6' in  domain['domainName']:
        domainId = domain['domainId']

print(domainId)

"""Set working domain to Demo6"""
loginDomain = netbrain_restful_lib.loginDomain(nb_url, token, tenantId, domainId)
print (loginDomain)



print(netbrain_restful_lib.logoutSession(nb_url, token))




