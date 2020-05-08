document.documentElement.style.fontSize = innerWidth / 10 + "px";

var mydata = JSON.parse(data);
ipconfig = mydata[0].ipconfig + mydata[0].port

var r = confirm("您未进行资质认证，是否需要进行？")
if (r == true) {

}
else {
    window.location.href = "http://"+ipconfig+"/mine/"
}