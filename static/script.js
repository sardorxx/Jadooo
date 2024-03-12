const initSlider = () => {
    const imageList = document.querySelector(".slider-wrapper .image-list");
    const sliderButtons = document.querySelectorAll(".slider-wrapper .slide-button");
    const sliderScrollbar = document.querySelector(".container .slider-scrollbar");
    const scrollThumb = sliderScrollbar.querySelector(".scrollbar-thumb");
    const maxScrollLeft = imageList.scrollWidth - imageList.clientWidth;


    scrollThumb.addEventListener("mousedown", (e) => {
        const startX = e.clientX;
        const thumbPosition = scrollThumb.offsetLeft;
        const handleMouseMove = (e) => {
            const delaX = e.clientX - startX;
            const newThumbPosition = thumbPosition + delaX;
            const maxThumbpPosition = sliderScrollbar.getBoundingClientRect().width - scrollbarThumb.offsetWidth;

            const boundedPosition = Math.max(0, Math.min(maxThumbpPosition, newThumbPosition))
            const scrollPosition = (boundedPosition / maxThumbpPosition) * maxScrollLeft

            scrollThumb.style.left =  `${boundedPosition}px`;
            imageList.scrollLeft = scrollPosition;
        }

        const handleMouseUp = () => {
            document.removeEventListener('mousedown', handleMouseMove);
            document.removeEventListener('mouseup', handleMouseUp);

        }

        document.addEventListener('mousedown', handleMouseMove);
        document.addEventListener('mouseup', handleMouseUp);
    })

    sliderButtons.forEach(button => {
        button.addEventListener('click', () => {
            const direction = button.id === "prev_slide" ? -1 : 1;
            const scrollAmount = imageList.clientWidth * direction;
            imageList.scrollBy({left: scrollAmount, behavior: 'smooth'})
        })
    })

    const handleSlideButtons = () => {
        sliderButtons[0].style.display = imageList.scrollLeft <= 0 ? 'none' : 'block';
        sliderButtons[1].style.display = imageList.scrollLeft >= maxScrollLeft ? 'none' : 'block';
    }
    const updateScrollThumbPosition = () =>{
        const scrollPosition = imageList.scrollLeft;
        const thumbPosition = (scrollPosition / maxScrollLeft) * (sliderScrollbar.clientWidth - scrollThumb.offsetWidth)
        scrollThumb.style.left = `${thumbPosition}px`;
    }
    imageList.addEventListener('scroll', () => {
        handleSlideButtons();
        updateScrollThumbPosition()
    })
}
window.addEventListener('load', initSlider)