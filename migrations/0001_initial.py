# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Application'
        db.create_table(u'ga_applications_application', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('default_base_map', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('script_tags', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('link_tags', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('application_script', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('application_css', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('left_sidebar_html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('right_sidebar_html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('left_sidebar_columns', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('right_sidebar_columns', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('header_html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('footer_html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('default_includes', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'ga_applications', ['Application'])

        # Adding model 'ApplicationLayer'
        db.create_table(u'ga_applications_applicationlayer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ga_applications.Application'])),
            ('renderedlayer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ga_resources.RenderedLayer'])),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'ga_applications', ['ApplicationLayer'])


    def backwards(self, orm):
        # Deleting model 'Application'
        db.delete_table(u'ga_applications_application')

        # Deleting model 'ApplicationLayer'
        db.delete_table(u'ga_applications_applicationlayer')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ga_applications.application': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Application', '_ormbases': [u'pages.Page']},
            'application_css': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'application_script': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'default_base_map': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'default_includes': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'footer_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'header_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'left_sidebar_columns': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'left_sidebar_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'link_tags': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'renderedlayers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ga_resources.RenderedLayer']", 'symmetrical': 'False', 'through': u"orm['ga_applications.ApplicationLayer']", 'blank': 'True'}),
            'right_sidebar_columns': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'right_sidebar_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'script_tags': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'ga_applications.applicationlayer': {
            'Meta': {'ordering': "('-weight',)", 'object_name': 'ApplicationLayer'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ga_applications.Application']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'renderedlayer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ga_resources.RenderedLayer']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ga_resources.dataresource': {
            'Meta': {'ordering': "['title']", 'object_name': 'DataResource', '_ormbases': [u'pages.Page']},
            'big': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bounding_box': ('django.contrib.gis.db.models.fields.PolygonField', [], {'null': 'True', 'blank': 'True'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'driver': ('django.db.models.fields.CharField', [], {'default': "'ga_resources.drivers.spatialite'", 'max_length': '255'}),
            'last_change': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_refresh': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'md5sum': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'metadata_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'metadata_xml': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'native_bounding_box': ('django.contrib.gis.db.models.fields.PolygonField', [], {'null': 'True', 'blank': 'True'}),
            'native_srs': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'next_refresh': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'refresh_every': ('timedelta.fields.TimedeltaField', [], {'null': 'True', 'blank': 'True'}),
            'resource_config': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resource_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'resource_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'three_d': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'ga_resources.renderedlayer': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'RenderedLayer', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'data_resource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ga_resources.DataResource']"}),
            'default_class': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '255'}),
            'default_style': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'default_for_layer'", 'to': u"orm['ga_resources.Style']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'styles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ga_resources.Style']", 'symmetrical': 'False'})
        },
        u'ga_resources.style': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Style', '_ormbases': [u'pages.Page']},
            'legend': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'legend_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'legend_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'stylesheet': ('django.db.models.fields.TextField', [], {})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['ga_applications']