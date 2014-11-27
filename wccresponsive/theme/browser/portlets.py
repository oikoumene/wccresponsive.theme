from collective.portlet.collectionmultiview import BaseRenderer
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile


class WCCEventRenderer(BaseRenderer):
    title = 'WCC Event'
    template = ViewPageTemplateFile('templates/wcc_event.pt')
