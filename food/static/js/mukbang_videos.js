let videos = document.querySelectorAll(".mukbang-video");
let degs = [0,-4,4,0]
let video_index = 0
let zIndex = 1
let status_flag = [true,false,false,false]
for (let index = 0; index < videos.length; index++) {
    const element = videos[index];
    element.style.transform = `rotate(${degs[index]}deg)`
}
function show_info_mukmang() {
    
}

function plus_video_index() {
    videos[video_index].style.zIndex = zIndex
    videos[video_index].style.transform = "rotate(360deg)"
    video_index++;
    if (video_index == videos.length) {video_index = 0;}
    console.log(video_index);
    zIndex++
}
function positive_video_index() {
    videos[video_index].style.zIndex = zIndex
    videos[video_index].style.transform = "rotate(360deg)"
    video_index--;
    if (video_index == 0) {video_index = videos.length;}
    console.log(video_index);
    zIndex++
}
