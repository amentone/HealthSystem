from flaskr import app, login_manager
from flask import render_template

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500

@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('errors/405.html'), 405

@app.errorhandler(502)
def bad_gateway(e):
    return render_template('errors/502.html'), 502

@app.errorhandler(400)
def bad_gateway(e):
    return render_template('errors/400.html'), 400

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('errors/unauthorized.html')
