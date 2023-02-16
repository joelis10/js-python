document.querySelectorAll(".cell").forEach(cell => cell.addEventListener("click", function(event) {
    const input = document.getElementById("input")
    const submit = document.getElementById("submit")

    if(cell.innerText == 'X') {
        input.value = ""
        submit.classList.add("disabled", "invalid")
        submit.innerText = "Invalid move."
        cell.style.backgroundColor = "red"
    } else if(cell.innerText == 'O') {
        input.value = ""
        submit.classList.add("disabled", "invalid")
        submit.innerText = "Invalid move."
        cell.style.backgroundColor = "red"
    } else {
        cell.style.border = "2px solid black"
        input.value = cell.innerText
        submit.classList.remove("disabled", "invalid")
        submit.classList.add("valid")
        submit.innerText = "Choose cell " + cell.innerText + " >"
    }
}))