"""GeoPoly public gui API."""
from . import runtime as _rt

GeoPolyApp = getattr(_rt, 'GeoPolyApp')
GeoPolyAppV2525 = getattr(_rt, 'GeoPolyAppV2525')
main = getattr(_rt, 'main')

def __getattr__(name):
    return getattr(_rt, name)

__all__ = ['GeoPolyApp', 'GeoPolyAppV2525', 'main']
