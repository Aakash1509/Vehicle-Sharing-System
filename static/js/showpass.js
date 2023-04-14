// function myFunction() {
//     var x = document.getElementById("myInput");
//     if (x.type === "password") {
//       x.type = "text";
//     } else {
//       x.type = "password";
//     }
//   }
const showPasswordToggle=document.querySelector(".showPasswordToggle");

const handleToggleInput=(e)=> {
if(showPasswordToggle.textcontent=="Show Password"){
    showPasswordToggle.textContent="Hide";
}
else{
    showPasswordToggle.textContent="Show Password";
}

};

showPasswordToggle.addEventListener('click',handleToggleInput);