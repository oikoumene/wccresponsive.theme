from plone.app.layout.viewlets.common import LogoViewlet as BaseLogoViewlet
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from wcc.theme.interfaces import IThemeSettings
from zope.component.hooks import getSite
from wcc.theme import getSettings
from datetime import datetime

class LogoViewlet(BaseLogoViewlet):

    index = ViewPageTemplateFile('templates/logo.pt')

    def update(self):
        super(LogoViewlet, self).update()

        lang = self.portal_state.language()
        portal = self.portal_state.portal()
        logoTitle = self.portal_state.portal_title()

        logoName = 'logo-%s.png' % lang
        if hasattr(portal, logoName):
            self.logo_tag = portal.restrictedTraverse(logoName
                    ).tag(title=logoTitle, alt=logoTitle)

        navroot = self.portal_state.navigation_root()
        if hasattr(navroot, 'getField'):
            self.navigation_root_description = navroot.getField(
                'description').get(navroot)
        else:
            self.navigation_root_description = u''

        settings = getSettings()
        if settings.logo_url.strip():
            self.navigation_root_url = settings.logo_url


class SubsiteViewlet(ViewletBase):

    index = ViewPageTemplateFile('templates/subsitemeta.pt')

    def available(self):
        settings = getSettings()
        if settings.is_subsite:
            return True
        return False


class CopyrightViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/copyright.pt')

    def year(self):
        return datetime.now().year
