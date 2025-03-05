const applyGlassmorphism = (elementId) => {
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
