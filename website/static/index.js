function deleteRecipe(recipeId) {
  fetch('/delete-recipe', {
    method: "POST",
    body: JSON.stringify({ recipeID: recipeId }),
  }).then((_res) => {
    window.location.href= "/";
  })
}

function favoriteRecipe(recipeId) {
  fetch('/favorite-recipe', {
    method: "POST",
    body: JSON.stringify({ recipeID: recipeId }),
  }).then((_res) => {
    window.location.href= "/";
  })
}