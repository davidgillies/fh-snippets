# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field families on 'Biog'
        m2m_table_name = db.shorten_name(u'biogs_biog_families')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('biog', models.ForeignKey(orm[u'biogs.biog'], null=False)),
            ('family', models.ForeignKey(orm[u'tree.family'], null=False))
        ))
        db.create_unique(m2m_table_name, ['biog_id', 'family_id'])


    def backwards(self, orm):
        # Removing M2M table for field families on 'Biog'
        db.delete_table(db.shorten_name(u'biogs_biog_families'))


    models = {
        u'biogs.biog': {
            'Meta': {'ordering': "('surname', 'first_name', 'birth_year')", 'object_name': 'Biog'},
            'birth_year': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'families': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tree.Family']", 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'snippets': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['snippets.Snippet']", 'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tags.Tag']", 'null': 'True', 'blank': 'True'}),
            'tree_members': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['tree.Tree']", 'null': 'True', 'blank': 'True'})
        },
        u'snippets.snippet': {
            'Meta': {'ordering': "('author',)", 'object_name': 'Snippet'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'snippet': ('django.db.models.fields.TextField', [], {}),
            'source_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'source_type': ('django.db.models.fields.CharField', [], {'default': "'BK'", 'max_length': '10'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tags.Tag']", 'symmetrical': 'False'})
        },
        u'tags.tag': {
            'Meta': {'ordering': "('tag_type',)", 'object_name': 'Tag'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tagname': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'tree.family': {
            'Meta': {'object_name': 'Family'},
            'children': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'kids'", 'symmetrical': 'False', 'to': u"orm['tree.Tree']"}),
            'husband': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hubbie'", 'to': u"orm['tree.Tree']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marriage_date': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'marriage_place': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'wife': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wiffy'", 'to': u"orm['tree.Tree']"})
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