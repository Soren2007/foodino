const blog_id = document.getElementsByClassName('q-a-box')[0].id
function show_like_box(box_name){
  if (box_name == 'like') {
    document.querySelector(`.q-a-box>div:nth-child(2)>div:first-child`).setAttribute('class','show-like')
    document.querySelector(`.q-a-box>div:nth-child(3)`).style.display = "none"
    document.querySelector(`.q-a-box>div:nth-child(2)>div:last-child`).style.color = "#ff4005"
  }
  else if (box_name == 'dislike') {
    document.querySelector(`.q-a-box>div:nth-child(3)>div:first-child`).setAttribute('class','show-like')
    document.querySelector(`.q-a-box>div:nth-child(2)`).style.display = "none"
    document.querySelector(`.q-a-box>div:nth-child(3)>div:last-child`).style.color = "#ff4005"
  }
  else {
    console.log('not fulnd');
  }
}
// onclick="add_like('{{article.id}}')"
document.getElementById("add_like_for_blog").addEventListener("click",
function add_like() {
  const element = document.getElementById('blog_likes')
  console.log(blog_id);
  if (sessionStorage.getItem(`is_user_like_or_dislike_${blog_id}`) != 'true'){
    show_like_box('like')
    $.ajax({
      type: "GET",
      url: "/blog/add-like/",
      data: {'blog_id': blog_id,},
      success: function (res) {
        sessionStorage.setItem(`is_user_like_or_dislike_${blog_id}`, true);
        sessionStorage.setItem(`like_or_dislike_${blog_id}`, 'like');
        element.innerText = res
      },
    });
  }
  else{
    show_alert_warning('شما قبلا پسندیده‌اید.')
  }
}
)
document.getElementById("add_dislike_for_blog").addEventListener("click",
function add_dislike() {
  const element = document.getElementById('blog_dislikes')
  
  if (sessionStorage.getItem(`is_user_like_or_dislike_${blog_id}`) != 'true'){
    show_like_box('dislike')
    $.ajax({
      type: "GET",
      url: "/blog/add-dislike/",
      data: {'blog_id': blog_id,},
      success: function (res) {
        sessionStorage.setItem(`is_user_like_or_dislike_${blog_id}`, true);
        sessionStorage.setItem(`like_or_dislike_${blog_id}`, 'dislike');
        element.innerText = res
      },
    });
  }
  else{
    show_alert_warning('شما قبلا نپسندیده‌اید.')
  }
}
)
show_like_box(sessionStorage.getItem(`like_or_dislike_${blog_id}`))