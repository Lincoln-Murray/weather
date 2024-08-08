addEventListener('DOMContentLoaded', (evt)=> {
    resize()
});

addEventListener('resize', (evt)=> {
    resize()
});

function resize() {
    document.getElementById('feelslike_c').style.left = String(window.innerWidth/2-64) + 'px'
}

directions = ['N','NNE','NE','ENE','E','ESE','SE','ESE','S','SSW','SW','WSW','W','WNW','NW','NNW']

var timer = setInterval(function() {
    if (document.getElementById('header') !== null) {
        resize()
        console.log(document.getElementById('wind_dir').alt)
        console.log(document.getElementById('wind_dir').style)
        document.getElementById('wind_dir').style.transform = 'rotate(' + String(directions.indexOf(document.getElementById('wind_dir').alt)*22.5-90) + 'deg)'
        arrows = document.getElementsByClassName('wind_dir')
        for (var i = 0, length = arrows.length; i < length; i++) {
            arrows[i].style.transform = 'rotate(' + String(directions.indexOf(arrows[i].alt)*22.5-90) + 'deg)'
        }
        clearInterval(timer)
        timer = null
    }
}, 200);