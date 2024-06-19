const header = document.querySelector("header");
const hamburgerBtn = document.querySelector("#hamburger-btn");

// Toggle mobile menu on hamburger button click
hamburgerBtn.addEventListener("click", () => {
// Check if the menu is currently shown
if (header.classList.contains("show-mobile-menu")) {
    // If it is, hide it
    header.classList.remove("show-mobile-menu");
} else {
    // If it's not, show it
    header.classList.add("show-mobile-menu");
}
});