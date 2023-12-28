const initSlider = () =>{
    const scrollbarThumb = slideScrollbar.querySelector('.scrollbar-thumb');

    // handle scrollbar drag
    scrollbarThumb.addEventListener("mousedown", (e) =>{
        const startX = e.clientX;
        const thumbPosition = scrollbarThumb.offsetLeft;

        //update thumb position on mouse move
        const handleMouseMove = (e) =>{
            const deltaX = e.clientX - startX;
            const newThumbPosition = thumbPosition + deltaX;
            const maxThumbPosition = slideScrollbar.getBoundingClientRect().width - scrollbarThumb.offsetwidth;


            const boundedPosition = Math.max(0, Math.min(maxThumbPosition, newThumbPosition));
            const scrollPosition = (boundedPosition / maxThumbPosition) *maxScrollLeft;

            scrollbarThumb.style.left = `${boundedPosition}px`;
            imageList.scrollLeft =scrollPosition;
        }
        //remove event listener for drag interaction
        const handleMouseUp = () =>{
            document.addEventListener("mousemove", handleMouseMove);
            document.addEventListener("mouseup", handleMouseUp);
        }
    });
}

function btn(){
    window.location.href='hotelacc'
}

function btn_2(){
    window.location.href='team'
}