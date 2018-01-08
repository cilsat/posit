import psycopg2 as pg
from tornado.log import enable_pretty_logging
from tornado_json.requesthandlers import APIHandler
from tornado_json import schema

enable_pretty_logging()
con = pg.connect(database='ehp', user='postgis', password='postgis')


class SawitHealthHandler(APIHandler):
    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "blok": {"type": "array", "items": {"type": "string"}}
            }
        },
        input_example={
            "blok": ["A10", "F03", "C25"]
        },
        output_schema={
            "type": "object",
            "properties": {
                "normal": {"type": "number"},
                "supply": {"type": "number"},
                "dead": {"type": "number"},
                "encumbrance": {"type": "number"},
                "new": {"type": "number"},
                "yellow": {"type": "number"},
                "special": {"type": "number"}
            }
        },
        output_example={
            "normal": 435,
            "supply": 13,
            "dead": 0,
            "encumbrance": 1,
            "new": 3,
            "yellow": 57,
            "special": 0
        },
    )
    def post(self):
        """
        POST the required parameters
        * `blok`: blok
        """
        blok = self.body['blok']
        if len(blok) > 0:
            if len(blok) > 1:
                tail = ''.join([" or blok = '" + b + "'" for b in blok[1:]])
            else:
                tail = ''
            query = "select descriptio, count(*) from sawit where blok = '" + \
                blok[0] + "'" + tail + " group by descriptio"
            print(query)
            cur = con.cursor()
            cur.execute(query)
            data = dict(cur.fetchall())

        nmap = {
            "normal": "NORMAL PALM",
            "supply": "SUPPLY PALM",
            "dead": "DIE PALM",
            "encumbrance": "ENCUMBRANCES",
            "new": "NEWLY PLANTED PALM",
            "yellow": "YELLOW PALM",
            "special": "SPECIAL CONDITION"
        }

        return {key: (data[val] if val in data.keys() else 0) for key, val in nmap.items()}

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Server", "Posit v0.1.0.0")
        self.set_header("Access-Control-Allow-Headers",
                        'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type')
        self.set_header('Access-Control-Allow-Methods', 'POST, OPTIONS')

    def options(self):
        self.set_status(204)
        self.clear_header('Content-Type')
        self.finish()
