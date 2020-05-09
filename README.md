# umbrella-reporting-api-tools
Tools to interact with the Cisco Umbrella Reporting API V2.

## Setup
Add your management API key and secret as well as OrgID to the `config` file. These scripts use the Umbrella management API to create a temporary access token that is then used to call the v2 reporting API. You do not need to create a reporting API key and secret.

## Get a list of identities by category type
You can change the category type that you want to get identities for by editing the `SearchCatagory` parameter in the `config` file.

The example below will searh for all identities with requests to the `File Storage` category
```
[SearchOptions]
SearchCatagory = File Storage
```

Run with Python 3 like so:
```
python3 identities-by-category.py
```

Sample Output
```
Identity                                           Type                 Requests

Blossom Network                                    network              19717
Blossom Site                                       site                 19717
Google WiFi                                        internal_network     14963
Derak Berreyesa (derak@gato.local)                 directory_user       14963
WIN10-DERAK-TES.gato.local                         directory_computer   14963
MerakiMX                                           tunnel_device        7020
```