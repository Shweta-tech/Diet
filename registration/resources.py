from import_export import resources
from .models import User,SchoolCoordinator

class bulkResource(resources.ModelResource):
    class meta:
        model = SchoolCoordinator