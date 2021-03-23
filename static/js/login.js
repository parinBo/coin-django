$("input[type=submit]").attr("disabled",true)
$("#terms").click(function(){
    if(document.getElementById("terms").checked){
        $("input[type=submit]").attr("disabled",false)
    }else{
        $("input[type=submit]").attr("disabled",true)
    }
})