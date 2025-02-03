import google.auth
from googleapiclient.discovery import build
from google.oauth2 import service_account
credentials_path = ‘Path of the json key file '
credentials = service_account.Credentials.from_service_account_file(credentials_path)
project_id = ‘Project id name'
instance_id = ‘Instance id name'
bucket_name = ‘Bucket name'
file_name = ‘Backup file name'
database_name = ‘Database name'
service = build('sqladmin', 'v1beta4', credentials=credentials)
def import_file_from_gcs(project_id, instance_id, bucket_name, file_name, database_name):
    import_body = {
        'importContext': {
            'fileType': 'BAK',
            'uri': f'gs://{bucket_name}/{file_name}',
            'database': database_name
        }
    }
    request = service.instances().import_(project=project_id, instance=instance_id, body=import_body)
    response = request.execute()
    operation_name = response['name']
    operation_request = service.operations().get(project=project_id, operation=operation_name)
    print(response)
    print(f'Successfully imported file {file_name} to database {database_name} in Cloud SQL instance {instance_id}')
import_file_from_gcs(project_id, instance_id, bucket_name, file_name, database_name)

