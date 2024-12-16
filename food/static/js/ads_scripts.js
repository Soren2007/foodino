window.addEventListener("load", ()=>{
  let p_elements_in_article = document.querySelectorAll("article p");
  console.log(p_elements_in_article);
  let i = 0
  while (((p_elements_in_article.length / 3)-2) >= i) {
    $.ajax({
      type: "POST",
      url: `/${lang}/ads/show-ads-random/`,
      data: {
        "csrfmiddlewaretoken":csrf,
      },
      success: function (res) {
        Random_Number = Math.floor(Math.random() * p_elements_in_article.length);
        const element = p_elements_in_article[Random_Number]
        element.innerHTML = element.innerHTML+res
      },
    });
    i++;
    console.log(i);
  }
})