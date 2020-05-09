import json
import requests
import configparser

category_type = 'File Storage'

# read api creds from config
config = configparser.ConfigParser()
config.read('config')
org_id = config['Umbrella']['OrgID']
mgmt_api_key = config['Umbrella']['ManagementAPIKey']
mgmt_api_secret = config['Umbrella']['ManagementAPISecret']

# management api url, used to get access token for reporting api
mgmt_api_url = 'https://management.api.umbrella.com/auth/v2/oauth2/token'
mgmt_header = {'content-type': 'application/json'}

# reporting api url
reporting_api_url = 'https://reports.api.umbrella.com/v2'

def get_reporting_request(access_token, endpoint):
    r = requests.get(reporting_api_url+endpoint, headers={"Authorization": "Bearer %s" % access_token})
    body = json.loads(r.content)
    return body

def get_access_token():
    r = requests.get(mgmt_api_url, headers=mgmt_header, auth=(mgmt_api_key, mgmt_api_secret))
    body = json.loads(r.content)
    return body['access_token']


if __name__ == '__main__':

    # get access token
    access_token = get_access_token()

    # get list of all categories
    r = get_reporting_request(access_token, '/organizations/{}/categories'.format(org_id))

    # loop througth category list and get category id
    category_id = ''
    for i in r['data']:
        if i['label'] == category_type:
            category_id = i['id']
            break

    # get identities for specific category
    r = get_reporting_request(access_token, '/organizations/{}/top-identities?from=-30days&to=now&limit=1000&offset=0&categories={}'.format(org_id, category_id))

    # loop through and print identity name and type
    for i in r['data']:
        print('Identity: {}, Type: {}'.format(i['identity']['label'], i['identity']['type']['type']))