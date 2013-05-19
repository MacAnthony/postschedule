# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Post.text'
        db.alter_column('schedule_post', 'text', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'Post.text'
        db.alter_column('schedule_post', 'text', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        'schedule.post': {
            'Meta': {'object_name': 'Post'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['schedule']