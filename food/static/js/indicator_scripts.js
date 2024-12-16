$(document).ready(()=>{
    $(window).scroll(()=>{
        let page_height = $(document).height();
        let window_height = $(window).height();
        let view_port = page_height - window_height;
        let scroll = ($(window).scrollTop() / view_port) * 100;
        $('.indicator').css('width',`${scroll}%`);
    });  
    }
)