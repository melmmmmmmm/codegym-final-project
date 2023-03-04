const colorOptions = document.getElementById("color-options");
const cardContainer = document.getElementById("card-container");

colorOptions.addEventListener("change", async (event) => {
    const selectedColor = event.target.value;
    const matchingColors = await getMatchingColors(selectedColor);
    const cardsHTML = matchingColors.map((color) => `<div class="card" style="background-color: ${color}"></div>`).join("");
    cardContainer.innerHTML = cardsHTML;
});

async function getMatchingColors(selectedColor) {
    const response = await fetch("/get_matching_colors", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ selectedColor }),
    });
    const matchingColors = await response.json();
    return matchingColors;
}
