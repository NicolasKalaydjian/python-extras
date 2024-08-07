import requests

# instalar dpendencias: pip install requests
# permisos del token: 
#    metadata:read 

# Configurar org, token y prefijo
token = 'insertar-token'
org = 'insertar-org'
prefix = 'insertar-prefijo'

headers = {'Authorization': f'token {token}', 'Accept': 'application/vnd.github.v3+json'}

# Obtener todos los repos
def get_all_repos(org, headers):
    repos = []
    page = 1
    per_page = 100  # 0 a 100
    tipo = 'all' # private / all
    while True:
        url = f'https://api.github.com/orgs/{org}/repos?page={page}&per_page={per_page}&type={tipo}'
        response = requests.get(url, headers=headers)
        if response.status_code != 200: break
        page_repos = response.json()
        if not page_repos: break
        repos.extend(page_repos)
        page += 1
    return repos

# Los repositorios estan ordenados por fecha de creacion
all_repos = get_all_repos(org, headers)
filtered_repos = [repo for repo in all_repos if repo['name'].startswith(prefix)]
print(f"Cantidad de repositorios totales: {len(all_repos)}")
print(f"Cantidad de repositorios que empiezan con '{prefix}': {len(filtered_repos)}")

def get_student_with_permissions(repo_name):
    student_user = repo_name.removeprefix(prefix)
    url = f'https://api.github.com/repos/{org}/{repo_name}/collaborators/{student_user}/permission'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        collaborator = response.json()
        role_name = collaborator.get('role_name')
        return (student_user, role_name)
    else:
        print(f'Error: {response.status_code}')
        print(response.text)
        return (student_user, 'N/A')

print(f'Permisos para: {prefix}')
nroRepo = 1
for repo in filtered_repos:
    repo_name = repo['name']
    (username, role_name) = get_student_with_permissions(repo_name)
    print(f'  {nroRepo:<2}. Usuario: {username:<23}, Rol: {role_name}')
    nroRepo += 1