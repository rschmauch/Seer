// Fonction pour afficher/masquer le menu déroulant
function toggleMenu() {
    const menu = document.getElementById("dropdownMenu");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}

// Fermer le menu si on clique en dehors
window.onclick = function(event) {
    const menu = document.getElementById("dropdownMenu");
    const icon = document.querySelector(".profile-icon");
    if (!icon.contains(event.target) && !menu.contains(event.target)) {
        menu.style.display = "none";
    }
};
