from flask import Flask, jsonify, request

app = Flask(__name__)  # Ativando o Flask

#Explicar como se utiliza
explicacao = [
    {
        "mensagem": "Use o método PUT na rota /soma  Vá em Body, selecione raw, escolha JSON e digite: "
                    '{"primeiro_numero": <valor>, "segundo_numero": <valor>}.'
    }
]

@app.route("/", methods=["GET"])
def explicar():
    return jsonify(explicacao)

@app.route("/soma", methods=['PUT'])
def soma_de_numeros():
    inclui = request.get_json()

    #Captura os números do JSON
    primeiro_numero = inclui.get('primeiro_numero')
    segundo_numero = inclui.get('segundo_numero')

    #Vendo se os números dados são int ou float
    if primeiro_numero is None or segundo_numero is None:
        return jsonify({"erro": "Os números precisam ser fornecidos no JSON da requisição."}), 400
    if not isinstance(primeiro_numero, (int, float)) or not isinstance(segundo_numero, (int, float)):
        return jsonify({"erro": "Os números precisam ser do tipo inteiro ou decimal."}), 400
    soma = primeiro_numero + segundo_numero
    return jsonify({"soma": soma})

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
