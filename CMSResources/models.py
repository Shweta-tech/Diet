from django.db import models

# Create your models here.
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from . import blocks


class ResourcesPage(Page):

    templates = "CMSResources/resources_page.html"

    content = StreamField(
        [
            
            ("articlecards",blocks.ArticleCardBlock()),
            ("imagecards",blocks.ImageCardBlock()),
            ("videocards",blocks.VideoCardBlock()),
        ],
        null = True,
        blank = True
    )
    
    subtitle = models.CharField(max_length = 100, blank = True, null = True )
   
    content_panels = Page.content_panels + [

        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
        
    ]


