#!/home/plone/workspace/Plone5/sites/bin/python
"""PILdriver, an image-processing calculator using PIL.

An instance of class PILDriver is essentially a software stack machine
(Polish-notation interpreter) for sequencing PIL image
transformations.  The state of the instance is the interpreter stack.

The only method one will normally invoke after initialization is the
`execute' method.  This takes an argument list of tokens, pushes them
onto the instance's stack, and then tries to clear the stack by
successive evaluation of PILdriver operators.  Any part of the stack
not cleaned off persists and is part of the evaluation context for
the next call of the execute method.

PILDriver doesn't catch any exceptions, on the theory that these
are actually diagnostic information that should be interpreted by
the calling code.

When called as a script, the command-line arguments are passed to
a PILDriver instance.  If there are no command-line arguments, the
module runs an interactive interpreter, each line of which is split into
space-separated tokens and passed to the execute method.

In the method descriptions below, a first line beginning with the string
`usage:' means this method can be invoked with the token that follows
it.  Following <>-enclosed arguments describe how the method interprets
the entries on the stack.  Each argument specification begins with a
type specification: either `int', `float', `string', or `image'.

All operations consume their arguments off the stack (use `dup' to
keep copies around).  Use `verbose 1' to see the stack state displayed
before each operation.

Usage examples:

    `show crop 0 0 200 300 open test.png' loads test.png, crops out a portion
of its upper-left-hand corner and displays the cropped portion.

    `save rotated.png rotate 30 open test.tiff' loads test.tiff, rotates it
30 degrees, and saves the result as rotated.png (in PNG format).
"""
# by Eric S. Raymond <esr@thyrsus.com>
# $Id$

# TO DO:
# 1. Add PILFont capabilities, once that's documented.
# 2. Add PILDraw operations.
# 3. Add support for composing and decomposing multiple-image files.
#

from __future__ import print_function



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
  '/home/plone/.buildout/eggs/plonetheme.barceloneta-1.6.14-py2.7.egg',
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

class PILDriver:

    verbose = 0

    def do_verbose(self):
        """usage: verbose <int:num>

        Set verbosity flag from top of stack.
        """
        self.verbose = int(self.do_pop())

    # The evaluation stack (internal only)

    stack = []          # Stack of pending operations

    def push(self, item):
        "Push an argument onto the evaluation stack."
        self.stack = [item] + self.stack

    def top(self):
        "Return the top-of-stack element."
        return self.stack[0]

    # Stack manipulation (callable)

    def do_clear(self):
        """usage: clear

        Clear the stack.
        """
        self.stack = []

    def do_pop(self):
        """usage: pop

        Discard the top element on the stack.
        """
        top = self.stack[0]
        self.stack = self.stack[1:]
        return top

    def do_dup(self):
        """usage: dup

        Duplicate the top-of-stack item.
        """
        if hasattr(self, 'format'):     # If it's an image, do a real copy
            dup = self.stack[0].copy()
        else:
            dup = self.stack[0]
        self.stack = [dup] + self.stack

    def do_swap(self):
        """usage: swap

        Swap the top-of-stack item with the next one down.
        """
        self.stack = [self.stack[1], self.stack[0]] + self.stack[2:]

    # Image module functions (callable)

    def do_new(self):
        """usage: new <int:xsize> <int:ysize> <int:color>:

        Create and push a greyscale image of given size and color.
        """
        xsize = int(self.do_pop())
        ysize = int(self.do_pop())
        color = int(self.do_pop())
        self.push(Image.new("L", (xsize, ysize), color))

    def do_open(self):
        """usage: open <string:filename>

        Open the indicated image, read it, push the image on the stack.
        """
        self.push(Image.open(self.do_pop()))

    def do_blend(self):
        """usage: blend <image:pic1> <image:pic2> <float:alpha>

        Replace two images and an alpha with the blended image.
        """
        image1 = self.do_pop()
        image2 = self.do_pop()
        alpha = float(self.do_pop())
        self.push(Image.blend(image1, image2, alpha))

    def do_composite(self):
        """usage: composite <image:pic1> <image:pic2> <image:mask>

        Replace two images and a mask with their composite.
        """
        image1 = self.do_pop()
        image2 = self.do_pop()
        mask = self.do_pop()
        self.push(Image.composite(image1, image2, mask))

    def do_merge(self):
        """usage: merge <string:mode> <image:pic1> [<image:pic2> [<image:pic3> [<image:pic4>]]]

        Merge top-of stack images in a way described by the mode.
        """
        mode = self.do_pop()
        bandlist = []
        for band in mode:
            bandlist.append(self.do_pop())
        self.push(Image.merge(mode, bandlist))

    # Image class methods

    def do_convert(self):
        """usage: convert <string:mode> <image:pic1>

        Convert the top image to the given mode.
        """
        mode = self.do_pop()
        image = self.do_pop()
        self.push(image.convert(mode))

    def do_copy(self):
        """usage: copy <image:pic1>

        Make and push a true copy of the top image.
        """
        self.dup()

    def do_crop(self):
        """usage: crop <int:left> <int:upper> <int:right> <int:lower> <image:pic1>

        Crop and push a rectangular region from the current image.
        """
        left = int(self.do_pop())
        upper = int(self.do_pop())
        right = int(self.do_pop())
        lower = int(self.do_pop())
        image = self.do_pop()
        self.push(image.crop((left, upper, right, lower)))

    def do_draft(self):
        """usage: draft <string:mode> <int:xsize> <int:ysize>

        Configure the loader for a given mode and size.
        """
        mode = self.do_pop()
        xsize = int(self.do_pop())
        ysize = int(self.do_pop())
        self.push(self.draft(mode, (xsize, ysize)))

    def do_filter(self):
        """usage: filter <string:filtername> <image:pic1>

        Process the top image with the given filter.
        """
        from PIL import ImageFilter
        filter = eval("ImageFilter." + self.do_pop().upper())
        image = self.do_pop()
        self.push(image.filter(filter))

    def do_getbbox(self):
        """usage: getbbox

        Push left, upper, right, and lower pixel coordinates of the top image.
        """
        bounding_box = self.do_pop().getbbox()
        self.push(bounding_box[3])
        self.push(bounding_box[2])
        self.push(bounding_box[1])
        self.push(bounding_box[0])

    def do_getextrema(self):
        """usage: extrema

        Push minimum and maximum pixel values of the top image.
        """
        extrema = self.do_pop().extrema()
        self.push(extrema[1])
        self.push(extrema[0])

    def do_offset(self):
        """usage: offset <int:xoffset> <int:yoffset> <image:pic1>

        Offset the pixels in the top image.
        """
        xoff = int(self.do_pop())
        yoff = int(self.do_pop())
        image = self.do_pop()
        self.push(image.offset(xoff, yoff))

    def do_paste(self):
        """usage: paste <image:figure> <int:xoffset> <int:yoffset> <image:ground>

        Paste figure image into ground with upper left at given offsets.
        """
        figure = self.do_pop()
        xoff = int(self.do_pop())
        yoff = int(self.do_pop())
        ground = self.do_pop()
        if figure.mode == "RGBA":
            ground.paste(figure, (xoff, yoff), figure)
        else:
            ground.paste(figure, (xoff, yoff))
        self.push(ground)

    def do_resize(self):
        """usage: resize <int:xsize> <int:ysize> <image:pic1>

        Resize the top image.
        """
        ysize = int(self.do_pop())
        xsize = int(self.do_pop())
        image = self.do_pop()
        self.push(image.resize((xsize, ysize)))

    def do_rotate(self):
        """usage: rotate <int:angle> <image:pic1>

        Rotate image through a given angle
        """
        angle = int(self.do_pop())
        image = self.do_pop()
        self.push(image.rotate(angle))

    def do_save(self):
        """usage: save <string:filename> <image:pic1>

        Save image with default options.
        """
        filename = self.do_pop()
        image = self.do_pop()
        image.save(filename)

    def do_save2(self):
        """usage: save2 <string:filename> <string:options> <image:pic1>

        Save image with specified options.
        """
        filename = self.do_pop()
        options = self.do_pop()
        image = self.do_pop()
        image.save(filename, None, options)

    def do_show(self):
        """usage: show <image:pic1>

        Display and pop the top image.
        """
        self.do_pop().show()

    def do_thumbnail(self):
        """usage: thumbnail <int:xsize> <int:ysize> <image:pic1>

        Modify the top image in the stack to contain a thumbnail of itself.
        """
        ysize = int(self.do_pop())
        xsize = int(self.do_pop())
        self.top().thumbnail((xsize, ysize))

    def do_transpose(self):
        """usage: transpose <string:operator> <image:pic1>

        Transpose the top image.
        """
        transpose = self.do_pop().upper()
        image = self.do_pop()
        self.push(image.transpose(transpose))

    # Image attributes

    def do_format(self):
        """usage: format <image:pic1>

        Push the format of the top image onto the stack.
        """
        self.push(self.do_pop().format)

    def do_mode(self):
        """usage: mode <image:pic1>

        Push the mode of the top image onto the stack.
        """
        self.push(self.do_pop().mode)

    def do_size(self):
        """usage: size <image:pic1>

        Push the image size on the stack as (y, x).
        """
        size = self.do_pop().size
        self.push(size[0])
        self.push(size[1])

    # ImageChops operations

    def do_invert(self):
        """usage: invert <image:pic1>

        Invert the top image.
        """
        from PIL import ImageChops
        self.push(ImageChops.invert(self.do_pop()))

    def do_lighter(self):
        """usage: lighter <image:pic1> <image:pic2>

        Pop the two top images, push an image of the lighter pixels of both.
        """
        from PIL import ImageChops
        image1 = self.do_pop()
        image2 = self.do_pop()
        self.push(ImageChops.lighter(image1, image2))

    def do_darker(self):
        """usage: darker <image:pic1> <image:pic2>

        Pop the two top images, push an image of the darker pixels of both.
        """
        from PIL import ImageChops
        image1 = self.do_pop()
        image2 = self.do_pop()
        self.push(ImageChops.darker(image1, image2))

    def do_difference(self):
        """usage: difference <image:pic1> <image:pic2>

        Pop the two top images, push the difference image
        """
        from PIL import ImageChops
        image1 = self.do_pop()
        image2 = self.do_pop()
        self.push(ImageChops.difference(image1, image2))

    def do_multiply(self):
        """usage: multiply <image:pic1> <image:pic2>

        Pop the two top images, push the multiplication image.
        """
        from PIL import ImageChops
        image1 = self.do_pop()
        image2 = self.do_pop()
        self.push(ImageChops.multiply(image1, image2))

    def do_screen(self):
        """usage: screen <image:pic1> <image:pic2>

        Pop the two top images, superimpose their inverted versions.
        """
        from PIL import ImageChops
        image2 = self.do_pop()
        image1 = self.do_pop()
        self.push(ImageChops.screen(image1, image2))

    def do_add(self):
        """usage: add <image:pic1> <image:pic2> <int:offset> <float:scale>

        Pop the two top images, produce the scaled sum with offset.
        """
        from PIL import ImageChops
        image1 = self.do_pop()
        image2 = self.do_pop()
        scale = float(self.do_pop())
        offset = int(self.do_pop())
        self.push(ImageChops.add(image1, image2, scale, offset))

    def do_subtract(self):
        """usage: subtract <image:pic1> <image:pic2> <int:offset> <float:scale>

        Pop the two top images, produce the scaled difference with offset.
        """
        from PIL import ImageChops
        image1 = self.do_pop()
        image2 = self.do_pop()
        scale = float(self.do_pop())
        offset = int(self.do_pop())
        self.push(ImageChops.subtract(image1, image2, scale, offset))

    # ImageEnhance classes

    def do_color(self):
        """usage: color <image:pic1>

        Enhance color in the top image.
        """
        from PIL import ImageEnhance
        factor = float(self.do_pop())
        image = self.do_pop()
        enhancer = ImageEnhance.Color(image)
        self.push(enhancer.enhance(factor))

    def do_contrast(self):
        """usage: contrast <image:pic1>

        Enhance contrast in the top image.
        """
        from PIL import ImageEnhance
        factor = float(self.do_pop())
        image = self.do_pop()
        enhancer = ImageEnhance.Contrast(image)
        self.push(enhancer.enhance(factor))

    def do_brightness(self):
        """usage: brightness <image:pic1>

        Enhance brightness in the top image.
        """
        from PIL import ImageEnhance
        factor = float(self.do_pop())
        image = self.do_pop()
        enhancer = ImageEnhance.Brightness(image)
        self.push(enhancer.enhance(factor))

    def do_sharpness(self):
        """usage: sharpness <image:pic1>

        Enhance sharpness in the top image.
        """
        from PIL import ImageEnhance
        factor = float(self.do_pop())
        image = self.do_pop()
        enhancer = ImageEnhance.Sharpness(image)
        self.push(enhancer.enhance(factor))

    # The interpreter loop

    def execute(self, list):
        "Interpret a list of PILDriver commands."
        list.reverse()
        while len(list) > 0:
            self.push(list[0])
            list = list[1:]
            if self.verbose:
                print("Stack: " + repr(self.stack))
            top = self.top()
            if not isinstance(top, str):
                continue
            funcname = "do_" + top
            if not hasattr(self, funcname):
                continue
            else:
                self.do_pop()
                func = getattr(self, funcname)
                func()

if __name__ == '__main__':
    import sys
    try:
        import readline
    except ImportError:
        pass # not available on all platforms

    # If we see command-line arguments, interpret them as a stack state
    # and execute.  Otherwise go interactive.

    driver = PILDriver()
    if len(sys.argv[1:]) > 0:
        driver.execute(sys.argv[1:])
    else:
        print("PILDriver says hello.")
        while True:
            try:
                if sys.version_info[0] >= 3:
                    line = input('pildriver> ')
                else:
                    line = raw_input('pildriver> ')
            except EOFError:
                print("\nPILDriver says goodbye.")
                break
            driver.execute(line.split())
            print(driver.stack)

# The following sets edit modes for GNU EMACS
# Local Variables:
# mode:python
# End:
