from flask import Blueprint, render_template
from mock import DATA

def make(name, pages):
    """Crea un blueprint donde cada página es una ruta que renderiza templates/<name>/<page>.html con datos mock."""
    bp = Blueprint(name, __name__)
    for page in pages:
        bp.add_url_rule("/" if page == "inicio" else f"/{page}", page,
                        (lambda p: lambda: render_template(f"{name}/{p}.html", **DATA))(page))
    return bp
