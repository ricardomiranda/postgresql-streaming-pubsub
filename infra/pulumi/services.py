import os

import pulumi_gcp as gcp

from typing import Dict


def main(project_name: str, project_deploy: str) -> None:
    print('INFO: infra.pulumi.pubsub.main')

    pubsub = gcp.projects.Service(
        disable_dependent_services=False,
        disable_on_destroy=False,
        project=project_deploy,
        resource_name='pubsub-{p}'.format(p=project_name),
        service='pubsub.googleapis.com'
    )
