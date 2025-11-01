const firstName = document.getElementById("first-name")
const lastName = document.getElementById("last-name")
const email = document.getElementById("email")
const password = document.getElementById("password")

First Name cannot be empty
Last Name cannot be empty
Looks like this is not an email
Password cannot be empty

function errorMessage(){

    var x=document.forms["email_form"]["email"].value;
    if (x==null || x=="")
    {
        var error_image = document.getElementById('error-image');
        error_image.style.display = 'inline';
        alert("Looks like this is not an email");
        return false;
    }

}