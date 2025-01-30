
# DATA MIGRATION
Designed and implemented an automated data migration solution to transfer physical SQL storage to Google Cloud SQL using Python, Jupyter Notebooks, and Google Cloud Platform. Streamlined the migration process by leveraging cloud technologies, ensuring scalability, accuracy, and efficiency.
## OBJECTIVE
The main focus of the project is to automate the process of data migration from the physical sql storage to cloud sql storage in one click.
### TECH STACK
- Platform Used  : Google Cloud Platform
- Language used  : Python
- IDE used       : Jupyter notebooks(Anaconda)
### STEPS TO BE FOLLOWED
- Create a backup file from physical database
- Upload the backup file into gcs bucket
- Restore the backup file from gcs bucket to cloud sql server 
### CREATE A BACKUP FILE FROM PHYSICAL DATABASE 
- Download local sql server and sql server management studio(ssdms)
- Connect the local sql server to ssdms
- Create an experimental database with some tables
- Using python 3 code to create a backup file for database and store it in destination folder





