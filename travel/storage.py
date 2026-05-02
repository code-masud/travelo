from django.core.files.storage import Storage
from django.conf import settings
from supabase import create_client, Client
import uuid

class SupabaseStorage(Storage):
    def __init__(self):
        self.supabase = create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_KEY
        )
        self.bucket = settings.SUPABASE_BUCKET

    def _save(self, name, content):
        file_ext = name.split(".")[-1]
        file_name = f"{uuid.uuid4()}.{file_ext}"

        file_data = content.read()

        self.supabase.storage.from_(self.bucket).upload(
            file_name,
            file_data,
            {"content-type": content.content_type}
        )

        return file_name

    def url(self, name):
        return self.supabase.storage.from_(self.bucket).get_public_url(name)

    def exists(self, name):
        # simple check (Supabase doesn't require strict existence checks)
        return False

    def delete(self, name):
        self.supabase.storage.from_(self.bucket).remove([name])

    def open(self, name, mode="rb"):
        # optional: not needed for admin display
        raise NotImplementedError("Direct open not supported")