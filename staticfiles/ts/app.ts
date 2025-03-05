interface ToastElement extends HTMLElement {
    querySelector: (selector: string) => HTMLElement | null;
}

const toggleDarkMode = () => {
    document.documentElement.classList.toggle("dark");
    localStorage.setItem("theme", document.documentElement.classList.contains("dark") ? "dark" : "light");
};

const initializeDarkMode = () => {
    if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark');
    } else {
        document.documentElement.classList.remove('dark');
    }
};

const initializeToasts = () => {
    const toasts = document.querySelectorAll('.toast') as NodeListOf<ToastElement>;
    
    toasts.forEach((toast) => {
        const progressBar = toast.querySelector('.progress-bar');
        if (progressBar) {
            setTimeout(() => {
                toast.classList.add('animate-fade-out');
                setTimeout(() => {
                    toast.remove();
                }, 300);
            }, 4500);
        }
    });
};

document.addEventListener("DOMContentLoaded", () => {
    initializeDarkMode();
    
    const darkModeButton = document.getElementById("dark-mode-toggle");
    if (darkModeButton) {
        darkModeButton.addEventListener("click", toggleDarkMode);
    }
    
    initializeToasts();
});