from flask import render_template
from flask.views import MethodView
import gbmodel

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()
        rows = model.select()
        entries = []
        for row in rows:
            entry = dict(key_id=row['id'], word=row['word'], lang=row['lang'],meaning=row['meaning'])
            entries.append(entry)
        return render_template('index.html', entries=entries)

