from flask import Flask ,jsonify ,request, render_template
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from sqlalchemy import text
app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend
# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/pp_lluvias'
# URI de la BBDD                      driver de la BD  user:clave@URL/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
db= SQLAlchemy(app)
ma=Marshmallow(app)



# defino la tabla
class Laprida(db.Model):   # la clase Producto hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    fecha=db.Column(db.Integer)
    refugio=db.Column(db.Float)
    sara=db.Column(db.Float)
    pozos=db.Column(db.Float)
    rural=db.Column(db.Float)
    tegua=db.Column(db.Float)
    alegre=db.Column(db.Float)
    
    def __init__(self,fecha,refugio,sara,pozos,rural,tegua,alegre):   #crea el  constructor de la clase
        self.fecha=fecha   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.refugio=refugio
        self.sara=sara
        self.pozos=pozos
        self.rural=rural
        self.tegua=tegua
        self.alegre=alegre

with app.app_context():
    db.create_all()  # crea las tablas
#  ************************************************************
class LapridaSchema(ma.Schema):
    class Meta:
        fields=('id','fecha','refugio','sara','pozos','rural','tegua','alegre')
laprida_schema=LapridaSchema()            # para crear un producto
lapridas_schema=LapridaSchema(many=True)  # multiples registros

# crea los endpoint o rutas (json) de Laprida
@app.route('/lapridas',methods=['GET'])
def get_Lapridas():
    all_lapridas=Laprida.query.all()     # query.all() lo hereda de db.Model
    result=lapridas_schema.dump(all_lapridas)  # .dump() lo hereda de ma.schema
    return jsonify(result)

@app.route('/lapridas/<id>',methods=['GET'])
def get_laprida(id):
    laprida=Laprida.query.get(id)
    return laprida_schema.jsonify(laprida)


@app.route('/lapridas/<id>',methods=['DELETE'])
def delete_laprida(id):
    laprida=Laprida.query.get(id)
    db.session.delete(laprida)
    db.session.commit()
    return laprida_schema.jsonify(laprida)

@app.route('/lapridas', methods=['POST']) # crea ruta o endpoint
def create_laprida():
    print(request.json)  # request.json contiene el json que envio el cliente
    fecha=request.json['fecha']
    refugio=request.json['refugio']
    sara=request.json['sara']
    pozos=request.json['pozos']
    rural=request.json['rural']
    tegua=request.json['tegua']
    alegre=request.json['alegre']

    new_laprida=Laprida(fecha,refugio,sara,pozos,rural,tegua,alegre)
    db.session.add(new_laprida)
    db.session.commit()
    return laprida_schema.jsonify(new_laprida)

@app.route('/lapridas/<id>' ,methods=['PUT'])
def update_laprida(id):
    laprida=Laprida.query.get(id)
    fecha=request.json['fecha']
    refugio=request.json['refugio']
    sara=request.json['sara']
    pozos=request.json['pozos']
    rural=request.json['rural']
    tegua=request.json['tegua']
    alegre=request.json['alegre']


    laprida.fecha=fecha
    laprida.refugio=refugio
    laprida.sara=sara
    laprida.pozos=pozos
    laprida.rural=rural
    laprida.tegua=tegua
    laprida.alegre=alegre


    db.session.commit()
    return laprida_schema.jsonify(laprida)

#######Necochea
# defino la tabla
class Necochea(db.Model):   # la clase Producto hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    fecha=db.Column(db.Integer)
    cooperativa=db.Column(db.Float)
    santamarina=db.Column(db.Float)
    zubillaga=db.Column(db.Float)
    buck=db.Column(db.Float)
    fernandez=db.Column(db.Float)
    energia=db.Column(db.Float)
    olivera=db.Column(db.Float)
    toscas=db.Column(db.Float)

    
    def __init__(self,fecha,cooperativa,santamarina,zubillaga,buck,fernandez,energia,olivera,toscas):   #crea el  constructor de la clase
        self.fecha=fecha   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.cooperativa=cooperativa
        self.santamarina=santamarina
        self.zubillaga=zubillaga
        self.buck=buck
        self.fernandez=fernandez
        self.energia=energia
        self.olivera=olivera
        self.toscas=toscas


with app.app_context():
    db.create_all()  # crea las tablas
#  ************************************************************
class NecocheaSchema(ma.Schema):
    class Meta:
        fields=('id','fecha','cooperativa','santamarina','zubillaga','buck','fernandez','energia','olivera','toscas')
necochea_schema=NecocheaSchema()            # para crear un producto
necocheas_schema=NecocheaSchema(many=True)  # multiples registros

# crea los endpoint o rutas (json) de Necochea
@app.route('/necocheas',methods=['GET'])
def get_necocheas():
    all_necocheas=Necochea.query.all()     # query.all() lo hereda de db.Model
    result=necocheas_schema.dump(all_necocheas)  # .dump() lo hereda de ma.schema
    return jsonify(result)

@app.route('/necocheas/<id>',methods=['GET'])
def get_necochea(id):
    necochea=Necochea.query.get(id)
    return necochea_schema.jsonify(necochea)


@app.route('/necocheas/<id>',methods=['DELETE'])
def delete_necochea(id):
    necochea=Necochea.query.get(id)
    db.session.delete(necochea)
    db.session.commit()
    return necochea_schema.jsonify(necochea)

@app.route('/necocheas', methods=['POST']) # crea ruta o endpoint
def create_necochea():
    print(request.json)  # request.json contiene el json que envio el cliente
    fecha=request.json['fecha']
    cooperativa=request.json['cooperativa']
    santamarina=request.json['santamarina']
    zubillaga=request.json['zubillaga']
    buck=request.json['buck']
    fernandez=request.json['fernandez']
    energia=request.json['energia']
    olivera=request.json['olivera']
    toscas=request.json['toscas']  
 
    new_necochea=Necochea(fecha,cooperativa,santamarina,zubillaga,buck,fernandez,energia,olivera,toscas)
    db.session.add(new_necochea)
    db.session.commit()
    return necochea_schema.jsonify(new_necochea)

@app.route('/necocheas/<id>' ,methods=['PUT'])
def update_necochea(id):
    necochea=Necochea.query.get(id)

    fecha=request.json['fecha']
    cooperativa=request.json['cooperativa']
    santamarina=request.json['santamarina']
    zubillaga=request.json['zubillaga']
    buck=request.json['buck']
    fernandez=request.json['fernandez']
    energia=request.json['energia']
    olivera=request.json['olivera']
    toscas=request.json['toscas']  

    necochea.fecha=fecha
    necochea.cooperativa=cooperativa
    necochea.santamarina=santamarina
    necochea.zubillaga=zubillaga
    necochea.buck=buck
    necochea.fernandez=fernandez
    necochea.energia=energia
    necochea.olivera=olivera
    necochea.toscas=toscas


    db.session.commit()
    return necochea_schema.jsonify(necochea)



# defino la tabla Balcarce
class Balcarce(db.Model):   # la clase Producto hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    fecha=db.Column(db.Integer)
    volcan=db.Column(db.Float)
    agrar=db.Column(db.Float)
    inta=db.Column(db.Float)
    pinos=db.Column(db.Float)
    agustin=db.Column(db.Float)

    
    def __init__(self,fecha,volcan,agrar,inta,pinos,agustin):   #crea el  constructor de la clase
        self.fecha=fecha   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.volcan=volcan
        self.agrar=agrar
        self.inta=inta
        self.pinos=pinos
        self.agustin=agustin


with app.app_context():
    db.create_all()  # crea las tablas
#  ************************************************************
class BalcarceSchema(ma.Schema):
    class Meta:
        fields=('id','fecha','volcan','agrar','inta','pinos','agustin')
balcarce_schema=BalcarceSchema()            # para crear un producto
balcarces_schema=BalcarceSchema(many=True)  # multiples registros

# crea los endpoint o rutas (json) de balcarce
@app.route('/balcarces',methods=['GET'])
def get_balcarces():
    all_balcarces=Balcarce.query.all()     # query.all() lo hereda de db.Model
    result=balcarces_schema.dump(all_balcarces)  # .dump() lo hereda de ma.schema
    return jsonify(result)

@app.route('/balcarces/<id>',methods=['GET'])
def get_balcarce(id):
    balcarce=Balcarce.query.get(id)
    return balcarce_schema.jsonify(balcarce)


@app.route('/balcarces/<id>',methods=['DELETE'])
def delete_balcarce(id):
    balcarce=Balcarce.query.get(id)
    db.session.delete(balcarce)
    db.session.commit()
    return balcarce_schema.jsonify(balcarce)

@app.route('/balcarces', methods=['POST']) # crea ruta o endpoint
def create_balcarce():
    print(request.json)  # request.json contiene el json que envio el cliente
    fecha=request.json['fecha']
    volcan=request.json['volcan']
    agrar=request.json['agrar']
    inta=request.json['inta']
    pinos=request.json['pinos']
    agustin=request.json['agustin']

    new_balcarce=Balcarce(fecha,volcan,agrar,inta,pinos,agustin)
    db.session.add(new_balcarce)
    db.session.commit()
    return balcarce_schema.jsonify(new_balcarce)

@app.route('/balcarces/<id>' ,methods=['PUT'])
def update_balcarce(id):
    balcarce=Balcarce.query.get(id)
    fecha=request.json['fecha']
    volcan=request.json['volcan']
    agrar=request.json['agrar']
    inta=request.json['inta']
    pinos=request.json['pinos']
    agustin=request.json['agustin']

    balcarce.fecha=fecha
    balcarce.volcan=volcan
    balcarce.agrar=agrar
    balcarce.inta=inta
    balcarce.pinos=pinos
    balcarce.agustin=agustin

    db.session.commit()
    return balcarce_schema.jsonify(balcarce)

# defino la tabla de MDP
class Mdp(db.Model):   # la clase Producto hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    fecha=db.Column(db.Integer)
    cuda=db.Column(db.Float)
    serrana=db.Column(db.Float)
    biocca=db.Column(db.Float)
    
    def __init__(self,fecha,cuda,serrana,biocca):   #crea el  constructor de la clase
        self.fecha=fecha   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.cuda=cuda
        self.serrana=serrana
        self.biocca=biocca

with app.app_context():
    db.create_all()  # crea las tablas
#  ************************************************************
class MdpSchema(ma.Schema):
    class Meta:
        fields=('id','fecha','cuda','serrana','biocca')
mdp_schema=MdpSchema()            # para crear un producto
mdps_schema=MdpSchema(many=True)  # multiples registros

# crea los endpoint o rutas (json) de Mdp
@app.route('/mdps',methods=['GET'])
def get_mdps():
    all_mdps=Mdp.query.all()     # query.all() lo hereda de db.Model
    result=mdps_schema.dump(all_mdps)  # .dump() lo hereda de ma.schema
    return jsonify(result)

@app.route('/mdps/<id>',methods=['GET'])
def get_mdp(id):
    mdp=Mdp.query.get(id)
    return mdp_schema.jsonify(mdp)


@app.route('/mdps/<id>',methods=['DELETE'])
def delete_mdp(id):
    mdp=Mdp.query.get(id)
    db.session.delete(mdp)
    db.session.commit()
    return mdp_schema.jsonify(mdp)

@app.route('/mdps', methods=['POST']) # crea ruta o endpoint
def create_mdp():
    print(request.json)  # request.json contiene el json que envio el cliente
    fecha=request.json['fecha']
    cuda=request.json['cuda']
    serrana=request.json['serrana']
    biocca=request.json['biocca']

    
    new_mdp=Mdp(fecha,cuda,serrana,biocca)
    db.session.add(new_mdp)
    db.session.commit()
    return mdp_schema.jsonify(new_mdp)

@app.route('/mdps/<id>' ,methods=['PUT'])
def update_mdp(id):
    mdp=Mdp.query.get(id)
    fecha=request.json['fecha']
    cuda=request.json['cuda']
    serrana=request.json['serrana']
    biocca=request.json['biocca']

    mdp.fecha=fecha
    mdp.cuda=cuda
    mdp.serrana=serrana
    mdp.biocca=biocca

    db.session.commit()
    return mdp_schema.jsonify(mdp)


# defino la tabla de Benito
class Benito(db.Model):   # la clase Producto hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    fecha=db.Column(db.Integer)
    campoamor=db.Column(db.Float)
    lopez=db.Column(db.Float)
    dionisia=db.Column(db.Float)
    smn=db.Column(db.Float)
    uriburu=db.Column(db.Float)

    
    def __init__(self,fecha,campoamor,lopez,dionisia,smn,uriburu):   #crea el  constructor de la clase
        self.fecha=fecha   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.campoamor=campoamor
        self.lopez=lopez
        self.dionisia=dionisia
        self.smn=smn
        self.uriburu=uriburu


with app.app_context():
    db.create_all()  # crea las tablas
#  ************************************************************
class BenitoSchema(ma.Schema):
    class Meta:
        fields=('id','fecha','campoamor','lopez','dionisia','smn','uriburu')
benito_schema=BenitoSchema()            # para crear un producto
benitos_schema=BenitoSchema(many=True)  # multiples registros

# crea los endpoint o rutas (json) de benito
@app.route('/benitos',methods=['GET'])
def get_Benitos():
    all_benitos=Benito.query.all()     # query.all() lo hereda de db.Model
    result=benitos_schema.dump(all_benitos)  # .dump() lo hereda de ma.schema
    return jsonify(result)

@app.route('/benitos/<id>',methods=['GET'])
def get_benito(id):
    benito=Benito.query.get(id)
    return benito_schema.jsonify(benito)


@app.route('/benitos/<id>',methods=['DELETE'])
def delete_benito(id):
    benito=Benito.query.get(id)
    db.session.delete(benito)
    db.session.commit()
    return benito_schema.jsonify(benito)

@app.route('/benitos', methods=['POST']) # crea ruta o endpoint
def create_benito():
    print(request.json)  # request.json contiene el json que envio el cliente
    fecha=request.json['fecha']
    campoamor=request.json['campoamor']
    lopez=request.json['lopez']
    dionisia=request.json['dionisia']
    smn=request.json['smn']
    uriburu=request.json['uriburu']

    new_benito=Benito(fecha,campoamor,lopez,dionisia,smn,uriburu)
    db.session.add(new_benito)
    db.session.commit()
    return benito_schema.jsonify(new_benito)

@app.route('/benitos/<id>' ,methods=['PUT'])
def update_benito(id):
    benito=Benito.query.get(id)
    fecha=request.json['fecha']
    campoamor=request.json['campoamor']
    lopez=request.json['lopez']
    dionisia=request.json['dionisia']
    smn=request.json['smn']
    uriburu=request.json['uriburu']

    benito.fecha=fecha
    benito.campoamor=campoamor
    benito.lopez=lopez
    benito.dionisia=dionisia
    benito.smn=smn
    benito.uriburu=uriburu

    db.session.commit()
    return benito_schema.jsonify(benito)


# defino la tabla de Loberia
class Loberia(db.Model):   # la clase Producto hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    fecha=db.Column(db.Integer)
    pieres=db.Column(db.Float)
    loberia=db.Column(db.Float)
    manuel=db.Column(db.Float)
    cantabria=db.Column(db.Float)

    
    def __init__(self,fecha,pieres,loberia,manuel,cantabria):   #crea el  constructor de la clase
        self.fecha=fecha   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.pieres=pieres
        self.loberia=loberia
        self.manuel=manuel
        self.cantabria=cantabria



with app.app_context():
    db.create_all()  # crea las tablas
#  ************************************************************
class LoberiaSchema(ma.Schema):
    class Meta:
        fields=('id','fecha','pieres','loberia','manuel','cantabria')
loberia_schema=LoberiaSchema()            # para crear un producto
loberias_schema=LoberiaSchema(many=True)  # multiples registros

# crea los endpoint o rutas (json) de benito
@app.route('/loberias',methods=['GET'])
def get_Loberias():
    all_loberias=Loberia.query.all()     # query.all() lo hereda de db.Model
    result=loberias_schema.dump(all_loberias)  # .dump() lo hereda de ma.schema
    return jsonify(result)

@app.route('/loberias/<id>',methods=['GET'])
def get_loberia(id):
    loberia=Loberia.query.get(id)
    return loberia_schema.jsonify(loberia)


@app.route('/loberias/<id>',methods=['DELETE'])
def delete_loberia(id):
    loberia=Loberia.query.get(id)
    db.session.delete(loberia)
    db.session.commit()
    return loberia_schema.jsonify(loberia)

@app.route('/loberias', methods=['POST']) # crea ruta o endpoint
def create_loberia():
    print(request.json)  # request.json contiene el json que envio el cliente
    fecha=request.json['fecha']
    pieres=request.json['pieres']
    loberia=request.json['loberia']
    manuel=request.json['manuel']
    cantabria=request.json['cantabria']

    new_loberia=Loberia(fecha,pieres,loberia,manuel,cantabria)
    db.session.add(new_loberia)
    db.session.commit()
    return loberia_schema.jsonify(new_loberia)

@app.route('/loberias/<id>' ,methods=['PUT'])
def update_loberia(id):
    loberia=Loberia.query.get(id)
    fecha=request.json['fecha']
    pieres=request.json['pieres']
    loberia=request.json['loberia']
    manuel=request.json['manuel']
    cantabria=request.json['cantabria']

    loberia.fecha=fecha
    loberia.pieres=pieres
    loberia.loberia=loberia
    loberia.manuel=manuel
    loberia.cantabria=cantabria

    db.session.commit()
    return loberia_schema.jsonify(loberia)

# defino la tabla de Lamadrid
class Lamadrid(db.Model):   # la clase Producto hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    fecha=db.Column(db.Integer)
    colina=db.Column(db.Float)
    querencia=db.Column(db.Float)
    lamadrid=db.Column(db.Float)

    
    def __init__(self,fecha,colina, querencia, lamadrid):   #crea el  constructor de la clase
        self.fecha=fecha   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.colina=colina
        self.querencia=querencia
        self.lamadrid=lamadrid
        

with app.app_context():
    db.create_all()  # crea las tablas
#  ************************************************************
class LamadridSchema(ma.Schema):
    class Meta:
        fields=('id','fecha', 'colina', 'querencia', 'lamadrid')
lamadrid_schema=LamadridSchema()            # para crear un producto
lamadrids_schema=LamadridSchema(many=True)  # multiples registros

# crea los endpoint o rutas (json) de Lamadrid
@app.route('/lamadrids',methods=['GET'])
def get_Lamadrids():
    all_lamadrids=Lamadrid.query.all()     # query.all() lo hereda de db.Model
    result=lamadrids_schema.dump(all_lamadrids)  # .dump() lo hereda de ma.schema
    return jsonify(result)

@app.route('/lamadrids/<id>',methods=['GET'])
def get_lamadrid(id):
    lamadrid=Lamadrid.query.get(id)
    return lamadrid_schema.jsonify(lamadrid)


@app.route('/lamadrids/<id>',methods=['DELETE'])
def delete_lamadrid(id):
    lamadrid=Lamadrid.query.get(id)
    db.session.delete(lamadrid)
    db.session.commit()
    return lamadrid_schema.jsonify(lamadrid)

@app.route('/lamadrids', methods=['POST']) # crea ruta o endpoint
def create_lamadrid():
    print(request.json)  # request.json contiene el json que envio el cliente
    fecha=request.json['fecha']
    colina=request.json['colina']
    querencia=request.json['querencia']
    lamadrid=request.json['lamadrid']

    new_lamadrid=Lamadrid(fecha,colina, querencia, lamadrid)
    db.session.add(new_lamadrid)
    db.session.commit()
    return lamadrid_schema.jsonify(new_lamadrid)

@app.route('/lamadrids/<id>' ,methods=['PUT'])
def update_lamadrid(id):
    lamadrid=Lamadrid.query.get(id)
    fecha=request.json['fecha']
    colina=request.json['colina']
    querencia=request.json['querencia']
    lamadrid=request.json['lamadrid']

    lamadrid.fecha=fecha
    lamadrid.colina=colina
    lamadrid.querencia=querencia
    lamadrid.lamadrid=lamadrid

    db.session.commit()
    return lamadrid_schema.jsonify(lamadrid)

#################################
#########lluvias


# defino la tabla
class Lluvia(db.Model):    
    id=db.Column(db.Integer, primary_key=True)   
    fecha=db.Column(db.DateTime)
    prom_balcarce=db.Column(db.Float)
    prom_benito=db.Column(db.Float)
    prom_lamadrid=db.Column(db.Float)
    prom_laprida=db.Column(db.Float)
    prom_loberia=db.Column(db.Float)
    prom_mdp=db.Column(db.Float)
    prom_necochea=db.Column(db.Float)
    
    def __init__(self,fecha,prom_balcarce, prom_benito, prom_lamadrid, prom_laprida, prom_loberia, prom_mdp, prom_necochea):   #crea el  constructor de la clase
        self.fecha=fecha   
        self.prom_balcarce=prom_balcarce
        self.prom_benito=prom_benito
        self.prom_lamadrid=prom_lamadrid
        self.prom_laprida=prom_laprida
        self.prom_loberia=prom_loberia
        self.prom_mdp=prom_mdp
        self.prom_necochea=prom_necochea

with app.app_context():
    db.create_all()  # crea las tablas

class LluviaSchema(ma.Schema):
    class Meta:
        fields=('id','fecha','prom_balcarce', 'prom_benito', 'prom_lamadrid', 'prom_laprida', 'prom_loberia', 'prom_mdp', 'prom_necochea')
lluvia_schema=LluviaSchema()            # para crear un producto
lluvias_schema=LluviaSchema(many=True)

@app.route('/')
def index():
    now = datetime.now()
    return render_template('lluvias.html', current_time=now)


@app.route('/lluvias/<id>' ,methods=['PUT'])
def update_lluvia(id):
    lluvia=Lluvia.query.get(id)
    fecha=request.json['fecha']
    prom_balcarce=request.json['prom_balcarce']
    prom_benito=request.json['prom_benito']
    prom_lamadrid=request.json['prom_lamadrid']
    prom_laprida=request.json['prom_laprida']
    prom_loberia=request.json['prom_loberia']
    prom_mdp=request.json['prom_mdp']
    prom_necochea=request.json['prom_necochea']

    lluvia.fecha=fecha
    lluvia.prom_balcarce=prom_balcarce
    lluvia.prom_benito=prom_benito
    lluvia.prom_lamadrid=prom_lamadrid
    lluvia.prom_laprida=prom_laprida
    lluvia.prom_loberia=prom_loberia
    lluvia.prom_mdp=prom_mdp
    lluvia.prom_necochea=prom_necochea

    db.session.commit()
    return lluvia_schema.jsonify(lluvia)


@app.route('/lluvias', methods=['GET','POST'])
def consulta_promedios():
    query = '''
        SELECT fecha,
            ROUND(prom_balcarce, 2) as prom_balcarce, 
            ROUND(prom_benito, 2) as prom_benito, 
            ROUND(prom_lamadrid, 2) as prom_lamadrid, 
            ROUND(prom_laprida, 2) as prom_laprida, 
            ROUND(prom_loberia, 2) as prom_loberia, 
            ROUND(prom_mdp, 2) as prom_mdp, 
            ROUND(prom_necochea, 2) as prom_necochea
        FROM (
            SELECT b.fecha,
                (b.volcan + b.agrar + b.inta + b.pinos + b.agustin)/5 as prom_balcarce, 
                (be.campoamor + be.lopez + be.dionisia + be.smn + be.uriburu)/5 as prom_benito, 
                (lam.colina + lam.querencia + lam.lamadrid)/3 as prom_lamadrid, 
                (lap.refugio + lap.sara + lap.pozos + lap.rural + lap.tegua + lap.alegre)/6 as prom_laprida,
                (lo.pieres + lo.loberia + lo.manuel + lo.cantabria)/4 as prom_loberia, 
                (m.cuda + m.serrana + m.biocca)/3 as prom_mdp,
                (n.cooperativa + n.santamarina + n.zubillaga + n.buck + n.fernandez + n.energia + n.olivera + n.toscas)/8 as prom_necochea
            FROM balcarce b
                JOIN benito be ON b.id = be.id 
                JOIN lamadrid lam ON b.id = lam.id 
                JOIN laprida lap ON b.id = lap.id 
                JOIN loberia lo ON b.id = lo.id 
                JOIN mdp m ON b.id = m.id 
                JOIN necochea n ON b.id = n.id 
            GROUP BY b.id
        ) as lluvias
    '''

    # Ejecuta este query usando estos parametros
    result = db.engine.execute(query)
    
    # Obtenemos los resultados como una lista de diccionarios
    var = [dict(row) for row in result]

    
    return jsonify(var)
    


# programa principal *******************************
if __name__=='__main__':  
    app.run(debug=True, port=5000)
