import requests

# instalar dpendencias: pip install requests
# permisos del token: 
#    metadata:read administration:write

# Configurar org, token y prefijo
token = 'insertar-token-de-acceso'
org = 'pdep-sm'
prefix = '2024-parcial-funcional-'

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

def change_permission_to_read(nroRepo, repo_name):
    student_name = repo_name.removeprefix(prefix)
    url = f'https://api.github.com/repos/{org}/{repo_name}/collaborators/{student_name}'
    # Datos para cambiar el permiso
    pull = {"permission": "pull"}  # 'pull' = 'read'
    push = {"permission": "push"}  # 'push' = 'write'
    # Seleccionar permiso
    permiso_nuevo = pull
    response = requests.put(url, headers=headers, json=permiso_nuevo)
    if response.status_code == 204:
        print(f'{nroRepo:<2}. Permisos de {student_name} cambiados a {permiso_nuevo.get('permission')}.')
    else:
        print(f'Error: {response.status_code}')
        print(response.text)        

print(f'Permisos para: {prefix}')
nroRepo = 1
for repo in filtered_repos:
    repo_name = repo['name']
    change_permission_to_read(nroRepo, repo_name)
    nroRepo += 1