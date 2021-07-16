import os

import pulumi
from pulumi_gcp import pubsub

from typing import Dict, Optional


def _parse_env_vars() -> dict:
    print('INFO: infra.pulumi.pubsub._parse_dataset')

    pg_customers: Optional[str] = os.getenv('_PG_CUSTOMERS')
    pg_geography_columns: Optional[str] = os.getenv('_PG_GEOGRAPHY_COLUMNS')
    pg_geom: Optional[str] = os.getenv('_PG_GEOM')
    pg_geometry_columns: Optional[str] = os.getenv('_PG_GEOMETRY_COLUMNS')
    pg_orders: Optional[str] = os.getenv('_PG_ORDERS')
    pg_products: Optional[str] = os.getenv('_PG_PRODUCTS')
    pg_products_on_hand: Optional[str] = os.getenv('_PG_PRODUCTS_ON_HAND')
    pg_raster_columns: Optional[str] = os.getenv('_PG_RASTER_COLUMNS')
    pg_raster_overviews: Optional[str] = os.getenv('_PG_RASTER_OVERVIEWS')
    pg_spatial_ref_sys: Optional[str] = os.getenv('_PG_SPATIAL_REF_SYS')

    print('''INFO: infra.pulumi.pubsub._parse_dataset returning: 
        pg_customers -> {pg_customers}; pg_geography_columns -> {pg_geography_columns} ;
        pg_geom -> {pg_geom};
        pg_geometry_columns -> {pg_geometry_columns}; pg_orders -> {pg_orders};
        pg_products -> {pg_products}; pg_products_on_hand -> {pg_products_on_hand};
        pg_raster_columns -> {pg_raster_columns}; pg_raster_overviews -> {pg_raster_overviews};
        pg_spatial_ref_sys -> {pg_spatial_ref_sys}'''.format(
        pg_customers=pg_customers,
        pg_geography_columns=pg_geography_columns,
        pg_geom=pg_geom,
        pg_geometry_columns=pg_geometry_columns,
        pg_orders=pg_orders,
        pg_products=pg_products,
        pg_products_on_hand=pg_products_on_hand,
        pg_raster_columns=pg_raster_columns,
        pg_raster_overviews=pg_raster_overviews,
        pg_spatial_ref_sys=pg_spatial_ref_sys
    ))

    return {
        'pg_customers': pg_customers,
        'pg_geography_columns': pg_geography_columns,
        'pg_geom': pg_geom,
        'pg_geometry_columns': pg_geometry_columns,
        'pg_orders': pg_orders,
        'pg_products': pg_products,
        'pg_products_on_hand': pg_products_on_hand,
        'pg_raster_columns': pg_raster_columns,
        'pg_raster_overviews': pg_raster_overviews,
        'pg_spatial_ref_sys': pg_spatial_ref_sys,
    }


def main(
    env: str,
    project: str,
    project_auchan: str,
    project_deploy: str
) -> None:
    print('INFO: infra.pulumi.pubsub.main')

    env_vars: dict = _parse_env_vars()

    # Topics
    t_pg_customers = pubsub.Topic(
        labels={
            'environment': env,
            'event_source': env_vars['pg_customers'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
        },
        name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_customers']),
        project=project_deploy,
        resource_name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_customers'])
    )

    t_pg_geography_columns = pubsub.Topic(
        labels={
            'environment': env,
            'event_source': env_vars['pg_geography_columns'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
        },
        name='{n}-{t}'.format(
            n=project_auchan, t=env_vars['pg_geography_columns']),
        project=project_deploy,
        resource_name='{n}-{t}'.format(
            n=project_auchan, t=env_vars['pg_geography_columns'])
    )

    t_pg_geom = pubsub.Topic(
        labels={
            'environment': env,
            'event_source': env_vars['pg_geom'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
        },
        name='{n}-{t}'.format(
            n=project_auchan, t=env_vars['pg_geom']),
        project=project_deploy,
        resource_name='{n}-{t}'.format(
            n=project_auchan, t=env_vars['pg_geom'])
    )

    t_pg_geometry_columns = pubsub.Topic(
        labels={
            'environment': env,
            'event_source': env_vars['pg_geometry_columns'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
        },
        name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_geometry_columns']),
        project=project_deploy,
        resource_name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_geometry_columns'])
    )

    t_pg_orders = pubsub.Topic(
        labels={
            'environment': env,
            'event_source': env_vars['pg_orders'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
        },
        name='{n}-{t}'.format(
            n=project_auchan, t=env_vars['pg_orders']),
        project=project_deploy,
        resource_name='{n}-{t}'.format(
            n=project_auchan, t=env_vars['pg_orders'])
    )

    t_pg_products = pubsub.Topic(
        labels={
            'environment': env,
            'event_source': env_vars['pg_products'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
        },
        name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_products']),
        project=project_deploy,
        resource_name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_products'])
    )

    t_pg_products_on_hand = pubsub.Topic(
        labels={
            'environment': env,
            'event_source': env_vars['pg_products_on_hand'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
        },
        name='{n}-{t}'.format(
            n=project_auchan, t=env_vars['pg_products_on_hand']),
        project=project_deploy,
        resource_name='{n}-{t}'.format(
            n=project_auchan, t=env_vars['pg_products_on_hand'])
    )

    t_pg_raster_columns = pubsub.Topic(
        labels={
            'environment': env,
            'event_source': env_vars['pg_raster_columns'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
        },
        name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_raster_columns']),
        project=project_deploy,
        resource_name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_raster_columns'])
    )

    t_pg_raster_overviews = pubsub.Topic(
        labels={
            'environment': env,
            'event_source': env_vars['pg_raster_overviews'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
        },
        name='{n}-{t}'.format(
            n=project_auchan, t=env_vars['pg_raster_overviews']),
        project=project_deploy,
        resource_name='{n}-{t}'.format(
            n=project_auchan, t=env_vars['pg_raster_overviews'])
    )

    t_pg_spatial_ref_sys = pubsub.Topic(
        labels={
            'environment': env,
            'event_source': env_vars['pg_spatial_ref_sys'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
        },
        name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_spatial_ref_sys']),
        project=project_deploy,
        resource_name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_spatial_ref_sys'])
    )

    # Subscriptions
    s_pg_customers = pubsub.Subscription(
        topic=t_pg_customers.name,
        ack_deadline_seconds=20,
        labels={
            'environment': env,
            'event_source': env_vars['pg_customers'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
       },
        name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_customers']),
        project=project_deploy,
        resource_name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_customers'])
    )

    s_pg_geography_columns = pubsub.Subscription(
        topic=t_pg_geography_columns.name,
        ack_deadline_seconds=20,
        labels={
            'environment': env,
            'event_source': env_vars['pg_geography_columns'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
       },
        name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_geography_columns']),
        project=project_deploy,
        resource_name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_geography_columns'])
    )

    s_pg_geom = pubsub.Subscription(
        topic=t_pg_geom.name,
        ack_deadline_seconds=20,
        labels={
            'environment': env,
            'event_source': env_vars['pg_geom'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
       },
        name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_geom']),
        project=project_deploy,
        resource_name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_geom'])
    )

    s_pg_geometry_columns = pubsub.Subscription(
        topic=t_pg_geometry_columns.name,
        ack_deadline_seconds=20,
        labels={
            'environment': env,
            'event_source': env_vars['pg_geometry_columns'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
       },
        name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_geometry_columns']),
        project=project_deploy,
        resource_name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_geometry_columns'])
    )

    s_pg_products = pubsub.Subscription(
        topic=t_pg_products.name,
        ack_deadline_seconds=20,
        labels={
            'environment': env,
            'event_source': env_vars['pg_products'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
       },
        name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_products']),
        project=project_deploy,
        resource_name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_products'])
    )

    s_pg_orders = pubsub.Subscription(
        topic=t_pg_orders.name,
        ack_deadline_seconds=20,
        labels={
            'environment': env,
            'event_source': env_vars['pg_orders'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
       },
        name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_orders']),
        project=project_deploy,
        resource_name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_orders'])
    )

    s_pg_products_on_hand = pubsub.Subscription(
        topic=t_pg_products_on_hand.name,
        ack_deadline_seconds=20,
        labels={
            'environment': env,
            'event_source': env_vars['pg_products_on_hand'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
       },
        name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_products_on_hand']),
        project=project_deploy,
        resource_name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_products_on_hand'])
    )

    s_pg_raster_columns = pubsub.Subscription(
        topic=t_pg_raster_columns.name,
        ack_deadline_seconds=20,
        labels={
            'environment': env,
            'event_source': env_vars['pg_raster_columns'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
       },
        name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_raster_columns']),
        project=project_deploy,
        resource_name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_raster_columns'])
    )

    s_pg_raster_overviews = pubsub.Subscription(
        topic=t_pg_raster_overviews.name,
        ack_deadline_seconds=20,
        labels={
            'environment': env,
            'event_source': env_vars['pg_raster_overviews'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
       },
        name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_raster_overviews']),
        project=project_deploy,
        resource_name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_raster_overviews'])
    )

    s_pg_spatial_ref_sys = pubsub.Subscription(
        topic=t_pg_spatial_ref_sys.name,
        ack_deadline_seconds=20,
        labels={
            'environment': env,
            'event_source': env_vars['pg_spatial_ref_sys'],
            'project': project,
            'project_auchan': project_auchan,
            'project_deploy': project_deploy,
       },
        name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_spatial_ref_sys']),
        project=project_deploy,
        resource_name='{n}-{t}-outcome'.format(
            n=project_auchan, t=env_vars['pg_spatial_ref_sys'])
    )
