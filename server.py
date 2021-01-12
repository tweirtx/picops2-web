import flask

app = flask.Flask("cookies")

cookieflag = "picoPS2{cH0c0l@te_cH!p}"
clientsideflag = 'picoPS2{p30p13_c@nt_b3_tru5t3d}'

with open('clientside.html', 'r') as r:
    clientfile = r.read()

with open('client.js', 'r') as f:
    clientjs = f.read()


@app.route("/cookie")
def cookie():
    cookiecookie = flask.request.cookies.get("can_have_cookies")
    if cookiecookie != "True":
        resp = flask.make_response("You cannot have cookies!")
        resp.set_cookie('can_have_cookies', "False")
        return resp
    else:
        return f"You may have a cookie! I hope you like {cookieflag}!"


@app.route("/client")
def client():
    return clientfile


@app.route("/client.js")
def client_js():
    return clientjs


@app.route("/clientflag")
def client_flag():
    return clientsideflag


@app.route("/definitelynotaflag/")
def notaflag():
    return "picoPS2{h3r3_@r3_th3_r0b0t5}"


@app.route("/robots.txt")
def robots():
    return flask.send_from_directory(".", "robots.txt")


@app.route("/vm")
def vm():
    return flask.send_from_directory(".", "dfweb.zip") # Google account password: CPHS2150


if __name__ == "__main__":
    app.run()
