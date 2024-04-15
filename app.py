#main app

from flask import Flask,render_template,request
import volume_controller
app = Flask(__name__)

#index route -> controller page
@app.get('/')
def index():
    return render_template("index.html")

@app.get('/volume_up')
def vol_up()->str:
    volume_controller.volume_up()
    return "success: Turn that up"

@app.get('/volume_down')
def vol_down()->str:
    volume_controller.volume_down()
    return "success: Turn that down"
@app.get('/volume_mute')
def vol_mute():
    volume_controller.mute_audio()
    return "success: Your nuisance has been nerfed! :)"

@app.get('/volume_unmute')
def vol_unmute():
    volume_controller.unmute_audio()
    return "success: Let there be music!"

@app.post('/volume_absolute')
def vol_abs():
    """
    {
    'level':56
    }
    """
    level:int = int(request.get_json()['level'])
    volume_controller.set_absolute_volume(level)
    return "success: Audio level set"
app.run(host='0.0.0.0',debug=True)
