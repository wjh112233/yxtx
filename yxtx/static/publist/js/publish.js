
window.onload=function(){

    var input=document.getElementById("userimg");

    var img;

    // 当用户上传时触发事件

    input.onchange=function(){

    document.getElementById("imgs").innerHTML="";

    readFile(this);

    }

//处理图片并添加都dom中的函数

var readFile=function(obj){

// 获取input里面的文件组

    var fileList=obj.files;

    //对文件组进行遍历，可以到控制台打印出fileList去看看

        for(var i=0;i<fileList.length;i++){

            var reader= new FileReader();

            reader.readAsDataURL(fileList[i]);

            // 当文件读取成功时执行的函数

            reader.onload=function(e){

            img=document.createElement('img');

            img.setAttribute("src",this.result);

            img.setAttribute("height","110px");

            img.setAttribute("width","110px");

            document.getElementById("imgs").appendChild(img)

            }

            //读取文件过程方法

            reader.onloadstart = function (e) {console.log("开始读取....");}

            reader.onprogress = function (e) { console.log("正在读取中....");}

            reader.onabort = function (e) {console.log("中断读取....");}

            reader.onerror = function (e) {console.log("读取异常....");}

            }

        }

}
