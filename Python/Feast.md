Recommended pipenv install:

```
pipenv install feast==0.14
```

Feast consists of many things (note it works with time-series data):

## Data Source

Refers to the raw underlying data (that feast will access when extracting features). An example of data souce can be a table in BigQuery.

## Entity

Refers to the collection of related features. For example, we can make an entity for 'driver' (assuming we make some ride-hailing service) by

```
from Feast import Entity

driver = Entity(name = 'driver', value_type = ValueType.STRING, join_key = 'driver_id')
```

In the above example, 'driver_id' would be refered to as the **Entity key**. Entity key refers to a primary key (a key unique for each element of a table that helps us identity rows as unique)

## Feature Views

Refers to an object representing time-series feature 'sub-data' from a given data source. It donsits of zero or more entities, one or more features (numerical value) and a data source. 

Feature views consistently model existing (pre-computed) feature data in a consistent way in both an offline (training) and online (deployed) settings. An example can be:

```
from feast import FeatureView, Feature, BigQuerySource
from feast.value_type import ValueType

drive_stats_fv = FeatureView(
        name = 'driver_activity',
        entities = ["driver"],
        features = [
            Feature(name = "trips_today", dtype = ValueType.INT64),
            Feature(name="rating", dtype=ValueType.FLOAT),
        ],
        batch_source = BigQuerySource(
            table_ref = "feast-oss.demo_data_driver_activity"
        )
)
```

Feature views can also be generated from an online store (instead of taking batch_source, it takes stream sources).

Note feature views does not need an entity as given by the example

```
from Feast import FeatureView, Feature, BigQuerySource

global_stats_fb = FeatureView(
    name = "global_stats",
    entities = [],
    features = [
        Feature(name="total_trips_today_by_all_drivers", dtype = ValueType.INT64),
    ],
    batch_source = BigQuerySource(
        table_ref = "feast-oss.demo_data.global_stats"
    )
)
```

If feature parameter is unspecified, Feast will infer the features by creating a feature for each column in the underlying data (except for the entity keys and timestamp).

We can combine distinct entities as one single entity (called entity aliases). For instance "origin" and "destination" can be aliases of a "location" entity as:

```
location = Entity(name="location", join_key="location_id", value_type=ValueType.INT64)

location_stats_fv= FeatureView(
    name="location_stats",
    entities=["location"],
    features=[
        Feature(name="temperature", dtype=ValueType.INT32)
    ],
    batch_source=BigQuerySource(
        table_ref="feast-oss.demo_data.location_stats"
    ),
)

temperatures_fs = FeatureService(
    name="temperatures",
    features=[
        location_stats_fv
            .with_name("origin_stats")
            .with_join_key_map(
                {"location_id": "origin_id"}
            ),
        location_stats_fv
            .with_name("destination_stats")
            .with_join_key_map(
                {"location_id": "destination_id"}
            ),
    ],
)
```

## Feature Services

Refers to a group of features from one or more feature views (referred to as by one single name):

```
driver_stats_fs = FeatureService(
    name="driver_activity",
    features=[driver_stats_fv, driver_ratings_fv[["lifetime_rating"]]]
)
```

```
from feast import FeatureStore
feature_store = FeatureStore('.')  # Initialize the feature store

feature_service = feature_store.get_feature_service("driver_activity")
features = feature_store.get_online_features(
    features=feature_service, entity_rows=[entity_dict]
)
```
