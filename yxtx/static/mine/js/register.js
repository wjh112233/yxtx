$(document).ready(function(){
    var accunt = document.getElementById("accunt")
    var accunterr = document.getElementById("accunterr")
    var checkerr = document.getElementById("checkerr")

    var pass = document.getElementById("pass")
    var passerr = document.getElementById("passerr")

    var passwd = document.getElementById("passwd")
    var passwderr = document.getElementById('passwderr')
    accunt.addEventListener("focus", function(){
        accunterr.style.display = "none"
        checkerr.style.display = "none"
    },false)

    accunt.addEventListener("blur", function(){
        instr = this.value
        var reg = /^1([38]\d|5[0-35-9]|7[3678])\d{8}$/;
		if(reg.test(instr)){
			$.post("/checkuserid/", {"userphone":instr}, function(data){
            if (data.status == "error"){
                checkerr.style.display = "block"
            }
        })
		}else{
			return;
		}

    },false)



    pass.addEventListener("focus", function(){
        passerr.style.display = "none"
    },false)
    pass.addEventListener("blur", function(){
        instr = this.value
        if (instr.length < 6 || instr.length > 16){
            passerr.style.display = "block"
            return
        }
    },false)


    passwd.addEventListener("focus", function(){
        passwderr.style.display = "none"
    },false)
    passwd.addEventListener("blur", function(){
        instr = this.value
        if (instr != pass.value){
            passwderr.style.display = "block"
        }
    },false)

})