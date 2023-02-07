document.querySelectorAll(".cell").forEach(cell => cell.addEventListener("click", function(event) {
    const input = document.getElementById("input")
    const submit = document.getElementById("submit")
    const desc = document.getElementById("desc")

    if(cell.innerText == 'X') {
        input.value = ""
        cell.style.border = "2px solid red"
        submit.classList.add("disabled")
    } else if(cell.innerText == 'O') {
        input.value = ""
        input.style.border = "2px solid red"
        submit.classList.add("disabled")
    } else {
        cell.style.border = "2px solid black"
        input.value = cell.innerText
        submit.classList.remove("disabled")
        desc.innerText = "You've chosen cell " + cell.innerText
    }
}))