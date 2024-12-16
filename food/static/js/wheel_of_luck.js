let spin = document.querySelector(".wheel-spin");
let click_number = 0
spin.addEventListener("click", () => {
    let wheel = document.querySelector(".wheel");
    if (click_number === 0) {
        // click_number++  
    $.ajax({
        type: "POST",
        url: `/${lang}/gift/get-gift-in-wheel-of-luck/`,
        data: {
            "csrfmiddlewaretoken" : csrf,
            "wheel_of_luck_id" : document.querySelector(".wheel-main-div").id,
        },
        success: function (res) {
            if (res=="Error") {
                show_alert_warning("شما ابتدا باید وارد شوید")
            }
            wheel.style.transform = `rotate(${res}deg)` 
        },
    });
    }
    // sessionStorage.setItem('is_', 'dislike');
}) 