$(document).ready(function () {

    var mydata = JSON.parse(data);
    ipconfig = mydata[0].ipconfig + mydata[0].port



    if (window.s) {
        window.s.close()
    };
    /*创建socket连接*/
    var h = document.getElementById("h")
    fromuser = h.getAttribute("fromuser")
    touser = h.getAttribute("touser")
    var socket = new WebSocket("ws://"+ipconfig+"/mess_connect/"+fromuser+"/"+touser+"/");
    socket.onopen = function () {
        socket.send('1');//成功连接上Websocket
    };
    socket.onmessage = function (e) {
        var obj_temp = JSON.parse(e.data);
        if (obj_temp.fromuser == fromuser ) {
            $('#chartarea').append(
                '<li style="margin-top: 0.2rem">'
               + '<div style="float: right;">'
                  +  '<img src="/static/mdeia/'+touser+'.png"'+' style="width: 1.5rem;height: 1.5rem;border-radius: 0.2rem;">' +
                '</div>'               +
                '<div style="margin-left: 0.3rem;float: right;width: 6.5rem;">' +
                    '<p style="white-space: pre-line;background: yellow;'+
                            'border-radius: 0.2rem;'+
                            'margin-top: 0.4rem;'+
                            'margin-bottom: 0.5rem;'+
                            'display: inline-block;'+
                            'padding: 0.2rem;'+
                             'float: right;'+
                            'margin-right: 0.2rem;'+
                            '">'+obj_temp.message+ '</p>' +
                '</div>' +
            '</li>'
            )


        }else {

            $('#chartarea').append('<li>' +
               ' <div style="float: left;">' +
                    '<img src='+"/static/mdeia/" + fromuser + ".png"+" style=\"width: 1.5rem;height: 1.5rem;border-radius: 0.2rem;\">"  +
                '</div>' +
                '<div style="margin-left: 0.3rem;float: left;width: 6.5rem;">' +

                    '<p style="white-space: pre-line;background: white;'+
                            'border-radius: 0.2rem;' +
                            'margin-top: 0.4rem;' +
                            'padding: 0.2rem;' +
                             'display: inline-block;'+
                            'margin-bottom: 0.5rem;' +
                            '">'+obj_temp.message  +'</p>'+
                '</div>' +
            '</li>');
        }

        //

    };
    // Call onopen directly if socket is already open
    if (socket.readyState === WebSocket.OPEN) socket.onopen();
    window.s = socket;


    $('#send_message').click(function () {
        //如果未连接到websocket
        if (!window.s) {
            alert("websocket未连接.");
        } else {
            window.s.send($('#thisText').val());//通过websocket发送数据
            $('#thisText').val('')
        }
    });

    // $('#close_websocket').click(function () {
    //     if (window.s) {
    //         window.s.close();//关闭websocket
    //         console.log('websocket已关闭');
    //     }
    // });

    // var xiaDan = document.getElementById("once_purchase")
    $('#once_purchase').click(function () {

        var once_purchase = document.getElementById("once_purchase")
        shopid = once_purchase.getAttribute("shopid")
        console.log(shopid)
        $.post("/changecart/0/",{"shopid":shopid}, function(data){
            if (data.status == "success"){
                //添加成功，把中间的span的innerHTML变成当前的数量
               // alert("亲，已经在购物车等待您！")
                var msg = "已经添加购物车，是否跳转页面";
                if (confirm(msg)==true){
                    window.location.href = "http://"+ipconfig+"/cart/0/"  //你也可以在这里做其他的操作
                }else{
                    return false;
                }
            }
            if (data.status == "false"){
                var msg = "不能重复添加，是否跳转页面";
                if (confirm(msg)==true){
                    window.location.href = "http://"+ipconfig+"/cart/0/"  //你也可以在这里做其他的操作
                }else{
                    return false;
                }
            }


        })
    })

})