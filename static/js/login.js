$("#signupInputbtn").attr("disabled",true)
$("#terms").click(function(){
    if(document.getElementById("terms").checked){
        $("#signupInputbtn").attr("disabled",false)
    }else{
        $("#signupInputbtn").attr("disabled",true)
    }
})