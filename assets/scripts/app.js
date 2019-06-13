var ingredientCounter = 0;

function addIngredient(ingredientCategory) {
    selectInput = document.getElementById(ingredientCategory);
    ingredientList = document.getElementById('picked_' + ingredientCategory);
    newIngredient = selectInput.options[selectInput.selectedIndex].value;

    ingredientList.innerHTML += "<input type='hidden' name='ingredientId_" + ingredientCounter + "' value='" + newIngredient + "' /><p class='text-white' id='ingredientId_" + ingredientCounter + "'>" + newIngredient + "<button type=\"button\" class=\"btn btn-warning minusButton\" onclick=\"removeIngredient('ingredientId_" + ingredientCounter + "')\">-</button></p>";
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
    selectInput = document.getElementById('selectAlcoholicIngredient');
    selectInput.selectedIndex = "0";
    ingredientList = document.getElementById('picked_selectAlcoholicIngredient');
    ingredientList.innerHTML = "";

    selectInput = document.getElementById('selectNonAlcoholicIngredient');
    selectInput.selectedIndex = "0";
    ingredientList = document.getElementById('picked_selectNonAlcoholicIngredient');
    ingredientList.innerHTML = "";

    selectInput = document.getElementById('selectFruitIngredient');
    selectInput.selectedIndex = "0";
    ingredientList = document.getElementById('picked_selectFruitIngredient');
    ingredientList.innerHTML = "";

    selectInput = document.getElementById('selectOtherIngredient');
    selectInput.selectedIndex = "0";
    ingredientList = document.getElementById('picked_selectOtherIngredient');
    ingredientList.innerHTML = "";

    selectInput = document.getElementById('selectGlassIngredient');
    selectInput.selectedIndex = "0";
    ingredientList = document.getElementById('picked_selectGlassIngredient');
    ingredientList.innerHTML = "";
}