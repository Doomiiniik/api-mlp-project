// Automatyczne wykrywanie backendu
const API_URL = window.location.hostname === "localhost"
    ? "http://localhost:8000"
    : "https://api.doomiiniik.dev";

// Mapowanie 0–25 → A–Z
function numberToLetter(num) {
    const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    return letters[num] || "?";
}

document.getElementById("predictBtn").onclick = async () => {
    const raw = document.getElementById("inputData").value;

    try {
        const data = JSON.parse(raw);

        const response = await fetch(`${API_URL}/v1/predict`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ features: data })
        });

        const result = await response.json();

        console.log("Prediction from backend:", result.predicted_class);

        const letter = numberToLetter(result.predicted_class);

        document.getElementById("result").innerText = "Wynik: " + letter;
        document.getElementById("resultBox").style.display = "block";

    } catch (err) {
        document.getElementById("result").innerText = "Błąd: " + err;
        document.getElementById("resultBox").style.display = "block";
    }
};
