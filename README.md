# umbrella-reporting-api-tools

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/derak/umbrella-reporting-api-tools)

Tools to interact with the Cisco Umbrella Reporting API V2.


# Installation

Clone this repo
```
git clone https://github.com/derak/umbrella-reporting-api-tools.git
```

Change into directory
```
cd umbrella-reporting-api-tools
```


# Setup
Add your management API key and secret as well as OrgID to the `config` file. This script uses the Umbrella management API to create a temporary access token that is then used to call the v2 reporting API. You do not need to create a reporting API key and secret.

## Get a list of identities by category type

Edit the `config` file and set `Type = Category`.

You can change the category type that you want to get identities for by editing the `SearchCategory` parameter in the `config` file.

The example below will search for all identities with requests to the `File Storage` category:
```
[SearchOptions]
SearchCategory = File Storage
```

## Get a list of identities by application name

Edit the `config` file and set `Type = Application`.

You can change the application name that you want to get identities for by editing the `SearchApplication` parameter in the `config` file.

The example below will search for all identities with requests to the `Google Drive` web application:
```
[SearchOptions]
SearchApplication = Google Drive
```

# To Run
First install required packages
```
pip3 install -r requirements.txt
```

Run script using Python 3 as you would any other Python script
```
python3 get-identities.py
```

# Run with Docker
You will first need to have [Docker](https://docs.docker.com/get-docker/) installed and running. instructions for getting started with Docker can be found [here](https://docs.docker.com/get-docker/). 

To run this script in a Docker container, you don't need to install the required packages. Simply use the following `make` commands to build and run the script.

Build Docker container
```
make build
````

Run script
```
make get-identities-by-catagory
```

# Sample Output
```
Identity                                           Type                 Requests

Blossom Network                                    network              19717
Blossom Site                                       site                 19717
Google WiFi                                        internal_network     14963
Derak Berreyesa (derak@gato.local)                 directory_user       14963
WIN10-DERAK-TES.gato.local                         directory_computer   14963
MerakiMX                                           tunnel_device        7020
```
