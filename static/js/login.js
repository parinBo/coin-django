$(document).ready(function(){
    $("#signupForm").hide();
    $("#signinBtn").click(function(){
        $(this).css("background-color", "gray");
        $("#signupBtn").css("background-color", "#0a58ca");
        $("#signinForm").show();
        $("#signupForm").hide();
    });


    $("#signupBtn").click(function(){
        $(this).css("background-color", "gray");
        $("#signinBtn").css("background-color", "#0a58ca");
        $("#signinForm").hide();
        $("#signupForm").show();
      });
  });