# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Biog'
        db.create_table(u'biogs_biog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('birth_year', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'biogs', ['Biog'])

        # Adding M2M table for field tags on 'Biog'
        m2m_table_name = db.shorten_name(u'biogs_biog_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('biog', models.ForeignKey(orm[u'biogs.biog'], null=False)),
            ('tag', models.ForeignKey(orm[u'tags.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['biog_id', 'tag_id'])

        # Adding M2M table for field tree_members on 'Biog'
        m2m_table_name = db.shorten_name(u'biogs_biog_tree_members')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('biog', models.ForeignKey(orm[u'biogs.biog'], null=False)),
            ('tree', models.ForeignKey(orm[u'tree.tree'], null=False))
        ))
        db.create_unique(m2m_table_name, ['biog_id', 'tree_id'])


    def backwards(self, orm):
        # Deleting model 'Biog'
        db.delete_table(u'biogs_biog')

        # Removing M2M table for field tags on 'Biog'
        db.delete_table(db.shorten_name(u'biogs_biog_tags'))

        # Removing M2M table for field tree_members on 'Biog'
        db.delete_table(db.shorten_name(u'biogs_biog_tree_members'))


    models = {
        u'biogs.biog': {
            'Meta': {'ordering': "('surname', 'first_name', 'birth_year')", 'object_name': 'Biog'},
            'birth_year': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tags.Tag']", 'null': 'True', 'blank': 'True'}),
            'tree_members': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tree.Tree']", 'null': 'True', 'blank': 'True'})
        },
        u'tags.tag': {
            'Meta': {'ordering': "('tag_type',)", 'object_name': 'Tag'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tagname': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'tree.tree': {
            'Meta': {'ordering': "('surname', 'birth_date')", 'object_name': 'Tree'},
            'birth_date': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'death_date': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tags.Tag']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['biogs']