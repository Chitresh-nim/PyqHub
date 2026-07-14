from django.core.files.storage import Storage
from PyqProject.supabase_client import supabase


class SupabaseStorage(Storage):
    bucket_name = "pdfs"

    def _save(self, name, content):
        content.seek(0)
        supabase.storage.from_(self.bucket_name).upload(
            name,
            content.read(),
            {"content-type": content.content_type},
        )
        return name

    def exists(self, name):
        return False

    def url(self, name):
        return supabase.storage.from_(self.bucket_name).get_public_url(name)