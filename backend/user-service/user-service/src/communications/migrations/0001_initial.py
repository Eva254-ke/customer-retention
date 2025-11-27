from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='SMSMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(choices=[('outgoing', 'Outgoing'), ('incoming', 'Incoming')], default='outgoing', max_length=10)),
                ('phone_number', models.CharField(max_length=32)),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('queued', 'Queued'), ('processing', 'Processing'), ('sent', 'Sent'), ('failed', 'Failed')], default='pending', max_length=16)),
                ('task_id', models.CharField(blank=True, max_length=64, null=True)),
                ('provider_response', models.JSONField(blank=True, default=dict)),
                ('error', models.TextField(blank=True)),
                ('metadata', models.JSONField(blank=True, default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
