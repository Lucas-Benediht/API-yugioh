from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar_cartas', methods=['GET'])
def buscar_cartas():
    nome_carta = request.args.get('nome_carta')

    if nome_carta:
        url = f'https://db.ygoprodeck.com/api/v7/cardinfo.php?name={nome_carta}'
        response = requests.get(url)
          
        if response.status_code == 200:
            data = response.json()
            cartas = data.get('data', [])

            if cartas:
                carta = cartas[0] 
        
                if carta.get('card_images'):
                    image_url = carta['card_images'][0]['image_url']
                else:
                    image_url = None
                return render_template('index.html', carta=carta, image_url=image_url)
            else:
                return render_template('index.html', error='Carta não encontrada')
        else:
            
            return render_template('index.html', error='Erro ao buscar carta')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



