function showSelectedColor() {
    var select = document.getElementById("color-select");
    var selectedColor = select.options[select.selectedIndex].value;
    var colorBox = document.getElementById("color-box");
    colorBox.style.backgroundColor = "#" + selectedColor;
    colorBox.style.width = "50px";
    colorBox.style.height = "50px";
}
