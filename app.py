from flask import Flask, render_template, redirect, url_for, session, request
from mock import ROLES, NAV
from blueprints import paciente, medico, administrativo, bioinformatico, gerente, transportista

app = Flask(__name__)
app.secret_key = "prototipo-exoma"
for m in (paciente, medico, administrativo, bioinformatico, gerente, transportista):
    app.register_blueprint(m.bp, url_prefix=f"/{m.bp.name}")

@app.context_processor
def ctx():
    r = session.get("rol")
    return dict(rol=r, rol_nombre=ROLES.get(r), nav=NAV.get(r, []))

@app.route("/")
def login(): return render_template("login.html", roles=ROLES)

@app.route("/entrar/<rol>")
def entrar(rol):
    if rol not in ROLES: return redirect(url_for("login"))
    session["rol"] = rol
    return redirect(url_for("verificar"))

@app.route("/verificar")  # simula "dispositivo nuevo"
def verificar(): return render_template("verificar.html")

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        rol = request.form.get("rol")
        if rol in ROLES:
            session["rol"] = rol
            # Redirige directo a la página de inicio de ese rol (ej: /medico/)
            return redirect(url_for(f"{rol}.inicio"))
    return render_template("registro.html", roles=ROLES)

@app.route("/ok")  # confirmación estática de cualquier acción
def ok(): return render_template("ok.html", m=request.args.get("m", "Acción realizada"), back=request.args.get("back", "/"))

if __name__ == "__main__":
    app.run(debug=True)
