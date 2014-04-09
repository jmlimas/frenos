# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Unidade'
        db.delete_table(u'principal_unidade')

        # Adding model 'Unidad'
        db.create_table(u'principal_unidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marca', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('modelo', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('ano', self.gf('django.db.models.fields.IntegerField')()),
            ('placas', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Cliente'])),
        ))
        db.send_create_signal(u'principal', ['Unidad'])


    def backwards(self, orm):
        # Adding model 'Unidade'
        db.create_table(u'principal_unidade', (
            ('placas', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('ano', self.gf('django.db.models.fields.IntegerField')()),
            ('marca', self.gf('django.db.models.fields.CharField')(max_length=140)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modelo', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Cliente'])),
        ))
        db.send_create_signal(u'principal', ['Unidade'])

        # Deleting model 'Unidad'
        db.delete_table(u'principal_unidad')


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
        }
    }

    complete_apps = ['principal']