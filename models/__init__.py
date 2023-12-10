#!/usr/bin/python3
"""__init__ magic method for models directory"""
"""Daniel Mayowa"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
