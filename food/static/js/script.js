// ------------------------------------------------------------------------------
// programmer : soren shamlou
// site name : foodino
// file name : script.js
// file type : javascript
// date: 2023/4/6
// update: 2023/6/1

// ------------------------------------------------------------------------------
let csrf = document.querySelector("input[name='csrfmiddlewaretoken']").value
let lang = document.querySelector("html").lang
const date = new Date();
const success_audio = new Audio("http://127.0.0.1:8000/media/sounds/short-success-sound.mp3");
let shake_event = new Shake()
shake_event.start();
window.addEventListener("shake",function () {let xhttp  = new XMLHttpRequest();xhttp.open("GET", "/carts/",)})
try {if (document.getElementById("id_show_chat_box_btn")){document.getElementById("id_event_box").style = "bottom:125px"}} catch (error) {console.log(error);}
// night display
// if (date.getHours() > 22 || date.getHours() > 0)
  // document.querySelector("*").classList.add("night");
document.getElementById("id_copy_right_date").innerText = date.getFullYear();
// night display
// internet checker
function internet_checker() {
  let status = navigator.onLine
  if(status == false){
    document.getElementById("id_message_div").innerHTML = `
    <div class="alert alert-error" id="alert_id_1">
    <i class="fa fa-times s-times" onclick="delete_element('alert_id_1')"></i>
    <div>
    <img src="/media/images/alerts/error.svg">
    <span>کاربر گرامی لطفا اینترنت خود را چک کنید.</<span>
    </div>
    </div>
    `
    document.body.scrollTo(0,0);
  }
  return status;
}
internet_checker()
// internet checker
// back to to btn
document.getElementById("id_goto_up_btn").addEventListener("click", function () {window.scrollTo(0, 0);});
// back to to btn
// orders app:
status_of_carts();
function status_of_carts() {
  if (internet_checker() == true) {
    $.ajax({
      type: "POST", 
      url: `/${lang}/orders/status-of-carts/`,
      data:{"csrfmiddlewaretoken":csrf,},
      success: function (res) {
        $("#id_indicator-value").text(res);
      },
    });
  }
}
function show_alert_success(message) {
  jQuery.getScript('https://unpkg.com/sweetalert/dist/sweetalert.min.js', function() {            
    success_audio.play()
    swal({
          title: "عملیات موفقیت آمیز",
          text: message,
          icon: "success",
          timer: 10000,
          button: "باشه",
        })
        .then((willSubmit) => {
          if (!willSubmit) {
              return false;
          }
      });
    });
}
function show_alert_warning(message) {
  jQuery.getScript('https://unpkg.com/sweetalert/dist/sweetalert.min.js', function() {            
    swal({
      title: "توجه",
      text: message,
      icon: "warning",
      timer: 10000,
      button: "باشه",
    })
    .then((willSubmit) => {
      if (!willSubmit) {
        return false;
      }
    });
  });
}
function show_alert_error(message) {
  jQuery.getScript('https://unpkg.com/sweetalert/dist/sweetalert.min.js', function() {            
    swal({
          title: "خطا در انجام عملیات",
          text: message,
          icon: "error",
          timer: 10000,
          button: "باشه",
        })
        .then((willSubmit) => {
          if (!willSubmit) {
              return false;
          }
      });
    });
}
function show_how_to_use() {
  alert("ok")
  $.ajax({
    type: "POST",
    url: `/${lang}/orders/show-how-to-use/`,
    data: {"csrfmiddlewaretoken":csrf,},
    success: function (res) {$("#on_page_section").html(res);alert(res)},
  });
}


function add_to_food_cart(food_id, qty, last_qty = NaN) {
  if (internet_checker() == true) {
    if (Number(last_qty) <= 1 && Number(qty) == -1) {delete_form_food_cart(food_id);} 
    else {
      if (qty == "input") {qty = document.getElementById("qty-input-" + food_id).value;}
      if (Number(qty) >= 0) {
        $.ajax({
          type: "POST",
          url: `/${lang}/orders/show-how-to-use/`,
          data: {"csrfmiddlewaretoken":csrf,},
          success: function (res) {
            $("#on_page_section").html(res);
            document.getElementById("add_to_cart").addEventListener("click", function () {
              let how_to_use = document.querySelector("#id_how_to_use option:checked").value
              document.getElementsByClassName("on-page")[0].remove()
              $.ajax({
                type: "POST",
                url: `/${lang}/orders/add-to-food-cart/`,
                data: {food_id: food_id,qty: qty,"how_to_use":how_to_use,"csrfmiddlewaretoken":csrf,},
                success: function (res) {$("#food_cart_list").html(res);status_of_carts();format_price()
                  show_alert_success("غذای مورد نظر به سبد خرید اضافه شد.")
                },
              });
            })
          },
        });
      }else{
        $.ajax({
          type: "POST",
          url: `/${lang}/orders/add-to-food-cart/`,
          data: {food_id: food_id,qty: qty,"csrfmiddlewaretoken":csrf,},
          success: function (res) {$("#food_cart_list").html(res);status_of_carts();format_price()
            show_alert_success("غذای مورد نظر به سبد خرید اضافه شد.")
          },
        });
      }
    }
  }
}

function add_to_my_recipe_cart(my_recipe_id, qty, last_qty = NaN) {
  if (internet_checker() == true) {
    if (Number(last_qty) <= 1 && Number(qty) == -1) {delete_form_my_recipe_cart(my_recipe_id);} 
    else {
      if (qty == "input") {qty = document.getElementById("qty-input-" + my_recipe_id).value;}
      if (Number(qty) >= 0) {
        $.ajax({
          type: "POST",
          url: `/${lang}/orders/show-how-to-use/`,
          data: {"csrfmiddlewaretoken":csrf,},
          success: function (res) {
            $("#on_page_section").html(res);
            document.getElementById("add_to_cart").addEventListener("click", function () {
              let how_to_use = document.querySelector("#id_how_to_use option:checked").value
              document.getElementsByClassName("on-page")[0].remove()
              $.ajax({
                type: "POST",
                url: `/${lang}/orders/add-to-my-recipe-cart/`,
                data: {my_recipe_id: my_recipe_id,qty: qty,"csrfmiddlewaretoken":csrf,},
                success: function (res) {$("#food_cart_list").html(res);status_of_carts();format_price();show_alert_success("دستور غذایی مورد نظر به سبد خرید اضافه شد.")
              },
              });
            })
          },
        });
      }
      else {
        $.ajax({
          type: "POST",
          url: `/${lang}/orders/add-to-my-recipe-cart/`,
          data: {my_recipe_id: my_recipe_id,qty: qty,"csrfmiddlewaretoken":csrf,},
          success: function (res) {$("#food_cart_list").html(res);status_of_carts();format_price();show_alert_success("دستور غذایی مورد نظر از سبد خرید حذف شد.")
        },
        });
      }
    }
  }
}


function update_from_food_cart(food_id, last_qty = NaN) {
  if (internet_checker() == true) {
    let qty = document.getElementById("qty-input-" + food_id).value;
    if (Number(last_qty) <= 0 || qty <= 0) {delete_form_food_cart(food_id);} 
    else{
      $.ajax({
        type: "POST",
        url: `/${lang}/orders/update-from-food-cart/`,
        data: {food_id: food_id,qty: qty,"csrfmiddlewaretoken":csrf,},
        success: function (res) {$("#food_cart_list").html(res);status_of_carts();format_price();show_alert_success("سبد خرید شما با موفقیت بروز رسانی شد.")},
      });
    }
  }
}

function update_from_my_recipe_cart(my_recipe_id, last_qty = NaN) {
  if (internet_checker() == true) {
    let qty = document.getElementById("qty-input-" + my_recipe_id).value;
    if (Number(last_qty) <= 0 || qty <= 0) {delete_form_food_cart(my_recipe_id);} 
    else{
      $.ajax({
        type: "POST",
        url: `/${lang}/orders/update-from-my-recipe-cart/`,
        data: {my_recipe_id: my_recipe_id,qty: qty,"csrfmiddlewaretoken":csrf,},
        success: function (res) {$("#food_cart_list").html(res);status_of_carts();format_price()},
      });
    }
  }
}

function delete_form_food_cart(food_id) {
  if (internet_checker() == true) {
    $.ajax({
      type: "POST",
      url: `/${lang}/orders/delete-form-food-cart/`,
      data: {food_id: food_id,"csrfmiddlewaretoken":csrf,},
      success: function (res) {$("#food_cart_list").html(res);status_of_carts();format_price()},
    });
  }
}

function delete_form_my_recipe_cart(my_recipe_id) {
  if (internet_checker() == true) {
    $.ajax({
      type: "POST",
      url: `/${lang}/orders/delete-form-my-recipe-cart/`,
      data: {my_recipe_id: my_recipe_id,"csrfmiddlewaretoken":csrf,},
      success: function (res) {$("#food_cart_list").html(res);status_of_carts();format_price()},
    });
  }
}
  function apply_coupon(order_id) {
    if (internet_checker() == true) {
      let coupon_code = document.getElementById("id_discount").value;
      $.ajax({
      type: "POST",
      url: `/${lang}/orders/apply-coupon/`,
      data: {
        order_id: order_id,
        coupon_code: coupon_code,
        "csrfmiddlewaretoken":csrf,
      },
      success: function (res) {window.location.reload();},
    });
  }
}
function count_qty(m,food_id) {
  let input = document.getElementById('qty-input-'+food_id);
  let = new_value = Number(input.value);
  if (m=='add') {new_value++;}
  else{new_value--;}
  input.value = new_value;
}
function show_cities_with_country() {
  $.ajax({
    url: `/${lang}/orders/show-cities-with-country/`,
    type: "POST",
    data: {
      "country_id":document.querySelector("option:checked").value,
      "csrfmiddlewaretoken":csrf,
    },
    success: function (res) {
      document.getElementById("city_id_options").innerHTML = res
    },
  });
}
function change_status_order(order_id) {
  $.ajax({
    type: "POST",
    url: `/${lang}/orders/change-status-order/`,
    data: {
      "order_id":order_id,
      "status_id":document.querySelector(`#status_${order_id} option:checked`).value,
      "csrfmiddlewaretoken":csrf,
    },
    success: function (res) {
      alert(res);
    },
  });
}

function find_branch() {
  $.ajax({
    type: "POST",
    url: `/${lang}/orders/find-branch/`,
    data: {
      "city_id":document.querySelector("#id_city option:checked").value,
      "csrfmiddlewaretoken":csrf,
    },
    success: function (res) {
      $("#branch_id_options").html(res);
    },
  });
}
// orders app:
  // comment app
function show_comment_form(food_id, comment_id, food_slug,model) {
  if (internet_checker() == true) {
    $.ajax({
      type: "GET",
      url: `/${lang}/comments/create-comment/` + food_slug + "/" + model,
      data: {food_id: food_id,comment_id: comment_id,"csrfmiddlewaretoken":csrf,},
      success: function (res) {
        $("#btn_reply_" + comment_id).hide();
        $("#comment_form_" + comment_id).html(res);
      },
    });
  }
}
  // comment app
// favorite app:

status_of_favorite()
function status_of_favorite() {
  if (internet_checker() == true) {
    try {
      $.ajax({
        type: "POST",
        url: `/${lang}/favorites/status-of-favorite/`,
        data: {
          "csrfmiddlewaretoken":csrf,
        },
        success: function (res) {
          $("#id_favorites_value").text(res);
        },
      });
    }
    catch (e) {
      
    }
  }
}

function add_to_favorite(food_id) {
  if (internet_checker() == true) {
    $.ajax({
      type: "POST",
      url: `/${lang}/favorites/add-to-favorite/`,
      data: {
        food_id: food_id,
        "csrfmiddlewaretoken":csrf,
      },
      success: function (res) {
        status_of_favorite();
        if (res == "این غذا قبلا در لیست غلایق شما قرار گرفته است.") {
          show_alert_warning(res);
        }
        else{
          show_alert_success(res);
          window.location.reload();
        }
      },
    });
  }
}
function delete_to_favorite(food_id) {
  if (internet_checker() == true) {
    $.ajax({
      type: "POST",
      url: `/${lang}/favorites/delete-to-favorite/`,
      data: {
        food_id: food_id,
        "csrfmiddlewaretoken":csrf,
      },
      success: function (res) {
        status_of_favorite();
        show_alert_success(res);
        window.location.reload();
      },
    });
  }
}

function add_to_favorite_blog(blog_id) {
  if (internet_checker() == true) {
    $.ajax({
      type: "POST",
      url: `/${lang}/favorites/add-to-favorite-blog/`,
      data: {
        blog_id: blog_id,
        "csrfmiddlewaretoken":csrf,
      },
      success: function (res) {
        status_of_favorite();
        if (res == "این غذا قبلا در لیست غلایق شما قرار گرفته است.") {
          show_alert_warning(res);
        }
        else{
          show_alert_success(res);
        }
      },
    });
  }
}
function delete_to_favorite_blog(blog_id) {
  if (internet_checker() == true) {
    $.ajax({
      type: "POST",
      url: `/${lang}/favorites/delete-to-favorite-blog/`,
      data: {
        blog_id: blog_id,
        "csrfmiddlewaretoken":csrf,
      },
      success: function (res) {
        status_of_favorite();
        show_alert_success(res);
        window.location.reload();
      },
    });
  }
}












function download_blog(file_name) {
  if (internet_checker() == true) {
    $.ajax({
      type: "GET",
      url: "/blog/download-blog/",
      data: {
        file_name: file_name,
      },
      success: function (res) {
        status_of_favorite();
        show_alert_success(res);
        window.location.reload();
      },
    });
  }
}
// favorite app:
// chat box
if (document.getElementById('id_show_chat_box_btn')){
  let element = document.getElementsByClassName("chat-box")[0];
  element.classList.add("hidden");
  element.classList.replace("opacity-0", "opacity-1");
  document.getElementById("id_show_chat_box_btn").addEventListener("click", function () {
  element.classList.replace("hidden", "show");});
  document.getElementsByClassName("chat-box-close")[0].addEventListener("click", function () {
  element.classList.replace("show", "hidden");
  });
}
// chat box
function show_part(part_name,food_slug,btn_number) {
  btn_status = [false,false,false]
  btn_ids = ['id_show_food_info_btn','id_show_food_stuff_form','id_show_food_comments']
  if (part_name == "show_info_food") {
    if (internet_checker() == true) {
      $.ajax({
        type: "GET",
        url: `/${lang}/food/show-food-part/`,
        data: {
          "food_slug":food_slug,
          "slid_name":part_name,
          "csrfmiddlewaretoken":csrf,
        },
        success: function (res) {
          $("#food_menu_slider").html(res);
          document.getElementById(btn_ids[btn_number]).classList.add('btn-model-2-active')
          btn_status[btn_number] = true;
        },
      });
    }
  }
  else if(part_name == "show_food_stuff_form") {
    if (internet_checker() == true) {
      $.ajax({
        type: "GET",
        url: `/${lang}/food/show-food-part/`,
        data: {
          "food_slug":food_slug,
          "slid_name":part_name,
          "csrfmiddlewaretoken":csrf,
        },
        success: function (res) {
          $("#food_menu_slider").html(res);
          document.getElementById(btn_ids[btn_number]).classList.add('btn-model-2-active')
          btn_status[btn_number] = true;
        },
      });
    }
  }
  else if(part_name == "show_food_comments") {
    if (internet_checker() == true) {
      $.ajax({
        type: "GET",
        url: `/${lang}/food/show-food-part/`,
        data: {
          "food_slug":food_slug,
          "slid_name":part_name,
          "csrfmiddlewaretoken":csrf,
        },
        success: function (res) {
          $("#food_menu_slider").html(res);
          document.getElementById(btn_ids[btn_number]).classList.add('btn-model-2-active')
          btn_status[btn_number] = true;
        },
      });
    }
  }
  else {document.getElementById('food_menu_slider').innerText = "Error";show_alert_error('این قسمت پیدا نشد')}
  for (let index = 0; index < btn_status.length; index++) {
    let element = btn_status[index];
    if (element == false){
      document.getElementById(btn_ids[index]).classList.remove('btn-model-2-active')
    }
  }
}

// prices
function format_price() {
  let prices  = document.querySelectorAll(".price")
  prices.forEach(price => {
  price.innerText = price.innerText.replace(/\B(?=(\d{3})+(?!\d))/g, ",")
  });
}
format_price()
// prices
// id_message_div
function delete_element(element_id) {
  let parent = document.getElementById('id_message_div')
  parent.removeChild(document.getElementById(element_id))
}
// let stuff_ids = ""
//     document.querySelectorAll(".set-stuff-food:checked").forEach(stuff => stuff_ids += `${stuff.id}`)
//     $.ajax({
// my r
function add_my_recipes(food_id) {
  if (internet_checker() == true) {
    let stuff_ids = ""
    document.querySelectorAll(".set-stuff-food:checked").forEach(stuff => stuff_ids += `${stuff.id},`)
    let recipe_name = prompt("نام دستور خود را وارد کنید.")
    while (recipe_name.length <= 0){
      recipe_name = prompt("نام دستور خود را وارد کنید.")
    }
    $.ajax({
      type: "POST",
      url: `/${lang}/food/add-to-my-recipes/`,
      data: {
        "stuff_ids":stuff_ids,
        "food_id":food_id,
        "recipe_name":recipe_name,
        "csrfmiddlewaretoken":csrf,
      },
      success: function (res) {
        show_alert_success(res)
      },
    });
  }
}
function update_my_recipe(food_id,recipe_id,recipe_name) {
  if (internet_checker() == true) {
    let stuff_ids = ""
    document.querySelectorAll(".set-stuff-food:checked").forEach(stuff => stuff_ids += `${stuff.id},`)
    $.ajax({
      type: "POST",
      url: `/${lang}/food/update-my-recipe/`,
      data: {
        "stuff_ids":stuff_ids,
        "food_id":food_id,
        "recipe_id":recipe_id,
        "recipe_name":recipe_name,
        "csrfmiddlewaretoken":csrf,
      },
      success: function (res) {
        show_alert_success(res)
        window.location.reload()
      },
    });
  }
}
function delete_my_recipe(food_id,recipe_id,recipe_name) {
  if (internet_checker() == true) {
    $.ajax({
      type: "POST",
      url: `/${lang}/food/delete-my-recipe/`,
      data: {
        "food_id":food_id,
        "recipe_id":recipe_id,
        "recipe_name":recipe_name,
        "csrfmiddlewaretoken":csrf,
      },
      success: function (res) {
        show_alert_success("دستور مورد نظر شما حذف شد.");
        window.open("/food/show-my-recipes/","_self");
      },
    });
  }
}
// my r
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
      $.ajax({
        type: "POST",
        url: `/${lang}/what-cook/show-recipes/`,
        data: {
          "stuff_names":stuff_names,
          "csrfmiddlewaretoken":csrf,
        },
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
// what cook
// add user from chat room
function add_user_from_chat_room() {
  $.ajax({
    type: "POST",
    url: `/${lang}/start-chat-online/`,
    data: {
      "csrfmiddlewaretoken":csrf,
      "full_name":document.getElementById("id_chat_room_full_name").value,
      "phone_number":document.getElementById("id_chat_room_phone_number").value,
      "avatar":document.querySelector(".radio-input:checked").value,
    },
    success: function (res) {
      window.location.reload()
    },
  });
}


// add user from chat room
let event_flag = true
function replace_event_show_to_hidden(event_id,base_class) {
  if (event_flag == true) {document.getElementById(event_id).classList.replace(`show_${base_class}`, `hidden_${base_class}`);
  event_flag == false
  if (base_class=="footer_event_box") {change_footer_buttons(false)};
}
  else{document.getElementById(event_id).classList.replace(`hidden_${base_class}`, `show_${base_class}`);event_flag == true}
}
// copy text
function copy_text(text) {navigator.clipboard.writeText(text);show_alert_success("کپی شد.")}
// copy text
function change_footer_buttons(flag) {
  try {
    if (document.getElementById("id_footer_event_box")) {
      if (flag == true) {   
        document.getElementsByClassName("back-to-top")[0].style = "bottom:50px"
        document.getElementsByClassName('event-box')[0].style = "bottom:120px"
        document.getElementById("id_show_chat_box_btn").style = "bottom:50px"
      }
      else{
        document.getElementsByClassName("back-to-top")[0].style = "bottom:5px !important"
        document.getElementsByClassName('event-box')[0].style = "bottom:70px !important"
        document.getElementById("id_show_chat_box_btn").style = "bottom:5px !important"
      }
    }
  } catch (error) {}
}
change_footer_buttons(true)
  let flag_top_event = true
  try {
    if (flag_top_event == true){
    let element_days=document.getElementById("days")
    if (element_days) {

    let element_hours= document.getElementById("hours")
    let element_minutes=document.getElementById("minutes")
    let element_seconds=document.getElementById("seconds")
    function countdownTimer() {
      let end_date = document.getElementById("event_end_date_input").value
      let difference = +new Date(end_date) - +new Date();
      if (difference > 0) {
        let days= Math.floor(difference/(1000*60*60*24));
        let hours= Math.floor((difference/(1000*60*60))%24);
        let minutes= Math.floor((difference/1000/60)%60);
        let seconds= Math.floor((difference/1000)%60);
        element_days.innerText = days
        element_hours.innerText = hours
        element_minutes.innerText = minutes
        element_seconds.innerText = seconds
        
  }
  else {
    flag_top_event = false
    document.getElementsByClassName('top_menu_event_link')[0].remove()
  }
  }
}
setInterval(countdownTimer, 1000);
}
}catch (error) {}


function show_(message) {
  Notification.requestPermission()
  .then(function show_notification(){
    const my_notification = new Notification(
      "Foodino",{body:message,icon:'/media/images/logo.png'}
    )
  })
}

function show_battery_level() {
  navigator.getBattery()
  .then(function battery(battery){
    const level =  battery.level * 100
    if(level<20){
      show_alert_warning("Your Battery Level is: "+level+"%")
    }
  })
}
setInterval(() => {
  show_battery_level()
}, 120000);


// window.addEventListener("load", function (event){
//   let elements = document.getElementsByClassName("box-model-1")
//   for (let index = 0; index < elements.length; index++) {
//     elements[index].classList.add("show_cart")
//   }
// })


// function translate(text) {
//   try {
//     let url = `https://api.dictionaryapi.dev/api/v2/entries/en/${word.value.toLowerCase()}`;
//     const res = await fetch(url);
//     const data = await res.json();
//     displayData(data);
//   } catch (error) {
//     console.log(error);
//   }
// }