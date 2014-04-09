# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Servicio'
        db.create_table(u'servicios_servicio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Cliente'])),
            ('unidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Unidad'])),
            ('articulo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Articulo'])),
            ('km', self.gf('django.db.models.fields.IntegerField')()),
            ('nextvisita', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'servicios', ['Servicio'])


    def backwards(self, orm):
        # Deleting model 'Servicio'
        db.delete_table(u'servicios_servicio')


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
        },
        u'principal.unidad': {
            'Meta': {'object_name': 'Unidad'},
            'ano': ('django.db.models.fields.IntegerField', [], {}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Cliente']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'modelo': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'placas': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'})
        },
        u'servicios.servicio': {
            'Meta': {'object_name': 'Servicio'},
            'articulo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Articulo']"}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Cliente']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'km': ('django.db.models.fields.IntegerField', [], {}),
            'nextvisita': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Unidad']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['servicios']