// what cook
let stuff_names = ""
function add_stuff() {
  if (internet_checker() == true) {
    let stuff_input = document.getElementById("stuff_input")
    let stuff_name = stuff_input.value
    if (stuff_name !== "") {
      let parent_element_stuffs_box = document.getElementsByClassName("stuffs-box")[0]
      let new_element = document.createElement("div")
      new_element.classList.add("stuff-box-m-r")
      new_element.innerText = stuff_name
      parent_element_stuffs_box.appendChild(new_element)
      stuff_names+=`${stuff_name},`
      // cs=document.querySelector("input[name='csrfmiddlewaretoken']").value
      $.ajax({
        type: "GET",
        data: {
          "stuff_names":stuff_names,
          // "csrfmiddlewaretoken":cs
        },
        url: `/what-cook/show-recipes/`,
        success: function (res) {
          document.getElementById("id_r_f_a").innerHTML = res
        },
      });
    }
    else{
      show_alert_error("ابتدا نام ماده را وارد کنید.")
    }
  }
}