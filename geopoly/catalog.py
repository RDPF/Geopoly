"""GeoPoly public catalog API (v27.1b).

Explicit public imports for the catalog layer.
"""
from .runtime import (
    CatalogItem, CATALOG, CATALOG_ITEMS, deduplicate_catalog_items, safe_name,
)

__all__ = [
    'CatalogItem', 'CATALOG', 'CATALOG_ITEMS',
    'deduplicate_catalog_items', 'safe_name',
]
