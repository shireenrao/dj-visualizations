// console.log("hello world")

const reportBtn = document.getElementById("report-btn")
const img = document.getElementById("img")
const modelBody = document.getElementById("modal-body")

// console.log(reportBtn)
// console.log(img)

if (img) {
    reportBtn.classList.remove("not-visible")
}

reportBtn.addEventListener('click', () => {
    console.log("clicked")
    img.setAttribute("class", "w-100")
    modelBody.prepend(img)
})
