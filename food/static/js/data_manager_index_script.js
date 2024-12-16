function show_years_with_chart_title() {
    $.ajax({
      type: "GET",
      data: {
        "chart_title":document.querySelector("#chart_title option:checked").value,
      },
      url: `/data-manager/show-years-with-chart-title/`,
      success: function (res) {
        document.getElementById("div_year").innerHTML = res
      },
    });
  }
  function show_months_with_year() {
    $.ajax({
      type: "GET",
      data: {
        "chart_title":document.querySelector("#chart_title option:checked").value,
        "year":document.querySelector("#year option:checked").value,
      },
      url: `/data-manager/show-months-with-year/`,
      success: function (res) {
        document.getElementById("div_month").innerHTML = res
      },
    });
  }
  function show_days_with_month() {
    $.ajax({
      type: "GET",
      data: {
        "chart_title":document.querySelector("#chart_title option:checked").value,
        "year":document.querySelector("#year option:checked").value,
        "month":document.querySelector("#month option:checked").value,
      },
      url: `/data-manager/show-days-with-month/`,
      success: function (res) {
        document.getElementById("div_day").innerHTML = res
      },
    });
  }
  let show_chart_number = 0
  function show_chart() {
    let image_chart = document.getElementById("div_plote")
    let year = document.querySelector("#year option:checked").value
    let month=document.querySelector("#month option:checked").value
    let day = document.querySelector("#day option:checked").value
    let chart_model = document.querySelector("#chart_model option:checked").value
    let chart_title = document.querySelector("#chart_title option:checked").value
    if (year=="none" || month=="none" || day=="none" || chart_model=="none" || chart_title=="none"){
      document.getElementById("id_message_div").innerHTML = `
      <div class="alert alert-error" id="alert_id_1">
      <i class="fa fa-times s-times" onclick="delete_element('alert_id_1')"></i>
      <div>
      <img src="/media/images/alerts/error.svg">
      <span>لطفا اطلاعات را تکمیل کنید.</<span>
      </div>
      </div>
      `
    }
    else{
      $.ajax({
          type: "GET",
          data: {
            "year":year,
            "month":month,
            "day":day,
            "chart_title":chart_title,
            "chart_model":chart_model,
            "color":document.getElementById("color").value,
            "color_dot":document.getElementById("color_dot").value,
            "show_chart_number":show_chart_number,
      },
      url: `/data-manager/show-plot/`,
      success: function (res) {
        image_chart.innerHTML = res
        show_chart_number++;
      },
    });
  }
}

function language_with_lang_code(params) {
  $.ajax({
      type: "POST",
      url: `/${lang}/data-manager/language-with-lang-code/`,
      data: {
        "csrfmiddlewaretoken":csrf,
        "language_code":document.querySelector("#id_language option:checked").value
        
  },
  success: function (res) {
    document.getElementById("id_message_div").innerHTML = `
      <div class="alert alert-success" id="alert_id_1">
      <i class="fa fa-times s-times" onclick="delete_element('alert_id_1')"></i>
      <div>
      <img src="/media/images/alerts/success.svg">
      <span>${res}</<span>
      </div>
      </div>
      `
  },
  });
} 