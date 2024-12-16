function show_user_number(number) {
    const element = document.getElementById("number")
    let i=0;
    while (i <= number) {
        i++;
        element.innerText = i;
    }
}
function win_lottery(lottery_id,users_length,user_number=1) {
    document.getElementById("id_wins_lottery").innerHTML = `<div class="wins-lottery-box">
    <div><span id="user_number">1</span></div>
        <div>
            <div class="wins-lottery-circle">
                <span id="number"></span>
            </div>
        </div>
        <div class="btn" onclick="win_lottery(${lottery_id},${users_length},${user_number+1})">
        </div>
    </div>`
    if (user_number==(users_length+1)){
        document.getElementsByClassName("wins-lottery-box")[0].remove()
        $.ajax({
            type: "POST",
            url: `/${lang}/gift/wins-lottery/`,
            data: {
              "lottery_id":lottery_id,
              "is_end":"true",
              "csrfmiddlewaretoken":csrf,
            },
            success: function (res) {
            window.location.reload()
            }, 
        }); 
    }
    else{
        let number_element = document.getElementById("number")
        document.getElementById("user_number").innerText = user_number
        $.ajax({
            type: "POST",
            url: `/${lang}/gift/wins-lottery/`,
            data: {
              "lottery_id":lottery_id,
              "is_end":"false",
              "csrfmiddlewaretoken":csrf,
            },
            success: function (res) {
            show_user_number(Number(res))
            }, 
        }); 
    }
}