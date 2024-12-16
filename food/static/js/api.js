
// const xhr = new XMLHttpRequest();
// xhr.open("GET","http://ip-api.com/json/");
// xhr.responseType = "json"
// xhr.onreadystatechange = function(e) {
//     if (this.status === 200 && this.readyState == this.DONE){
//         thisElement.remove();
//         const table = document.querySelector(".check-ip-wrapper table");
//         table.classList.toggle('ds-none');
//         const data = this.response;
//         const countryData = [data.query , data.country , `<img id="country-flag" src=>` , data.countryCode.toLowerCase() , data.regionName , data.city , data.as]
//         data.countryCode.toLowerCase()
//         $.ajax({
//             type: "GET",
//             url: 'language/set-language/',
//             data: {
//               "countryCode":data.countryCode.toLowerCase(),
//               "flag":`https://flagicons.lipis.dev/flags/4x3/${data.countryCode.toLowerCase()}.svg`
//             },
//             success: function (res) {
//               window.location.reload()
//             },
//         });
//     }
//     else if(this.status < 200 && this.readyState == this.DONE){
//         show_alert_error('Error Ip')
//     }
// }