function getBooleanValue(elementId) {
  return document.getElementById(elementId).checked;
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  
  // Validate required fields
  const cityCode = document.getElementById("uiCityCode").value;
  const cityPartRange = document.getElementById("uiCityPartRange").value;
  
  if (!cityCode || !cityPartRange) {
      alert("Please fill in all required fields (City Code and City Part Range)");
      return;
  }

  const formData = {
      squareMeters: parseFloat(document.getElementById("uiSquareMeters").value),
      numberOfRooms: parseInt(document.getElementById("uiNumberOfRooms").value),
      hasYard: getBooleanValue("uiHasYard"),
      hasPool: getBooleanValue("uiHasPool"),
      floors: parseInt(document.getElementById("uiFloors").value),
      cityCode: parseInt(cityCode),
      cityPartRange: parseInt(cityPartRange),
      numPrevOwners: parseInt(document.getElementById("uiNumPrevOwners").value),
      hasStormProtector: getBooleanValue("uiHasStormProtector"),
      basement: getBooleanValue("uiBasement"),
      attic: getBooleanValue("uiAttic"),
      garage: getBooleanValue("uiGarage"),
      hasStorageRoom: getBooleanValue("uiHasStorageRoom"),
      hasGuestRoom: getBooleanValue("uiHasGuestRoom"),
      HouseAge: parseInt(document.getElementById("uiHouseAge").value)
  };

  const url = "http://127.0.0.1:5000/predict_home_price";

  $.post(url, formData, function(data, status) {
      if (data.status === 'error') {
          alert("Error in prediction: " + data.error);
          return;
      }
      
      console.log(data.estimated_price);
      const estPrice = document.getElementById("uiEstimatedPrice");
      estPrice.innerHTML = "<h2>Estimated Price: €" + data.estimated_price.toLocaleString('fr-FR', {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2
      }) + "</h2>";
  }).fail(function(response) {
      alert('Error: ' + response.statusText);
  });
}

window.onload = function() {
  console.log("document loaded");
};