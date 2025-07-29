from flask import Flask,jsonify,request

app=Flask(__name__) #Clase importada
@app.route('/') #Indica que es ruta raíz
def index(): #Vista index en forma de función
    return "<h1> API<h1>"

@app.route("/users/<user_id>")
def get_user(user_id): #Método Get
    user={'id':user_id,'name':'Mateo','telefono':"4060280"}

    query=request.args.get('query')
    if query:
        user["query"]=query   
    return jsonify(user),200


@app.route('/users',methods=["POST"])
def create_user():                     #No recibe ningún parámetro
    data=request.get_json()
    data['status']="user created"
    return jsonify(data),201

@app.route('/users/<user_id>',methods=["DELETE"])
def delete_user(user_id):
      return jsonify({"mensaje": f"Usuario con ID {user_id} eliminado"}), 202

@app.route('/users/<user_id>',methods=["PUT"])
def update_user(user_id):                   
    data=request.get_json()
    return jsonify({"mensaje": f"Usuario con ID {user_id} actualizado",
        "datos_actualizados": data}),200


if __name__ =='__main__': #Si está desde el archivo inicial se ejecuta
    app.run(debug=True,port=8080) #Modo depuración activado

