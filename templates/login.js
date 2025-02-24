function validate(){
    var username=document.getElementById("username").value
    var password=document.getElementById("password").value
    var un="admin1234"
    var pw="user1234"
    if(username==un && password==pw){
        alert("login succesfully");
    }
    else{
        alert("login failed");
    }
}