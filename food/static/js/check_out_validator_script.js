let input_submit_element = document.querySelector("input[type='submit']")
let mobile_number_flag  = true
input_submit_element.disabled = true;
document.querySelector('input[name="phone_number"]').addEventListener('input',function(){mobile_number_checker()})
function mobile_number_checker() {
  let element = document.querySelectorAll('input[name="phone_number"]')[0]
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
    if (mobile_number_flag === true) {
      input_submit_element.disabled = false;
    }
    else{input_submit_element.disabled = true;}
  }
}

document.querySelector('input[name="email"]').addEventListener('input',function(){email_checker()})

function email_checker() {
  let element = document.querySelector('input[name="email"]')
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
    else if (value[0] == '@'){
      mobile_number_flag  = false
      error_box_message.innerText="ابتدای ایمیل نباید @ باشد."
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
    if (mobile_number_flag === true) {
      input_submit_element.disabled = false;
    }
    else{input_submit_element.disabled = true;}
  }
}