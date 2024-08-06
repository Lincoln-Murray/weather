addEventListener('DOMContentLoaded', (evt)=> {
    resize()
});

addEventListener('resize', (evt)=> {
    resize()
});

function resize() {
    document.getElementById('feelslike_c').style.left = String(window.innerWidth/2-64) + 'px'
}


var timer = setInterval(function() {
    if (document.getElementById('header') !== null) {
        resize()
        clearInterval(timer)
        timer = null
    }
}, 200);