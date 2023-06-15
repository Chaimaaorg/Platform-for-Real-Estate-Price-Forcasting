from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur l'application de prédiction de prix !"

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    try:
        # Get all features from the form data
        squareMeters = float(request.form['squareMeters'])
        numberOfRooms = int(request.form['numberOfRooms'])
        hasYard = int(request.form['hasYard'] == 'true')
        hasPool = int(request.form['hasPool'] == 'true')
        floors = int(request.form['floors'])
        cityCode = int(request.form['cityCode'])
        cityPartRange = int(request.form['cityPartRange'])
        numPrevOwners = int(request.form['numPrevOwners'])
        hasStormProtector = int(request.form['hasStormProtector'] == 'true')
        basement = int(request.form['basement'] == 'true')
        attic = int(request.form['attic'] == 'true')
        garage = int(request.form['garage'] == 'true')
        hasStorageRoom = int(request.form['hasStorageRoom'] == 'true')
        hasGuestRoom = int(request.form['hasGuestRoom'] == 'true')
        HouseAge = int(request.form['HouseAge'])

        estimated_price = util.get_estimated_price(
            squareMeters, numberOfRooms, hasYard, hasPool, floors, cityCode,
            cityPartRange, numPrevOwners, hasStormProtector, basement, attic,
            garage, hasStorageRoom, hasGuestRoom, HouseAge
        )

        response = jsonify({
            'estimated_price': estimated_price,
            'status': 'success'
        })
        
    except Exception as e:
        response = jsonify({
            'error': str(e),
            'status': 'error'
        })
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()