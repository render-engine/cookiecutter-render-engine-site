"""
This is a simple app setup script created with `render-engine init`
"""

from render_engine import Site, Page, Collection

app = Site()
app.output_path = "{{cookiecutter.output_path}}"

app.site_vars.update({
    {% if site_title %}
    SITE_TITLE:"{{site_title}}",
    {% endif %}
    {% if site_url %}
    SITE_URL:"{{site_url}}",
    {% endif %}
    {% if site_description %}
    SITE_DESCRIPTION:"{{site_description}}",
    {% endif %}
    "OWNER":{
        "name": "{{owner['name']}}",
        "email": "{{owner['email']}}",
    },
    "NAVIGATION":[
        {
            "name": "Home",
            "url": "/",
        },
        {% if not skip_collection %}
        {
            "name": "Collection Page",
            "url": "/example-page.html",
        }
        {% endif %}
    ]
    })

@app.page
class Index(Page):
    template = "index.html"

{% if not skip_collection %}
@app.collection
class Pages(Collection):
    content_path = "{{collection_path}}" # path to content files
{% endif %}

{% if not blog %}

if __name__ == "__main__":
    app.render()
