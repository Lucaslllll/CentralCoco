from app import app # app está dentro do meu init principal


@app.route("/")
def index():
	return "Tua mae aa"


