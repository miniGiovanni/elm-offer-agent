let selectedBuild = "elm-simple.txt";

function selectBuild(build, element) {
    selectedBuild = build;

    document.querySelectorAll(".card").forEach(card => {
        card.classList.remove("active");
    });

    element.classList.add("active");

    updateVersionLabel();
}

async function copyPrompt() {
    const url = `https://raw.githubusercontent.com/miniGiovanni/elm-offer-agent/main/builds/${selectedBuild}`;

    const res = await fetch(url);

    if (!res.ok) {
        alert("Kon Elm niet laden!");
        return;
    }

    const text = await res.text();

    const full = text + "\n\n--- INPUT ---\nKLANT:\n\nOFFERTE:\n";

    navigator.clipboard.writeText(full);

    showToast(`Elm (${selectedBuild}) gekopieerd!`);
}

function showToast(message) {
    const toast = document.getElementById("toast");
    toast.innerText = message + "✅";
    toast.classList.add("show");

    setTimeout(() => {
        toast.classList.remove("show");
    }, 2000);
}

async function updateVersionLabel() {
    const url = `https://raw.githubusercontent.com/miniGiovanni/elm-offer-agent/main/builds/${selectedBuild}`;

    const res = await fetch(url);
    const text = await res.text();

    // eerste regel bevat versie
    const firstLine = text.split("\n")[0];

    document.getElementById("versionLabel").innerText = firstLine;
}

updateVersionLabel();