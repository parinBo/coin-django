$(document).ready(function(){
    $("#signupform").toggle()
    $("#signinbtn").click(function(){
        $("#signinform").show()
        $("#signupform").hide()
        $("#signupbtn").removeClass("active-btn").addClass("wait-btn");
        $(this).removeClass("wait-btn").addClass("active-btn");
        $()
    })
    $("#signupbtn").click(function(){
        $("#signupform").show()
        $("#signinform").hide()
        $("#signinbtn").removeClass("active-btn").addClass("wait-btn");
        $(this).removeClass("wait-btn").addClass("active-btn");
    })
   
})
