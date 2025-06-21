document.addEventListener("DOMContentLoaded", () => {
    const counters = document.querySelectorAll('.count');

    const animateCounter = (counter) => {
        const target = +counter.getAttribute('data-count');
        const update = () => {
            const current = +counter.innerText;
            const increment = Math.ceil(target / 50);

            if (current < target) {
                counter.innerText = current + increment;
                setTimeout(update, 20);
            } else {
                counter.innerText = target;
            }
        };
        update();
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                animateCounter(counter);
                observer.unobserve(counter); // animate once
            }
        });
    }, {
        threshold: 0.6
    });

    counters.forEach(counter => {
        counter.innerText = '0';
        observer.observe(counter);
    });
});