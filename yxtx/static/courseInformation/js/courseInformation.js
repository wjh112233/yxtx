$(document).ready(function(){
    document.documentElement.style.fontSize = innerWidth / 10 + "px";
    var mydata = JSON.parse(data);
    ipconfig = mydata[0].ipconfig + mydata[0].port

    var mydata = JSON.parse(data);
    ipconfig = mydata[0].ipconfig + mydata[0].port


    var sayGood = document.getElementById("sayGood")
    var count1 = 0
    sayGood.addEventListener("click" , function () {
        count1++

        if (count1 == 1){
            sayGood.style.color = "red"
        }
        if (count1 == 2){
            sayGood.style.color = ""
            count1 = 0
        }

    })

    var collect = document.getElementById("collect")
    var count2 = 0
    collect.addEventListener("click" , function () {
        count2++
        if (count2 == 1){
            collect.style.color = "red"
        }
        if (count2 == 2){
            collect.style.color = ""
            count2 = 0
        }

    })

    $("#iwant").click(function () {
        pid = this.getAttribute("want")
        window.location.href ="http://"+ipconfig+"/chart/"+pid+"/0/"
    })




})


