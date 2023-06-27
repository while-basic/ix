# Generated by Django 4.2.1 on 2023-06-04 05:06

from django.db import migrations, models

import ix
from ix.pg_vector.index import (
    AddEuclideanDistanceIndex,
    AddInnerProductIndex,
    AddCosineDistanceIndex,
)


class Migration(migrations.Migration):
    dependencies = [
        ("pg_vector_test", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="embedding",
            name="indexed_embedding",
            field=ix.pg_vector.fields.VectorField(
                base_field=models.FloatField(), null=True, size=3
            ),
        ),
        AddEuclideanDistanceIndex("embeddings", "indexed_embedding", lists=150),
        AddInnerProductIndex("embeddings", "indexed_embedding", lists=200),
        AddCosineDistanceIndex("embeddings", "indexed_embedding", lists=250),
        AddEuclideanDistanceIndex(
            "embeddings",
            "indexed_embedding",
            lists=150,
            index_name="my_model_embedding_l2_idx",
        ),
        AddInnerProductIndex(
            "embeddings",
            "indexed_embedding",
            lists=200,
            index_name="my_model_embedding_ip_idx",
        ),
        AddCosineDistanceIndex(
            "embeddings",
            "indexed_embedding",
            lists=250,
            index_name="my_model_embedding_cos_idx",
        ),
    ]