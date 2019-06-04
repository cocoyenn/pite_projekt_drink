var ingredientCounter = 0;

function addIngredient() {
    selectInput = document.getElementById('selectIngredient');
    ingredientList = document.getElementById('IngredientList');
    newIngredient = selectInput.options[selectInput.selectedIndex].value;

    ingredientList.innerHTML += "<input type='hidden' name='ingredientId_" + ingredientCounter + "' value='" + newIngredient + "' /><p id='ingredientId_" + ingredientCounter + "'>" + newIngredient + "<button type=\"button\" class=\"btn btn-warning\" onclick=\"removeIngredient('ingredientId_" + ingredientCounter + "')\">-</button></p>";
    ingredientCounter++;
}

Element.prototype.remove = function() {
    this.parentElement.removeChild(this);
}
NodeList.prototype.remove = HTMLCollection.prototype.remove = function() {
    for(var i = this.length - 1; i >= 0; i--) {
        if(this[i] && this[i].parentElement) {
            this[i].parentElement.removeChild(this[i]);
        }
    }
}

function removeIngredient(ingredient) {
     ingredientToRemove = document.getElementById(ingredient);
     ingredientToRemove.remove();
}

function resetIngredientList() {
    selectInput = document.getElementById('selectIngredient');
    selectInput.selectedIndex = "0";
    ingredientList = document.getElementById('IngredientList');
    ingredientList.innerHTML = "";
}