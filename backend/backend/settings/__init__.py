from __future__ import absolute_import, unicode_literals

# Después de agregar una introducción absoluta, importe el método de contenido en el módulo actual: desde XX Importar XX como XX

from backend.settings.celery import app as celery_app



__all__ = ('celery_app',)