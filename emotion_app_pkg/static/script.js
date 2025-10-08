const form = document.getElementById("emotionForm");
const textInput = document.getElementById("textInput");

form.addEventListener("submit", () => {
    // Optional: Disable button while analyzing
    form.querySelector("button").disabled = true;
    form.querySelector("button").innerText = "Analyzing...";
});
