$(document).ready(function(){
    var mydata = JSON.parse(data);
    ipconfig = mydata[0].ipconfig + mydata[0].port

    var clicks = document.getElementsByClassName("info_click")
    for (var i = 0; i < clicks.length; i++){
        clicking = clicks[i]
        clicking.addEventListener("click", function(){
            pid = this.getAttribute("ga")
            window.location.href = "http://"+ipconfig+"/courseInformation/"+pid+"/"
            // window.location.href = "http://127.0.0.1:8000/courseInformation/"+pid
        })
    }

})