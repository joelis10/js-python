document.querySelectorAll(".cell").forEach(cell => cell.addEventListener("click", function(event) {
    const input = document.getElementById("input")
    const submit = document.getElementById("submit")

    if(cell.innerText == 'X') {
        input.value = ""
        submit.classList.add("disabled")
        submit.classList.add("invalid")
        submit.innerText = "Invalid move."
    } else if(cell.innerText == 'O') {
        input.value = ""
        submit.classList.add("disabled")
        submit.classList.add("invalid")
        submit.innerText = "Invalid move."
    } else {
        cell.style.border = "2px solid black"
        input.value = cell.innerText
        submit.classList.remove("disabled")
        submit.classList.remove("invalid")
        submit.classList.add("valid")
        submit.innerText = "Choose cell " + cell.innerText + " >"
    }
}))