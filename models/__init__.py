"""Initialize the reload function to recreate saved objects"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
