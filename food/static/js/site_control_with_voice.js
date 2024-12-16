function convert_audio_to_text(params) {
    let text = textArea.value;
    // Create a new SpeechSynthesisUtterance object
    let utterance = new SpeechSynthesisUtterance();
    // Set the text and voice of the utterance
    utterance.text = text;
    utterance.voice = window.speechSynthesis.getVoices()[0];
    // Speak the utterance
    window.speechSynthesis.speak(utterance);
}

function get_command() {
    var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition
    const recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;
    recognition.start();
    recognition.onresult = function(event) {
        let result = event.results[0][0].transcript;
        if (result == "") {
            convert_audio_to_text = "command started"
        }
        console.log(result);
    }

}
get_command()
