# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table('schedule_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('scheduled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('schedule', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table('schedule_post')


    models = {
        'schedule.post': {
            'Meta': {'object_name': 'Post'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scheduled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['schedule']