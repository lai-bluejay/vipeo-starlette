from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates
import uvicorn

import os
import sys
root = os.path.dirname(os.path.abspath(__file__))
sys.path.append("%s/.." % root)
sys.path.append(u"{0:s}".format(root))
from src.forms import VipListForm, make_choice

import requests


templates = Jinja2Templates(directory='templates')
print(templates)

app = Starlette(debug=True)
app.mount('/static', StaticFiles(directory='statics'), name='static')



@app.route('/', methods=['GET', 'POST'])
async def index(request):
    xform = await request.form()
    form = VipListForm(xform)
    platforms = make_choice('platformlist')
    if form.validate():
        return RedirectResponse(f'{form.parser.data}{form.url.data}')
    return templates.TemplateResponse('index.html', {'request':request,'form':form, 'platforms':platforms})


@app.route('/error')
async def error(request):
    """
    An example error. Switch the `debug` setting to see either tracebacks or 500 pages.
    """
    raise RuntimeError("Oh no")


@app.exception_handler(404)
async def not_found(request, exc):
    """
    Return an HTTP 404 page.
    """
    template = "404.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=404)


@app.exception_handler(500)
async def server_error(request, exc):
    """
    Return an HTTP 500 page.
    """
    template = "500.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=500)




if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
