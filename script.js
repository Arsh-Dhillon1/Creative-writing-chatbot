function fetchPrompt() {
    let genre = document.getElementById("searchBox").value || "sci-fi"; // Default to sci-fi if empty

    fetch(`/generate_prompt?genre=${genre}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = data.prompt || "Error: No prompt found";
        })
        .catch(error => {
            document.getElementById("result").innerText = "API Connection Failed";
            console.error("Error:", error);
        });
}
