from wagtail.core import blocks
from wagtail.core.blocks import StructBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

class ArticleCardBlock(blocks.StructBlock):
    
    title = blocks.CharBlock(required = True, help_text  = 'Add Title')
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [   
                ("title", blocks.CharBlock(required = True, help_text  = 'Title')),
                ("author", blocks.CharBlock(required = True, help_text  = 'Author')),
                ("description", blocks.TextBlock(required = True, help_text = 'Description')),
                ("article", blocks.RichTextBlock(required=True,help_text = 'Article'))
            ]
            
       )
    )
    
   
    class Meta:
        template="CMSResources/article_card.html"
        icon="media"
        label="Article Card"



class ImageCardBlock(blocks.StructBlock):
    
    title = blocks.CharBlock(required = True, help_text  = 'Add Title')
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [   
                ("title", blocks.CharBlock(required = True, help_text  = 'Title')),
                ("description", blocks.TextBlock(required = True, help_text = 'Description')),
                ("image", ImageChooserBlock()),
            ]
            
       )
    )
    
   
    class Meta:
        template="CMSResources/image_card.html"
        icon="media"
        label="Image Card"

class VideoCardBlock(blocks.StructBlock):
    
    title = blocks.CharBlock(required = True, help_text  = 'Add Title')
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required = True, help_text  = 'Add Title')),
                ("caption", blocks.CharBlock(required = True, help_text  = 'Caption')),
                ("video", EmbedBlock(label=("Video"))),
               
            ]
            
       )
    )
    
   
    class Meta:
        template="CMSResources/video_card.html"
        icon="media"
        label="Video Cards"


class ResourcesLinkBlock(blocks.StructBlock):
    
    title = blocks.CharBlock(required = True, help_text  = 'Add Title')
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [   
                ("title", blocks.CharBlock(required = True, help_text  = 'Title')),
                ("description", blocks.TextBlock(required = True, help_text = 'Description')),
                ("link", blocks.RichTextBlock(required=True,help_text = 'Resources Link')),
            ]
            
       )
    )
    
   
    class Meta:
        template="CMSResources/resourceslinks.html"
        icon="media"
        label="Resources Link"