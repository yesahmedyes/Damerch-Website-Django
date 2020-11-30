let slider = document.getElementById("myRange");
let output = document.getElementById("range");
output.innerHTML = " ";

slider.oninput = function() {
    if (this.value == 0) {
        output.innerHTML = " ";
    }
    else if (this.value == 1) {
        output.innerHTML = this.value + " - 99";
    }
    else if (this.value > 1 && this.value <= 10) {
        output.innerHTML = (((parseInt(this.value) - 1) *100)-1) + " - " + (((parseInt(this.value) - 1) *100)  + 100);
    }
    else if (this.value > 10 && this.value < 20) {
        output.innerHTML = (((parseInt(this.value) - 10) *1000)-1) + " - " + (((parseInt(this.value) - 10) *1000)  + 1000);
    }
    else if (this.value >= 20 && this.value < 29) {
        output.innerHTML = (((parseInt(this.value) - 19) * 10000)-1) + " - " + (((parseInt(this.value) - 19) * 10000)  + 10000);
    }
}

