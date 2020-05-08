$(document).ready(function() {

    var flag = document.getElementById("flag").innerHTML



    var ischoses = document.getElementsByClassName("ischoose")
    var summoney = document.getElementById("summoney").innerHTML
    for (var j = 0; j < ischoses.length; j++) {
        ischose = ischoses[j]

        ischose.addEventListener("click", function () {
            money = this.getAttribute("money")
            pid = this.getAttribute("shopid")

            if(this.style.backgroundColor=='white'){
                $.post("/changecart/2/", {"shopid": pid,"status":1}, function (data) {
                if (data.status == "success") {
                    var ischoose = document.getElementById(pid+"choose")
                    ischoose.style.backgroundColor='red';
                    summoney = parseInt(money) + parseInt(summoney)
                    document.getElementById("summoney").innerHTML = summoney

                    }
                })
            }
            else if(this.style.backgroundColor=='red'){
                $.post("/changecart/2/", {"shopid": pid,"status":0}, function (data) {
                if (data.status == "success") {
                    var ischoose = document.getElementById(pid+"choose")
                    ischoose.style.backgroundColor='white';
                    summoney =  parseInt(summoney) - parseInt(money)
                    document.getElementById("summoney").innerHTML = summoney
                    }
                })

            }else {
                //状态为jia传到后台，实现ischose变为1，返回状态为success为成功
                $.post("/changecart/2/", {"shopid": pid,"status":1}, function (data) {
                if (data.status == "success") {
                        var ischoose = document.getElementById(pid+"choose")
                        ischoose.style.backgroundColor='red';
                        summoney = parseInt(money) + parseInt(summoney)
                        document.getElementById("summoney").innerHTML = summoney
                    }
                })


            }

        }, false)
    }
    var deleteshops = document.getElementsByClassName("delete")
    for (var i = 0; i < deleteshops.length; i++){
        deleteshop = deleteshops[i]

        deleteshop.addEventListener("click", function(){
            pid = this.getAttribute("ga")

            $.post("/changecart/1/",{"shopid":pid}, function(data){
                if (data.status == "success"){
                    //更改总价
                    document.getElementById("summoney").innerHTML = data.price
                    //删除元素
                     var div = document.getElementById(pid+"div")
                     div.parentNode.removeChild(div)


                }
            })
        })
    }

    if(flag == '1'){
        alert("亲，您的订单已经支付成功！")
    }
})