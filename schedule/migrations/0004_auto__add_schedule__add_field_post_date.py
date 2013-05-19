# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.date'
        db.add_column('schedule_post', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.date'
        db.delete_column('schedule_post', 'date')


    models = {
        'schedule.post': {
            'Meta': {'object_name': 'Post'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['schedule']