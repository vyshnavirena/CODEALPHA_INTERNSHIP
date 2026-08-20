// ==========================================
// PHISHING AWARENESS TRAINING
// JavaScript
// ==========================================


// ==========================================
// START TRAINING BUTTON
// ==========================================

function startTraining() {

    alert(
        "Welcome to Phishing Awareness Training! 🛡️\n\n" +
        "You will learn how to identify phishing attacks, " +
        "recognize warning signs, and stay safe online."
    );

    document.getElementById("learn").scrollIntoView({
        behavior: "smooth"
    });
}


// ==========================================
// QUIZ
// ==========================================

function checkAnswer(correct) {

    const result = document.getElementById("result");

    if (correct) {

        result.textContent =
            "✅ Correct! Always verify suspicious messages before clicking links.";

        result.style.color = "green";

    } else {

        result.textContent =
            "❌ Incorrect! Do not click suspicious links. Verify the message first.";

        result.style.color = "red";
    }
}


// ==========================================
// WELCOME MESSAGE
// ==========================================

console.log("Phishing Awareness Training website loaded successfully.");