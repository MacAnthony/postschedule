# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Post.scheduled'
        db.delete_column('schedule_post', 'scheduled')

        # Deleting field 'Post.date'
        db.delete_column('schedule_post', 'date')


    def backwards(self, orm):
        # Adding field 'Post.scheduled'
        db.add_column('schedule_post', 'scheduled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Post.date'
        db.add_column('schedule_post', 'date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    models = {
        'schedule.post': {
            'Meta': {'object_name': 'Post'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['schedule']