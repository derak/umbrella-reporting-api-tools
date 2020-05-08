# umbrella-reporting-api-tools
Tools to interact with the Cisco Umbrella Reporting API V2.

## Setup
Add your management API key and secret as well as OrgID to the config file. These scripts use the Umbrella management API to create a temporary access token that is then used to call the v2 reporting API. You do not need to create a reporting API key and secret.

## Get a list of identities by category type
You can change the category type that you want to get identities for by editing  `category_type = 'File Storage'` in `identities-by-category.py`.

Run with Python 3 like so:

```
python3 identities-by-category.py
```