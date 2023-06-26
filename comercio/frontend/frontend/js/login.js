$(document).ready(function() {
    

    
})
function createUser(jsonData){
    let url_user = "http://localhost:3000/auth/registration";
    $.ajax({
        url: url_user,
        type: 'POST',
        data: jsonData,
        contentType: 'application/json',
        success: function(response) {
          // Handle the successful response
          console.log('User created successfully!');
        },
        error: function(xhr, status, error) {
          // Handle any errors that occur during the request
          console.log('Error:', status, error);
        }
      });
    
    

}

function obtainForm(){
    var username=document.getElementById("username_id").value
    var email_user=document.getElementById("email_id").value
    var pw1=document.getElementById("password1").value
    var pw2=document.getElementById("password2").value

    var jsonData={
        "username": username,
        "email": email_user,
        "password1": pw1,
        "password2": pw2
    };
    return(jsonData);
}

$("#registerButton").on("click",obtainForm);

createUser(obtainForm)