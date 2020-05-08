$(document).ready(function(){
    var mydata = JSON.parse(data);
    ipconfig = mydata[0].ipconfig + mydata[0].port


    window.confirm = function (message) {
            var iframe = document.createElement("IFRAME");
            iframe.style.display = "block";
            iframe.setAttribute("src", 'data:text/plain,');
            document.documentElement.appendChild(iframe);
            var alertFrame = window.frames[0];
            var result = alertFrame.window.confirm(message);
            iframe.parentNode.removeChild(iframe);
            return result;
    };
    var thisMmessage = document.getElementsByClassName("message_group")
    var timer ;
    for (var i = 0; i < thisMmessage.length; i++){
        clicking = thisMmessage[i]
        clicking.addEventListener("touchstart", function(e){
            piduserTo = this.getAttribute("userTo")
            timer = setTimeout(function () {
                timer = 0
                if (confirm("您确定删除本条消息？也将删除对方消息列表")){
                        $.post("/delete_usergroup/", {"piduserTo":piduserTo}, function(data){
                            if (data.status == "success"){
                                $(e.target).parent().parent().remove()
                            }
                        })
                }
            } , 2000);
        } , false)
        clicking.addEventListener("touchend", function(){
            clearTimeout(timer)
            if (timer != 0 ){
                piduserTo = this.getAttribute("userTo")  //
                pidShopId = this.getAttribute("ShopId")
                window.location.href = "http://"+ipconfig+"/chart/"+pidShopId+"/1/"

            }
        } , false)
    }

})

