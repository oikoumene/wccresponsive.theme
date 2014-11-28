from five import grok
from zope.interface import Interface
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from wccresponsive.theme.interfaces import IThemeSettings
from wccresponsive.theme.vocabulary import SCHEMES_CSS
from zope.component.hooks import getSite
from wccresponsive.theme import getSettings

class SchemeCSS(grok.View):
    grok.context(Interface)
    grok.name('wccresponsive-theme-scheme.css')

    def render(self):
        settings = getSettings()
        self.request.response.setHeader('Content-Type','text/css; charset=utf-8')
        scheme_css = SCHEMES_CSS[settings.scheme]
        site = getSite()
        result = getattr(site, scheme_css)
        return unicode(result)
