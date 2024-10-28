function oi(event) {
    event.preventDefault();
    
    let user = document.getElementById("surname").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let password1 = document.getElementById("password1").value;

    if (email === localStorage.getItem("email") && user === localStorage.getItem("user")){
        alert("account already exists with this email")
        return;
    }

    if (password === password1 && password.length >= 8) {
        localStorage.setItem("user", user);
        localStorage.setItem("email", email);
        localStorage.setItem("password", password);
        alert("Account created!");
        window.location.href = "log%20in.html";
    } else {
        alert("Password incorrect or its length is shorter than 8");
    }
}



function io(event) {
    event.preventDefault();
    
    let user1 = document.getElementById("surname1").value;
    let email1 = document.getElementById("email1").value;
    let password2 = document.getElementById("password1").value;

    let storeduser = localStorage.getItem("user");
    let storedemail = localStorage.getItem("email");
    let storedpassword = localStorage.getItem("password");

    if (user1 === storeduser && email1 === storedemail && storedpassword === password2) {
        alert("Login correct!");
        
    } else {
        alert("Login incorrect!");
        window.location.href = "log%20in.html";
    }
}


