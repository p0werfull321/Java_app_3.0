import requests

# Define your Artifactory URL and API key or username/password
artifactory_url = 'http://13.52.185.193:8082/artifactor'
api_key = 'artifactory-access-token'
repo_name = 'admin'

# Upload a JAR file to Artifactory
jar_file_path = '/home/ubuntu/Java_app_3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
upload_url = f'http://13.52.185.193:8082/artifactory/example-repo-local/your/jar/file.jar'

headers = {
    'X-JFrog-Art-Api': artifactory-access-token,  # Use API key for authentication
}

with open(jar_file_path, 'rb') as jar_file:
    response = requests.put(upload_url, headers=headers, data=jar_file)

if response.status_code == 201:
    print("JAR file uploaded successfully.")
else:
    print(f"Failed to upload JAR file. Status code: {response.status_code}")
    print(response.text)
