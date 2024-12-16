try {
    let images = document.querySelectorAll(".show-image-class-default");
    for (let index = 0; index < images.length; index++) {
        let show_image_flag = false
        images[index].addEventListener('click',function(){
            if (show_image_flag == false){
                this.classList.add('show-image-class-on-page')
                show_image_flag = true
            }
            else{
                this.classList.remove('show-image-class-on-page')
                show_image_flag = false
            }
        })
        
    }
} catch (error) {
    console.log(error);
}
// document.body.classList