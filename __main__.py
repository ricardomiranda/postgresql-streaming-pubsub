import os

from infra.pulumi import pubsub
from infra.pulumi import services

from typing import Dict, Optional


def _parse_env_vars() -> dict:
    print('INFO: __main__._parse_dataset')

    env: Optional[str] = os.getenv('_ENV')
    location: str = os.getenv('_LOCATION', default='europe-west3')
    name: Optional[str] = os.getenv('_NAME')
    project: Optional[str] = os.getenv('_PROJECT')
    project_deploy: Optional[str] = os.getenv('_PROJECT_DEPLOY')
    suffix: Optional[str] = os.getenv('_SUFFIX')

    print('''INFO: __main__._parse_dataset returning: 
        env -> {e}; location -> {l}; name -> {name}; 
        project -> {p}; project_deploy -> {pd};
        suffix -> {s}'''.format(
        e=env,
        l=location,
        name=name,
        p=project,
        pd=project_deploy,
        s=suffix
    ))

    return {
        'env': env,
        'location': location,
        'name': name,
        'project': project,
        'project_deploy': project_deploy,
        'suffix': suffix,
    }


env_vars: dict = _parse_env_vars()


# Enable services
services.main(
    project_name=env_vars['name'],
    project_deploy=env_vars['project_deploy']
)

# Crete Pubu/Sub Topics
pubsub.main(
    env=env_vars['env'],
    project=env_vars['project'],
    project_name=env_vars['name'],
    project_deploy=env_vars['project_deploy']
)
