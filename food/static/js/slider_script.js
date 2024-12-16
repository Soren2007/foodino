// try {
  let slides = document.getElementsByClassName("header-box");
  let dots = document.getElementsByClassName("dot");
  let width = 0 
  function show_time(dot_index_number) {
    const dot = dots[dot_index_number-2].children[0]
    width += 1
    dot.style.width = `${width}%`
    if (width == 99 || dot_index_number != slid_index_number){
      dot.style.width = '0%'
      width = 0
      clearInterval(timer_dot)
    }
  }
  let slid_index_number = 1
  function show_slid(n) {
      let i;
      if (n > slides.length) { slid_index_number = 1 }
      if (n < 1) { slid_index_number = slides.length }
      for (i = 0; i < slides.length; i++) {
        slides[i].classList.replace("show-slid","hidden-slid");
      }
      for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
      }
      slides[slid_index_number - 1].classList.replace("hidden-slid","show-slid");
      dots[slid_index_number - 1].className += " active";
      let = timer_dot = setInterval(function(){
        show_time(slid_index_number)
      }, 99)
      

  }
  function change_slid(index_number) {show_slid(slid_index_number = index_number);}
  auto() 
  // show_slid(slid_index_number)
  function auto() {
      show_slid(slid_index_number)
      setTimeout(auto, 10000);
      
      slid_index_number++
  }

// } catch (error) {
  
// }