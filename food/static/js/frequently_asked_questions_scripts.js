

let elements = document.getElementsByClassName('frequently-asked-question')
for (const element of elements) {
    let flag = false
    element.addEventListener("click", function(event){
        // this.classList.replace("","")
        if (flag == false){
            this.children[1].classList.replace("frequently-asked-question-response-hidden","frequently-asked-question-response-show")
            this.children[0].children[0].children[0].classList.replace("fa-angle-left","fa-angle-down")
            flag = true
        }
        else{
            this.children[1].classList.replace("frequently-asked-question-response-show","frequently-asked-question-response-hidden")
            this.children[0].children[0].children[0].classList.replace("fa-angle-down","fa-angle-left")
            flag = false
        }
    })
}
