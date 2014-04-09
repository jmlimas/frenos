# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Articulo', fields ['clave']
        db.create_unique(u'principal_articulo', ['clave'])


    def backwards(self, orm):
        # Removing unique constraint on 'Articulo', fields ['clave']
        db.delete_unique(u'principal_articulo', ['clave'])


    models = {
        u'principal.articulo': {
            'Meta': {'object_name': 'Articulo'},
            'clave': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'principal.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['principal']