import ibm_boto3
from ibm_botocore.client import Config, ClientError

# credentials = {
#   "apikey": "gKaFIoaRKP9ad65voNRw3XgsJ57hWx9poLxeD0ZhSU-F",
#   "endpoints": "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints",
#   "iam_apikey_description": "Auto-generated for key e4c21767-2673-403d-80f9-c233861585fa",
#   "iam_apikey_name": "Service credentials-1",
#   "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer",
#   "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/e00af52f4d384d14abfcc314024b251b::serviceid:ServiceId-30cf369e-a0f7-4b92-b29b-86d141b426be",
#   "resource_instance_id": "crn:v1:bluemix:public:cloud-object-storage:global:a/e00af52f4d384d14abfcc314024b251b:38b9e2c3-3f3c-4cde-9137-37d3b296e178::"
# }

# Constants for IBM COS values
COS_ENDPOINT = "https://s3.jp-tok.cloud-object-storage.appdomain.cloud" # Current list avaiable at https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints
COS_API_KEY_ID = "gKaFIoaRKP9ad65voNRw3XgsJ57hWx9poLxeD0ZhSU-F" # eg "W00YiRnLW4a3fTjMB-odB-2ySfTrFBIQQWanc--P3byk"
COS_AUTH_ENDPOINT = "https://iam.cloud.ibm.com/identity/token"
COS_RESOURCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/e00af52f4d384d14abfcc314024b251b:38b9e2c3-3f3c-4cde-9137-37d3b296e178::" # eg "crn:v1:bluemix:public:cloud-object-storage:global:a/3bf0d9003abfb5d29761c3e97696b71c:d6f04d83-6c4f-4a62-a165-696756d63903::"

# Create resource
cos = ibm_boto3.resource("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_RESOURCE_CRN,
    ibm_auth_endpoint=COS_AUTH_ENDPOINT,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)

def get_buckets():
    print("Retrieving list of buckets")
    try:
        buckets = cos.buckets.all()
        for bucket in buckets:
            print("Bucket Name: {0}".format(bucket.name))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve list buckets: {0}".format(e))

# get_buckets()
def get_item(bucket_name, item_name):
    print("Retrieving item from bucket: {0}, key: {1}".format(bucket_name, item_name))
    try:
        file = cos.Object(bucket_name, item_name).get()
        print("File Contents: {0}".format(file["Body"].read()))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve file contents: {0}".format(e))

def delete_bucket(bucket_name):
    print("Deleting bucket: {0}".format(bucket_name))
    try:
        cos.Bucket(bucket_name).delete()
        print("Bucket: {0} deleted!".format(bucket_name))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to delete bucket: {0}".format(e))


def get_bucket_contents(bucket_name):
    print("Retrieving bucket contents from: {0}".format(bucket_name))
    try:
        files = cos.Bucket(bucket_name).objects.all()
        for file in files:
            print("Item: {0} ({1} bytes).".format(file.key, file.size))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve bucket contents: {0}".format(e))

        def multi_part_upload(bucket_name, item_name, file_path):
            try:
                print("Starting file transfer for {0} to bucket: {1}\n".format(item_name, bucket_name))
                # set 5 MB chunks
                part_size = 1024 * 1024 * 5

                # set threadhold to 15 MB
                file_threshold = 1024 * 1024 * 15

                # set the transfer threshold and chunk size
                transfer_config = ibm_boto3.s3.transfer.TransferConfig(
                    multipart_threshold=file_threshold,
                    multipart_chunksize=part_size
                )

                # the upload_fileobj method will automatically execute a multi-part upload
                # in 5 MB chunks for all files over 15 MB
                with open(file_path, "rb") as file_data:
                    cos.Object(bucket_name, item_name).upload_fileobj(
                        Fileobj=file_data,
                        Config=transfer_config
                    )

                print("Transfer for {0} Complete!\n".format(item_name))
            except ClientError as be:
                print("CLIENT ERROR: {0}\n".format(be))
            except Exception as e:
                print("Unable to complete multi-part upload: {0}".format(e))


def multi_part_upload(bucket_name, item_name, file_path):
    try:
        print("Starting file transfer for {0} to bucket: {1}\n".format(item_name, bucket_name))
        # set 5 MB chunks
        part_size = 1024 * 1024 * 5

        # set threadhold to 15 MB
        file_threshold = 1024 * 1024 * 15

        # set the transfer threshold and chunk size
        transfer_config = ibm_boto3.s3.transfer.TransferConfig(
            multipart_threshold=file_threshold,
            multipart_chunksize=part_size
        )

        # the upload_fileobj method will automatically execute a multi-part upload
        # in 5 MB chunks for all files over 15 MB
        with open(file_path, "rb") as file_data:
            cos.Object(bucket_name, item_name).upload_fileobj(
                Fileobj=file_data,
                Config=transfer_config
            )

        print("Transfer for {0} Complete!\n".format(item_name))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to complete multi-part upload: {0}".format(e))


get_buckets()

from os import listdir
from os.path import isfile, join
for f in listdir('./'):
    i = join('./', f)
    print(f)
    print(i)
    multi_part_upload("thethirdeye1901", f, join('./', f))



get_bucket_contents("thethirdeye1901")