from flask import Flask,request,abort,jsonify,render_template
import dataset
from bson.json_util import dumps,default
import json
import codecs

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
db = dataset.connect('sqlite:///static/data/2017.db')

def get_text(data):
    for r in data:
        yield json.dumps(r,ensure_ascii=False)
@app.route('/api/2017')
def get_grade():
    print ('Request args: ' + str(dict(request.args)))
    query_dict = {}
    for key in ['日時','相手','球場','観衆']:
        arg = request.args.get(key)
        print(arg)
        if arg:
            query_dict[key] = arg

    data = db['Schedule_E'].find(**query_dict)
    l = list()
    for r in data:
        l.append(dict(r))
        # print(type(r))
    # return json.dumps(l,ensure_ascii=False)

    return render_template('show.html',
                           heading = "Schedule_E",
                           schedule = json.dumps(l,ensure_ascii=False)
)
    abort(404)

if __name__=='__main__':
    app.run(port=8000,debug=True)
