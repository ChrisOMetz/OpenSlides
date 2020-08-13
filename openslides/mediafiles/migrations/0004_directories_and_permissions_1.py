# Generated by Django 2.2.2 on 2019-06-28 06:06

from django.db import migrations, models

import openslides.mediafiles.models
import openslides.utils.models


class Migration(migrations.Migration):

    dependencies = [("mediafiles", "0003_auto_20190119_1425")]

    operations = [
        migrations.AlterModelOptions(
            name="mediafile",
            options={
                "default_permissions": (),
                "ordering": ("title",),
                "permissions": (
                    ("can_see", "Can see the list of files"),
                    ("can_manage", "Can manage files"),
                ),
            },
        ),
        migrations.RenameField(
            model_name="mediafile", old_name="timestamp", new_name="create_timestamp"
        ),
        migrations.AddField(
            model_name="mediafile",
            name="access_groups",
            field=models.ManyToManyField(blank=True, to="users.Group"),
        ),
        migrations.AddField(
            model_name="mediafile",
            name="is_directory",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="mediafile",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.SET_NULL,
                related_name="children",
                to="mediafiles.Mediafile",
            ),
        ),
        migrations.AddField(
            model_name="mediafile",
            name="original_filename",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="mediafile",
            name="mediafile",
            field=models.FileField(
                null=True, upload_to=openslides.mediafiles.models.get_file_path
            ),
        ),
        migrations.AlterField(
            model_name="mediafile", name="title", field=models.CharField(max_length=255)
        ),
    ]