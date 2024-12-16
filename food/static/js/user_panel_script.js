// console.log(document.getElementById("change_profile_and_full_name_btn"));
document.getElementById("change_profile_and_full_name_btn").addEventListener("click",function(e){
    $.ajax({
        type: "GET",
        url: `/${lang}/accounts/change-profile-and-full-name/`,
        data: {"csrfmiddlewaretoken":csrf,},
        success: function (res) {$("#on_page_section").html(res);},
    });
})