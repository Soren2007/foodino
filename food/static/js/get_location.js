window.addEventListener("load",()=>{
  let lang = document.querySelector("html").lang
// let csrf = document.querySelector("input[name='csrfmiddlewaretoken']").value
navigator.geolocation.getCurrentPosition(save_location)
function save_location(data) {
    let latitude = data.coords.latitude // عرض
    let longitude = data.coords.longitude // طول
    console.log(latitude);
    console.log(longitude);
    $.ajax({
        type: "POST",
        url: `/${lang}/accounts/save-location/`,
        data: {
          "latitude_location":latitude,
          "longitude_location":longitude,
          "csrfmiddlewaretoken":csrf,
        }
    });
} 
})