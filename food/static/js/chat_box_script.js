const send_message_audio = new Audio("/media/sounds/send_message.mp3");
function record_sound() {
    navigator.mediaDevices.getUserMedia({audio: true,}).then(function (stream) {
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();
    const audioChunks = [];
    mediaRecorder.addEventListener("dataavailable", function (event) {audioChunks.push(evendata);})
    ;}
    );
}
function send_message(phone_number,mod) {
  // check_out_time_of_last_message()
  let radio_message_box_id = document.querySelector(".radio_message_box input[type='radio']:checked").id
  let message = document.getElementById('id_chat_message')
  let chat_box_element = document.getElementById("id_chat_box_body");
  if (message.value.length > 0) {
    console.log(radio_message_box_id);
  if (radio_message_box_id == "q_by_chat_gpt"){
    let message_parent = document.querySelector("#messages_user_and_suport_refresh");
    let user_avatar = document.querySelector("#id_user_avatar").value
    let date = new Date()
    let full_date = `${date.getFullYear()}/${date.getMonth()}/${date.getDay()}`
    let temp = message_parent.innerHTML 
    temp=temp + `
    <div class="chat-box-user-message">
        <div>
            <img src="/media/${user_avatar}">
        </div>
        <div>
            <p>${message.value}</p>
            <p class="date-time">${full_date}</p>
        </div>
    </div>`
    message_parent.innerHTML = temp
    chat_box_element.scrollTo(0, chat_box_element.scrollHeight);
    send_message_audio.play();
    $.ajax({
      type: "POST",
      url: `/${lang}/chat-gpt/open-ai-chat-gpt/`,
      data: {message: message.value,"csrfmiddlewaretoken":csrf,"phone_number":phone_number},
      success: function (res) {
        res_message = `<div class="chat-box-helper-message">
        <div>
            <p>${res}</p>
            <p class="date-time">${full_date}</p>
        </div>
        <div>
            <img src="/media/images/avatar/ai_avatar.png" alt="">
        </div>
        </div>`
        message_parent.innerHTML = temp + res_message
        chat_box_element.scrollTo(0, chat_box_element.scrollHeight);
      },
    });
    message.value = "";
  }
  else{
      $.ajax({
        type: "GET",
        url: `/${lang}/add-message/`,
        data: {message: message.value,},
        success: function (res) {
          $("#id_chat_box_body").html(res);
          send_message_audio.play();
          chat_box_element.scrollTo(0, chat_box_element.scrollHeight);
          refresh_messages(phone_number,false)
        },
      });
      message.value = "";
  }
}
}
function internet_checker() {
  let status = navigator.onLine;
  if (status == false) {
    
  }
  return status
}
function show_message(phone_number,is_manage_chat=true) {
  if (internet_checker() == true) {
    check_out_time_of_last_message()
    $.ajax({
      type: "GET",
      url: `/${lang}/show-messages/`,
      data: {
      phone_number: phone_number,
      is_manage_chat: is_manage_chat,
      "csrfmiddlewaretoken":csrf,
    },
    success: function (res) {
      if (is_manage_chat == true) {
          $("#id_chat_box_manages").html(res);
          let chat_box_element = document.getElementById(
            "id_chat_box_body_manager"
            );
            chat_box_element.scrollTo(0, chat_box_element.scrollHeight);
          }
          setTimeout(function (){refresh_messages(phone_number,is_manage_chat)}, 5000);
      },
    });
  }
}
function send_message_manager(receiver_user_phone_number) {
  if (internet_checker() == true) {
    let message = document.getElementById("id_chat_message_manager");
    let parent_id = document.getElementById("id_parent_id").value;
    if (message.value.length > 0) {
      $.ajax({
        type: "GET",
        url: "/manage-chat-room/show-messages/",
        data: {message: message.value,receiver_user_phone_number: receiver_user_phone_number,parent_id: parent_id,model: "send_message",},
      success: function (res) {
        let chat_box_element = document.getElementById("id_chat_box_body_manager");
        $("#id_chat_box_body_manager").html(res);
        chat_box_element.scrollTo(0, chat_box_element.scrollHeight);
        show_message(receiver_user_phone_number)
        send_message_audio.play();
      },
    });
    message.value = "";
    }
  }
}
function send_message_with_enter(event,receiver_user_phone_number) {
  console.log(event);
  if (event.key == "Enter"){
    send_message_manager(receiver_user_phone_number);
  }
}
function reply_message(id) {
  document.getElementById("id_parent_id").value = id;
}
function refresh_messages(phone_number,is_manage_chat=true) {
  $.ajax({
    type: "POST",
    url: `/${lang}/refresh-messages/`,
    data: {
    phone_number: phone_number,
    is_manage_chat: is_manage_chat,
    "csrfmiddlewaretoken":csrf,
  },
  success: function (res) {
    if (res != "false") {
    $("#id_chat_box_body_manager").html(res);
      
      if (is_manage_chat == true) {
        let chat_box_element = document.getElementById(
          "id_chat_box_body_manager"
          );
          chat_box_element.scrollTo(0, chat_box_element.scrollHeight);
      }
      else {
        console.log("ok");
        $("#messages_user_and_suport_refresh").html(res);
      }
    }
    },
  });
  setTimeout(function (){refresh_messages(phone_number,is_manage_chat)}, 5000);
}


function clear_chats() {
  if (internet_checker() == true) {
    $.ajax({
      type: "POST",
      url: `/${lang}/clear-chat/`,
      data: {"csrfmiddlewaretoken":csrf,},
      success: function (res) {
        window.location.reload();
      },
    });
  }
}
// check out time of last message for delete messages
function check_out_time_of_last_message() {
  const hours = new Date().getHours();
  let chat_room_start_hours = Number(sessionStorage.getItem( "chat_room_start_hours"))
  console.log(hours - Number(sessionStorage.getItem( "chat_room_start_hours")));
  console.log(chat_room_start_hours);
  if (chat_room_start_hours === Number()) {
    if (Number(sessionStorage.getItem( "chat_room_start_hours")) - hours >= 3) {
      console.log("ok");
      // clear_chats()
  }}else{sessionStorage.setItem( "chat_room_start_hours",String(hours))
  console.log("ok");}
}

window.addEventListener("load",function(){
  const chat_session_phone_number_data = document.getElementById("chat_session_phone_number").value
  const is_manage_chat_data = document.getElementById("is_manage_chat").value
  document.getElementById("id_clear_chats_btn").addEventListener("click",function(){clear_chats()})
  document.getElementById("id_refresh_chat_btn").addEventListener("click",function(){refresh_messages(chat_session_phone_number_data,is_manage_chat_data)})
  document.getElementById("id_send_message_btn").addEventListener("click",function(){send_message(chat_session_phone_number_data,is_manage_chat_data)})
  let element = document.getElementById("id_chat_message")
  if(element){element.addEventListener("keypress",function(event){if (event.key == "Enter") {send_message(chat_session_phone_number_data,is_manage_chat_data)}});}
})