#!/home/plone/workspace/Plone5/sites/bin/python
#
# The Python Imaging Library.
# $Id$
#
# print image files to postscript printer
#
# History:
# 0.1   1996-04-20 fl   Created
# 0.2   1996-10-04 fl   Use draft mode when converting.
# 0.3   2003-05-06 fl   Fixed a typo or two.
#

from __future__ import print_function

VERSION = "pilprint 0.3/2003-05-05"



import sys
sys.path[0:0] = [
  '/home/plone/.buildout/eggs/bpython-0.13.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.reload-2.0-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.PDBDebugMode-1.3.1-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.PrintingMailHost-0.7-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.DocFinderTab-1.0.5-py2.7.egg',
  '/home/plone/.buildout/eggs/Paste-1.7.5.1-py2.7.egg',
  '/home/plone/.buildout/eggs/setuptools-18.3.1-py2.7.egg',
  '/home/plone/.buildout/eggs/PasteDeploy-1.3.4-py2.7.egg',
  '/home/plone/.buildout/eggs/PasteScript-1.7.5-py2.7.egg',
  '/home/plone/.buildout/eggs/i18ndude-3.3.5-py2.7.egg',
  '/home/plone/.buildout/eggs/ZopeSkel-2.19-py2.7.egg',
  '/home/plone/.buildout/eggs/collective.dexteritypaste-1.0alpha1.1-py2.7.egg',
  '/home/plone/.buildout/eggs/toutpt.zopeskel-1.3.3-py2.7.egg',
  '/home/plone/.buildout/eggs/Plone-5.0-py2.7.egg',
  '/home/plone/.buildout/eggs/Pillow-2.7.0-py2.7-linux-x86_64.egg',
  '/home/plone/workspace/Plone5/sites/src/pas.plugins.sqlalchemy/src',
  '/home/plone/workspace/Plone5/sites/src/collective.saconnect/src',
  '/home/plone/.buildout/eggs/Cheetah-2.2.1-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/ordereddict-1.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.i18n-3.0.2-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.i18nmessageid-3.5.3-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/zope.interface-3.6.7-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/zope.tal-3.5.2-py2.7.egg',
  '/home/plone/.buildout/eggs/collective.monkeypatcher-1.1.1-py2.7.egg',
  '/home/plone/.buildout/eggs/Zope2-2.13.23-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.testing-3.9.7-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.site-3.9.2-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.publisher-3.12.6-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.processlifetime-1.0-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.component-3.9.5-py2.7.egg',
  '/home/plone/.buildout/eggs/Pygments-2.0.2-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.z3cform-1.1.5-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.sqlalchemy-0.7.6-py2.7.egg',
  '/home/plone/.buildout/eggs/z3c.saconfig-0.14-py2.7.egg',
  '/home/plone/.buildout/eggs/SQLAlchemy-1.0.9-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/DateTime-3.0.3-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.upgrade-1.3.18-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.openid-2.1.0-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.iterate-3.1.3-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.dexterity-2.1.13-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.caching-1.2.7-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.CMFPlone-5.0-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.CMFPlacefulWorkflow-1.6.4-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.ATContentTypes-2.2.7-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.Archetypes-1.10.10-py2.7.egg',
  '/home/plone/.buildout/eggs/Unidecode-0.04.1-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.i18n-3.7.4-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.StandardCacheManagers-2.13.1-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.PythonScripts-2.13.2-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.MIMETools-2.13.0-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.MailHost-2.13.2-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.ExternalMethod-2.13.1-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.BTreeFolder2-2.13.3-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.viewlet-3.7.2-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.traversing-3.13.2-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.testbrowser-3.11.1-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.tales-3.5.3-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.structuredtext-3.5.1-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.size-3.4.1-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.sequencesort-3.4.0-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.sendmail-3.7.5-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.security-3.7.4-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/zope.schema-4.2.2-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.ptresource-3.9.0-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.proxy-3.6.1-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/zope.pagetemplate-3.6.3-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.location-3.9.1-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.lifecycleevent-3.6.2-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.exceptions-3.6.2-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.event-3.5.2-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.deferredimport-3.5.3-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.contenttype-3.5.5-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.contentprovider-3.7.2-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.container-3.11.2-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/zope.configuration-3.7.4-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.browserresource-3.10.3-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.browserpage-3.12.2-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.browsermenu-3.9.1-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.browser-1.3-py2.7.egg',
  '/home/plone/.buildout/eggs/zLOG-2.11.2-py2.7.egg',
  '/home/plone/.buildout/eggs/zExceptions-2.13.0-py2.7.egg',
  '/home/plone/.buildout/eggs/zdaemon-2.0.7-py2.7.egg',
  '/home/plone/.buildout/eggs/transaction-1.1.1-py2.7.egg',
  '/home/plone/.buildout/eggs/tempstorage-2.12.2-py2.7.egg',
  '/home/plone/.buildout/eggs/pytz-2013b-py2.7.egg',
  '/home/plone/.buildout/eggs/initgroups-2.13.0-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/docutils-0.12-py2.7.egg',
  '/home/plone/.buildout/eggs/ZopeUndo-2.12.0-py2.7.egg',
  '/home/plone/.buildout/eggs/ZODB3-3.10.5-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/ZConfig-2.9.3-py2.7.egg',
  '/home/plone/.buildout/eggs/RestrictedPython-3.6.0-py2.7.egg',
  '/home/plone/.buildout/eggs/Record-2.13.0-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/Products.ZCTextIndex-2.13.5-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/Products.ZCatalog-3.0.2-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.OFSP-2.13.2-py2.7.egg',
  '/home/plone/.buildout/eggs/Persistence-2.13.2-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/MultiMapping-2.13.0-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/Missing-2.13.1-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/ExtensionClass-2.13.2-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/DocumentTemplate-2.13.2-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/Acquisition-2.13.9-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/AccessControl-3.0.11-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/zope.annotation-3.5.0-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.textfield-1.2.6-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.globalrequest-1.1-py2.7.egg',
  '/home/plone/.buildout/eggs/z3c.formwidget.query-0.12-py2.7.egg',
  '/home/plone/.buildout/eggs/z3c.form-3.2.7-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.z3cform-0.8.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.protect-3.0.9-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.widgets-2.0.1-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.CMFCore-2.2.10-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.hookable-3.4.1-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/Products.SecureMailHost-1.1.2-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.ResourceRegistries-3.0.3-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.PortalTransforms-2.1.10-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.PluggableAuthService-1.10.0-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.PlonePAS-5.0.4-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.MimetypesRegistry-2.0.8-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.GenericSetup-1.8.0-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.DCWorkflow-2.2.4-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.CMFUid-2.2.1-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.CMFQuickInstallerTool-3.0.12-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.CMFFormController-3.0.5-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.CMFEditions-2.2.15-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.CMFDiffTool-3.0.2-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.contentmigration-2.1.11-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.ramcache-1.0-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.portlets-3.1.2-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.folder-1.1.0-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.session-3.5.6-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.portlets-2.2-py2.7.egg',
  '/home/plone/.buildout/eggs/five.localsitemanager-2.0.5-py2.7.egg',
  '/home/plone/.buildout/eggs/borg.localrole-3.1.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.openid-2.0.4-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.statusmessages-4.0-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.memoize-1.1.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.locking-2.1.0-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.supermodel-1.2.6-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.contentrules-2.0.4-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.autoform-1.6.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.uuid-1.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.layout-2.5.15-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.content-3.0.12-py2.7.egg',
  '/home/plone/.buildout/eggs/lxml-3.4.4-py2.7-linux-x86_64.egg',
  '/home/plone/.buildout/eggs/plone.schemaeditor-2.0.7-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.rfc822-1.1.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.namedfile-3.0.3-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.formwidget.namedfile-1.0.13-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.dexterity-2.3.5-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.behavior-1.1-py2.7.egg',
  '/home/plone/.buildout/eggs/z3c.zcmlhook-1.0b1-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.CMFDynamicViewFTI-4.1.3-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.registry-1.0.2-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.registry-1.3.5-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.cachepurging-1.0.9-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.caching-1.0.1-py2.7.egg',
  '/home/plone/.buildout/eggs/python_dateutil-1.5-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.dottedname-3.4.6-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.deprecation-3.4.1-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.cachedescriptors-3.5.1-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.app.locales-3.6.2-py2.7.egg',
  '/home/plone/.buildout/eggs/z3c.autoinclude-0.3.5-py2.7.egg',
  '/home/plone/.buildout/eggs/slimit-0.8.1-py2.7.egg',
  '/home/plone/workspace/Plone5/sites/src/plonetheme.barceloneta',
  '/home/plone/.buildout/eggs/plone.theme-3.0.0-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.schema-1.0a1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.portlet.static-3.0.2-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.portlet.collection-3.0.4-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.outputfilters-2.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.intelligenttext-2.0.3-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.indexer-1.0.3-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.browserlayer-2.1.5-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.batching-1.0.5-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.workflow-2.2.4-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.vocabularies-2.1.21-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.viewletmanager-2.0.9-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.users-2.3.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.theming-1.2.14-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.redirector-1.3.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.locales-5.0.5-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.linkintegrity-3.0.2-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.multilingual-3.0.12-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.i18n-3.0.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.discussion-2.4.8-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.customerize-1.3.3-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.controlpanel-3.0.3-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.contenttypes-1.2.4-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.contentrules-4.0.8-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.contentmenu-2.1.6-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.contentlisting-1.2.2-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.api-1.4.7-py2.7.egg',
  '/home/plone/.buildout/eggs/mockup-2.0.12-py2.7.egg',
  '/home/plone/.buildout/eggs/five.pt-2.2.3-py2.7.egg',
  '/home/plone/.buildout/eggs/five.customerize-1.1-py2.7.egg',
  '/home/plone/.buildout/eggs/cssmin-0.2.0-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.PluginRegistry-1.3-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.PlacelessTranslationService-2.0.5-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.PasswordResetTool-2.2.1-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.ExternalEditor-1.1.1-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.ExtendedPathIndex-3.1-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.validation-2.0-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.collection-1.1.4-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.blob-1.6.0-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.uuid-1.0.3-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.folder-1.0.7-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.ZSQLMethods-2.13.4-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.datetime-3.4.1-py2.7.egg',
  '/home/plone/.buildout/eggs/mechanize-0.2.5-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.broken-3.6.0-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.filerepresentation-3.6.1-py2.7.egg',
  '/home/plone/.buildout/eggs/zc.lockfile-1.0.2-py2.7.egg',
  '/home/plone/.buildout/eggs/six-1.8.0-py2.7.egg',
  '/home/plone/.buildout/eggs/five.globalrequest-1.0-py2.7.egg',
  '/home/plone/.buildout/eggs/repoze.xmliter-0.6-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.transformchain-1.0.4-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.keyring-3.0.1-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.app.publication-3.12.0-py2.7.egg',
  '/home/plone/.buildout/eggs/Markdown-2.0.3-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.formlib-4.0.6-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.ZopeVersionControl-1.1.3-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.copy-3.5.0-py2.7.egg',
  '/home/plone/.buildout/eggs/feedparser-5.0.1-py2.7.egg',
  '/home/plone/.buildout/eggs/python_openid-2.2.5-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.componentvocabulary-1.0.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.scale-1.3.5-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.synchronize-1.0.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.alterego-1.0-py2.7.egg',
  '/home/plone/.buildout/eggs/z3c.caching-2.0a1-py2.7.egg',
  '/home/plone/.buildout/eggs/zc.buildout-2.4.3-py2.7.egg',
  '/home/plone/.buildout/eggs/ply-3.4-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.querystring-1.3.8-py2.7.egg',
  '/home/plone/.buildout/eggs/roman-1.4.0-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.subrequest-1.6.11-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.resourceeditor-2.0.3-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.resource-1.0.4-py2.7.egg',
  '/home/plone/.buildout/eggs/diazo-1.2.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.relationfield-1.3.2-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.intid-1.1.0-py2.7.egg',
  '/home/plone/.buildout/eggs/z3c.relationfield-0.7-py2.7.egg',
  '/home/plone/.buildout/eggs/archetypes.multilingual-3.0.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.lockingbehavior-1.0.2-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.versioningbehavior-1.2.5-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.event-2.0.3-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.stringinterp-1.1.2-py2.7.egg',
  '/home/plone/.buildout/eggs/decorator-3.4.0-py2.7.egg',
  '/home/plone/.buildout/eggs/Chameleon-2.22-py2.7.egg',
  '/home/plone/.buildout/eggs/z3c.pt-3.0.0a1-py2.7.egg',
  '/home/plone/.buildout/eggs/sourcecodegen-0.6.14-py2.7.egg',
  '/home/plone/.buildout/eggs/python_gettext-1.0-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.app.imaging-2.0.0-py2.7.egg',
  '/home/plone/.buildout/eggs/archetypes.schemaextender-2.1.5-py2.7.egg',
  '/home/plone/.buildout/eggs/future-0.14.0-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.error-3.7.4-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.authentication-3.7.1-py2.7.egg',
  '/home/plone/.buildout/eggs/cssselect-0.9.1-py2.7.egg',
  '/home/plone/.buildout/eggs/five.intid-1.0.3-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.intid-3.7.2-py2.7.egg',
  '/home/plone/.buildout/eggs/zc.relation-1.0-py2.7.egg',
  '/home/plone/.buildout/eggs/z3c.objpath-1.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.formwidget.recurrence-2.0.1-py2.7.egg',
  '/home/plone/.buildout/eggs/plone.event-1.3-py2.7.egg',
  '/home/plone/.buildout/eggs/icalendar-3.9.1-py2.7.egg',
  '/home/plone/.buildout/eggs/collective.elephantvocabulary-0.2.5-py2.7.egg',
  '/home/plone/.buildout/eggs/Products.DateRecurringIndex-2.1-py2.7.egg',
  '/home/plone/.buildout/eggs/zope.keyreference-3.6.4-py2.7.egg',
  ]


from PIL import Image
from PIL import PSDraw

letter = ( 1.0*72, 1.0*72, 7.5*72, 10.0*72 )

def description(file, image):
    import os
    title = os.path.splitext(os.path.split(file)[1])[0]
    format = " (%dx%d "
    if image.format:
        format = " (" + image.format + " %dx%d "
    return title + format % image.size + image.mode + ")"

import getopt, os, sys

if len(sys.argv) == 1:
    print("PIL Print 0.2a1/96-10-04 -- print image files")
    print("Usage: pilprint files...")
    print("Options:")
    print("  -c            colour printer (default is monochrome)")
    print("  -p            print via lpr (default is stdout)")
    print("  -P <printer>  same as -p but use given printer")
    sys.exit(1)

try:
    opt, argv = getopt.getopt(sys.argv[1:], "cdpP:")
except getopt.error as v:
    print(v)
    sys.exit(1)

printer = None # print to stdout
monochrome = 1 # reduce file size for most common case

for o, a in opt:
    if o == "-d":
        # debug: show available drivers
        Image.init()
        print(Image.ID)
        sys.exit(1)
    elif o == "-c":
        # colour printer
        monochrome = 0
    elif o == "-p":
        # default printer channel
        printer = "lpr"
    elif o == "-P":
        # printer channel
        printer = "lpr -P%s" % a

for file in argv:
    try:

        im = Image.open(file)

        title = description(file, im)

        if monochrome and im.mode not in ["1", "L"]:
            im.draft("L", im.size)
            im = im.convert("L")

        if printer:
            fp = os.popen(printer, "w")
        else:
            fp = sys.stdout

        ps = PSDraw.PSDraw(fp)

        ps.begin_document()
        ps.setfont("Helvetica-Narrow-Bold", 18)
        ps.text((letter[0], letter[3]+24), title)
        ps.setfont("Helvetica-Narrow-Bold", 8)
        ps.text((letter[0], letter[1]-30), VERSION)
        ps.image(letter, im)
        ps.end_document()

    except:
        print("cannot print image", end=' ')
        print("(%s:%s)" % (sys.exc_info()[0], sys.exc_info()[1]))
