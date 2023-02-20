const input = document.getElementById("input")
const submit = document.getElementById("submit")
const boardCell = document.querySelectorAll(".cell")
const form = document.querySelector("form")

window.onload = function() {
    for(var i = 0; boardCell.length; i++) {
        if(boardCell[i].innerText == "X") {
            boardCell[i].style.backgroundColor = "red"
            boardCell[i].style.color = "white"
        }

        if(boardCell[i].innerText == "O") {
            boardCell[i].style.backgroundColor = "blue"
            boardCell[i].style.color = "white"
        }
    }
}


boardCell.forEach(cell => cell.addEventListener("click", function() {
    if(cell.innerText == 'X') {
        input.value = ""
        submit.classList.add("disabled", "invalid")
        submit.innerText = "Invalid move."
    } else if(cell.innerText == 'O') {
        input.value = ""
        submit.classList.add("disabled", "invalid")
        submit.innerText = "Invalid move."
    } else {
        cell.style.border = "2px solid black"
        input.value = cell.innerText
        submit.classList.remove("disabled", "invalid")
        submit.classList.add("valid")
        submit.innerText = "Choose cell " + cell.innerText + " >"
    }
}))
