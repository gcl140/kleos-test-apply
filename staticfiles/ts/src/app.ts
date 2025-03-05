const applyGlassmorphism = (elementId: string) => {
    const element = document.getElementById(elementId);
    if (element) {
        element.style.backdropFilter = "blur(10px)";
        element.style.backgroundColor = "rgba(255, 255, 255, 0.1)";
        element.style.border = "1px solid rgba(255, 255, 255, 0.3)";
    }
};

document.addEventListener("DOMContentLoaded", () => {
    applyGlassmorphism("glass-effect");
});

const toggleDarkMode = () => {
    document.body.classList.toggle("dark-mode");
};

document.addEventListener("DOMContentLoaded", () => {
    const darkModeButton = document.getElementById("dark-mode-toggle");
    if (darkModeButton) {
        darkModeButton.addEventListener("click", toggleDarkMode);
    }
});
