![](website-image.PNG)
# House Price Prediction Application

## Overview
This web application predicts house prices based on various features using a machine learning model. The application consists of a Flask backend serving a machine learning model and a responsive frontend interface for users to input house details.

## Features
- Real-time price prediction
- 15 different input parameters including:
  - Square meters
  - Number of rooms
  - House features (yard, pool, basement, attic, etc.)
  - Location details (city code, city part range)
  - Property characteristics (age, previous owners, etc.)
- Responsive web interface
- Client-side input validation
- Error handling

## Technology Stack
- **Frontend**: HTML, CSS, JavaScript, jQuery
- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn
- **Data Processing**: NumPy, Pandas


## Installation

### Prerequisites
- Python 3.8 or higher
- Conda (recommended) or pip

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Chaimaaorg/Platform-for-Real-Estate-Price-Forcasting.git
   ```

2. Create and activate a Conda environment:
   ```bash
   conda create --name real_estate python=3.8
   conda activate real_estate
   ```

3. Install required packages:
   ```bash
   conda install scikit-learn pandas flask numpy
   ```
   
   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask server:
   ```bash
   python server/server.py
   ```
   The server will start on http://127.0.0.1:5000/

2. Open the application in your web browser:
   - Navigate to the project directory
   - Open index.html in a web browser
   - Or setup a local server to serve the frontend files

## Usage

1. Fill in the house details in the form:
   - Enter square meters
   - Specify number of rooms
   - Check applicable features (yard, pool, etc.)
   - Enter location details
   - Provide other property characteristics

2. Click "Estimate Price" to get the prediction

3. The estimated price will be displayed in Euros

## Model Information

The prediction model is trained on Paris real estate data and considers the following features:
- squareMeters
- numberOfRooms
- hasYard
- hasPool
- floors
- cityCode
- cityPartRange
- numPrevOwners
- hasStormProtector
- basement
- attic
- garage
- hasStorageRoom
- hasGuestRoom
- HouseAge

## API Endpoints

### Predict Home Price
- **URL**: `/predict_home_price`
- **Method**: POST
- **Data Parameters**: All house features as form data
- **Response**: JSON with estimated price
  ```json
  {
    "estimated_price": 350000.00,
    "status": "success"
  }
  ```

## Error Handling
- Client-side validation for required fields
- Server-side error handling with appropriate error messages
- API error responses with descriptive messages

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
