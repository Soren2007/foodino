function show_password(input_id) {
  let input = document.getElementById(input_id)
  let icon = document.getElementById(`icon_eye_${input_id}`)
  if (input.type == "password"){
    input.type = "text"
    icon.classList.replace("fa-eye", "fa-eye-slash")
  }
  else{
    icon.classList.replace("fa-eye-slash","fa-eye")
    input.type = "password"
  }
}
// validator
// accent forms
let input_submit_element = document.querySelector("input[type='submit']")
let mobile_number_flag  = true
let password_flag  = true
input_submit_element.disabled = true;
document.querySelectorAll('input[name="mobile_number"]')[0].addEventListener('input',function(){mobile_number_checker()})
function mobile_number_checker() {
  let element = document.querySelectorAll('input[name="mobile_number"]')[0]
  let value = element.value
  let label_element = document.querySelector(`label[for="${element.id}"]`)
  let error_box_message = document.querySelector(`div[error_address='${element.id}']+ul li`)
  if (value.length<=11 || value.length>=11) {
    label_element.classList.add('error-label')
    label_element.classList.replace('correct-label','error-label')
    element.classList.add('no-valid');
    error_box_message.classList.replace('hidden','show')
    if (value.length == 0){
      mobile_number_flag  = false
      error_box_message.innerText="این فیلد نباید خالی باشد."
      input_submit_element.disabled = true;
    }
    else if (value[0] !== '0'){
      mobile_number_flag  = false
      error_box_message.innerText="ابتدای شماره موبایل باید صفر باشد."
      navigator.vibrate([100, 200,100]);
      input_submit_element.disabled = true;
    }
    else if (value.length <= 10 || value.length > 11){
      mobile_number_flag  = false
      error_box_message.innerText="شماره موبایل نادرست است."
      navigator.vibrate([100, 200,100]);
      input_submit_element.disabled = true;
    }
    else{
      mobile_number_flag =true
    }
    if(mobile_number_flag === true){
      label_element.classList.replace('error-label','correct-label')
      element.classList.replace('no-valid','valid')
      error_box_message.classList.replace('show','hidden')
    }
    if (password_flag === true && mobile_number_flag === true) {
      input_submit_element.disabled = false;
    }
    else{input_submit_element.disabled = true;}
  }
}
document.querySelector('input[name="password"]').addEventListener('input',function(){password_checker()})
function password_checker() {
  let element = document.querySelector('input[name="password"]')
  let value = element.value
  let label_element = document.querySelector(`label[for="${element.id}"]`)
  let error_box_message = document.querySelector(`div[error_address='${element.id}']+ul li`)
  if (value.length<=8 || value.length >= 16) {
    label_element.classList.add('error-label')
    label_element.classList.replace('correct-label','error-label')
    element.classList.add('no-valid');
    error_box_message.classList.replace('hidden','show')
    if (value.length == 0){
      password_flag = false
      error_box_message.innerText="این فیلد نباید خالی باشد."
      navigator.vibrate([100, 200,100]);
    }
    else if (value.length <= 7 || value.length > 16){
      password_flag  = false
      error_box_message.innerText="رمز عبور باید 8 الا 16 کارکتر باشد."
      navigator.vibrate([100, 200,100]);
    }
    else{
      password_flag =true
    }
    if(password_flag === true){
      label_element.classList.replace('error-label','correct-label')
      element.classList.replace('no-valid','valid')
      error_box_message.classList.replace('show','hidden')
    }
  }
  if (password_flag === true && mobile_number_flag === true) {
    input_submit_element.disabled = false;
  }
  else{input_submit_element.disabled = true;}
}
  // accent forms
  // validator
// mobile_number_checker()
// password_checker()