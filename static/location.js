addEventListener('DOMContentLoaded', (evt)=> {
    navigator.geolocation.getCurrentPosition(write_positions);
});

function write_positions(position) {
    $.ajax({ 
        url: '/positions', 
        type: 'POST', 
        contentType: 'application/json', 
        data: JSON.stringify({ 'longitude': position.coords.longitude, 'latitude': position.coords.latitude}), 
        success: function(response) {
            document.write(String(response))
        }, 
        error: function(error) { 
            console.log(error); 
        }});
}