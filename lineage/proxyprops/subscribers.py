from Products.CMFCore.interfaces import IPropertiesTool
from collective.proxyproperties import ProxyProperties

def addProxyPropUtil(event):
    """Add a proxy property local util when a child site is created
    """
    sm = event.object.getSiteManager()
    sm.registerUtility(ProxyProperties(), IPropertiesTool)
