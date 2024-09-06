
import sys
import traceback
from flask import render_template, make_response, json
from ...configs_package.modules.logger_config import logger, get_message

def error_handlers_view(app):
    @app.errorhandler(404)
    def page_not_found(e):

        app.logger.error('Page not found: %s', e)
        image = "https://atlassianblog.wpengine.com/wp-content/uploads/2017/12/44-incredible-404-error-pages@3x.png"
        title = f"{e.code} {e.name}"
        error_code=e.code
        error_description = e.name
        message = "Oops! Something went wrong on our end. Please try again later."
        response = e.get_response()
        # replace the body with JSON
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"

        resp = make_response(render_template('errors/error.html', title=title, message=message, error_description=error_description, 
                                             image=image, error_code=error_code), 404)
        resp.headers['X-Something'] = 'Page Not Found'

        get_message(e, type='debug')

        return resp
    
    @app.errorhandler(500)
    def page_not_found(e):

        title = f"{e.code} {e.name}"
        error_code=e.code
        error_description = e.name
        message = "Oops! Something went wrong on our end. Please try again later."
        # Log the error
        app.logger.error('Internal Server Error: %s', e)
        image='https://static.doofinder.com/main-files/uploads/2019/09/error-500-doofinder.jpg'
        # Render the error page
        resp = make_response(render_template('errors/error.html', title=title, message=message, error_description=error_description, 
                                             image=image, error_code=error_code), 500)
        resp.headers['X-Something'] = 'Internal Server Error'

        get_message(e, type='debug')
        
        return resp
    
    @app.errorhandler(Exception)
    def handle_generic_error(e):
        title = "General error"
        error_code="Exp."
        error_description = f"An exception occurred {e}"
        message = "Oops! Something went wrong on our end. Please try again later."
        app.logger.error('Internal Server Error: %s', e)
        image=image='https://miro.medium.com/v2/resize:fit:1400/1*2Z41mMgjOxkUUuvIwd7Djw.png'
        resp = make_response(render_template('errors/error.html', title=title, message=message, error_description=error_description, 
                                             image=image, error_code=error_code), 500)
        resp.headers['X-Something'] = 'Generic Error'

        get_message(e, type='debug')
        
        return resp

    @app.errorhandler(400)
    def handle_unauthorized_error(e):

        title = f"{e.code} {e.name}"
        error_code=e.code
        error_description = e.name
        message = "Oops! Something went wrong on our end. Please try again later."
        image=image='https://www.techquintal.com/wp-content/uploads/2022/08/400-Bad-Request-Error.jpg'
        #resp = make_response(render_template('errors/400.html', message=f"{e.code} -{e.name}. Unauthorized 
        #                                     {e.description}", image=image, error_code=error_code), 400)
        resp = make_response(render_template('errors/error.html', title=title, message=message, error_description=error_description, 
                                             image=image, error_code=error_code), 400)
        resp.headers['X-Something'] = 'Unauthorized'

        get_message(e, type='debug')
        
        return resp
    
        
    @app.errorhandler(401)
    def handle_unauthorized_error(e):

        title = f"{e.code} {e.name}"
        error_code=e.code
        error_description = e.name
        message = "Oops! Something went wrong on our end. Please try again later."
        image=image='https://www.asktheegghead.com/wp-content/uploads/2019/12/401-error-wordpress-featured-image.jpg'
        resp = make_response(render_template('errors/error.html', title=title, message=message, error_description=error_description, 
                                             image=image, error_code=error_code), 401)
        resp.headers['X-Something'] = 'Unauthorized'

        get_message(e, type='debug')
       
        return resp

    @app.errorhandler(403)
    def handle_forbidden_error(e):

        title = f"{e.code} {e.name}"
        error_code=e.code
        error_description = e.name
        message = "Oops! Something went wrong on our end. Please try again later."
        image='https://www.online-tech-tips.com/wp-content/uploads/2021/06/http-403.jpeg'
        resp = make_response(render_template('errors/error.html', title=title, message=message, error_description=error_description, 
                                             image=image, error_code=error_code), 403)
        resp.headers['X-Something'] = 'Forbidden'

        get_message(e, type='debug')
        
        return resp

    @app.errorhandler(405)
    def handle_method_not_allowed_error(e):
        
        title = f"{e.code} {e.name}"
        error_code=e.code
        error_description = e.name
        message = "Oops! Something went wrong on our end. Please try again later."
        image='https://www.ionos.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/405-Method-Not-Allowed-t.jpg'
        resp = make_response(render_template('errors/error.html', title=title, message=message, error_description=error_description, 
                                             image=image, error_code=error_code), 405)
        resp.headers['X-Something'] = 'Method Not Allowed'

        get_message(e, type='debug')
        
        return resp
    
    @app.errorhandler(503)
    def unavailable_service(e):

        title = f"{e.code} {e.name}"
        error_code=e.code
        error_description = e.name
        message = "Oops! Something went wrong on our end. Please try again later."
        image='https://www.lifewire.com/thmb/3Zne74PQmtY62N1E02VkiNg78bQ=/768x0/filters:no_upscale():max_bytes(150000):strip_icc()/shutterstock_717832600-Converted-5a29aaf3b39d030037b2cda9.png'
        resp = make_response(render_template('errors/error.html', title=title, message=message, error_description=error_description, 
                                             image=image, error_code=error_code), 503)
        resp.headers['X-Something'] = 'Method Not Allowed'

        get_message(e, type='debug')
        
        return resp