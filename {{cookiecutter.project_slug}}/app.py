"""
This is a simple app setup script created with `render-engine init`
"""

from render_engine import (
    Site,
    Page,
    Collection,
    {% if not cookiecutter.skip_blog %}
    Blog
)
from render_engine.parsers.markdown import MarkdownPageParser
{% else %}
)
{% endif %}

app = Site()
app.output_path = "{{cookiecutter.output_path}}"

app.site_vars.update({
    "SITE_TITLE":"{{cookiecutter.SITE_TITLE}}",
    "SITE_URL":"{{cookiecutter.SITE_URL}}",
    "SITE_DESCRIPTION":"{{cookiecutter.SITE_DESCRIPTION}}",
    "OWNER":{
        "name": "{{cookiecutter.author_name}}",
        "email": "{{cookiecutter.author_email}}",
    },
    "NAVIGATION":[
        {
            "name": "Home",
            "url": "/",
        },{% if not cookiecutter.skip_collection %}
        {
            "name": "Collection Page",
            "url": "/example-page.html",
        }{% endif %}{% if not cookiecutter.skip_blog %}
        {
            "name": "Blog",
            "url": "/blog/blog.html",
        }{% endif %}
    ]
    })

@app.page
class Index(Page):
    template = "index.html"

{% if not cookiecutter.skip_collection %}
@app.collection
class Pages(Collection):
    content_path = "{{cookiecutter._collection.content_path}}" # path to content files
    routes = ["{{cookiecutter._collection.routes}}"] # route to collection page
    template = "page.html"
{% endif %}

{% if not cookiecutter.skip_blog %}
@app.collection
class Blog(Blog):
    content_path = "{{cookiecutter._blog.content_path}}" # path to content files
    routes = ["{{cookiecutter._blog.routes}}"] # route to collection page
    pageParser = MarkdownPageParser
    template = "page.html"
{% endif %}

if __name__ == "__main__":
    app.render()
