const navBar = document.querySelector("header"),
       menuBtns = document.querySelectorAll(".button_menu-in-header-box"),

       overlay = document.querySelector(".overlay");

     menuBtns.forEach((menuBtn) => {
       menuBtn.addEventListener("click", () => {
         navBar.classList.toggle("open");
       });
     });

     overlay.addEventListener("click", () => {
       navBar.classList.remove("open");
     });