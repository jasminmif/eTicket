# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ticket'
        db.create_table(u'ticket_ticket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid_code', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True, blank=True)),
            ('used', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('printed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ticket', ['Ticket'])


    def backwards(self, orm):
        # Deleting model 'Ticket'
        db.delete_table(u'ticket_ticket')


    models = {
        u'ticket.ticket': {
            'Meta': {'object_name': 'Ticket'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'printed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'uuid_code': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['ticket']