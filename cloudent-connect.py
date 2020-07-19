# Use CouchDB to create a CouchDB client
# from cloudant.client import CouchDB
# client = CouchDB(USERNAME, PASSWORD, url='http://127.0.0.1:5984', connect=True)

# Use Cloudant to create a Cloudant client using account
from cloudant.client import Cloudant

credential_ = {
  "apikey": "VeKsYuRFRFt6wRUaBbN7BeaEK9eNSl133JiAg0jVvqX1",
  "host": "43fdafdd-c981-4d94-ae11-e7a0e2559071-bluemix.cloudantnosqldb.appdomain.cloud",
  "iam_apikey_description": "Auto-generated for key d7285fd2-3662-46ff-b440-eb621966386d",
  "iam_apikey_name": "Service credentials-1",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/f4b50f58334e4fe7b7814d27cc60278c::serviceid:ServiceId-3ebd4f53-5305-4a71-98f0-6a878197c7ac",
  "password": "bf95666de7a829ea0352f76108937e9ee9d8d6cf17698628d9e9f638ff17f64b",
  "port": 443,
  "url": "https://43fdafdd-c981-4d94-ae11-e7a0e2559071-bluemix:bf95666de7a829ea0352f76108937e9ee9d8d6cf17698628d9e9f638ff17f64b@43fdafdd-c981-4d94-ae11-e7a0e2559071-bluemix.cloudantnosqldb.appdomain.cloud",
  "username": "43fdafdd-c981-4d94-ae11-e7a0e2559071-bluemix"
}

# Create client using auto_renew to automatically renew expired cookie auth

client = Cloudant(credential_["username"],
                  credential_["password"],
                  url=credential_["url"],
                  connect=True,
                  auto_renew=True)
# or using url
# client = Cloudant(USERNAME, PASSWORD, url='https://acct.cloudant.com')

# or with a 429 replay adapter that includes configured retries and initial backoff
# client = Cloudant(USERNAME, PASSWORD, account=ACCOUNT_NAME,
#                   adapter=Replay429Adapter(retries=10, initialBackoff=0.01))

# or with a connect and read timeout of 5 minutes
# client = Cloudant(USERNAME, PASSWORD, account=ACCOUNT_NAME,
#                   timeout=300)

# Perform client tasks...

# Create a database using an initialized client
# The result is a new CloudantDatabase or CouchDatabase based on the client
my_database = client.create_database('my_database')

# You can check that the database exists
if my_database.exists():
    print('SUCCESS!!')

session = client.session()
print('Username: {0}'.format(session['userCtx']['name']))
print('Databases: {0}'.format(client.all_dbs()))

# Disconnect from the server
client.disconnect()
