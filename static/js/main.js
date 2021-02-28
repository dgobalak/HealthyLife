feather.replace()   // For the menu icons to display

var healthData = {
    email: "",
    date: "",
    age: -1,
    blood_pressure: "",
    heart_rate: -1,
    body_temp: -1,
    height: 0.0,
    weight: 0.0
};

const begin = document.getElementById('begin-button');
const voice2text = document.getElementById('voice2text')

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recorder = new SpeechRecognition();

recorder.onstart = () => {
    console.log('voice is activated, you can talk')
}

recorder.onresult = (event) => {
    const current = event.resultIndex;
    const transcript = event.results[current][0].transcript;
    voice2text.textContent = transcript;
    console.log(transcript);
}

begin.addEventListener('click', main);

function speak (message) {
    var msg = new SpeechSynthesisUtterance(message)
    var voices = window.speechSynthesis.getVoices()
    msg.voice = voices[0]
    window.speechSynthesis.speak(msg)
}

function main() {
    speak("What is your blood pressure?");
    setTimeout(() => {recorder.start();}, 500);
}
