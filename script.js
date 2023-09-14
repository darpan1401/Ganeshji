function playAudio(audioIndex) {
    // Send an HTTP request to trigger audio playback on your Python server
    fetch(`http://192.168.226.114:5000/run-code?audio=${audioIndex}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.text();
        })
        .then(data => {
            // Handle the response from the server, e.g., display a message
            alert(data);
        })
        .catch(error => {
            // Handle request or server errors
            console.error('Error:', error);
        });
}
