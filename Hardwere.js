document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".nav-btn");
    const tabs = document.querySelectorAll(".tab-content");

    buttons.forEach(btn => {
        btn.addEventListener("click", () => {
            const target = btn.dataset.tab;

            tabs.forEach(tab => {
                tab.classList.remove("active");
            });

            const targetTab = document.getElementById(target);
            if (targetTab) {
                targetTab.classList.add("active");
            }
        });
    });
});

