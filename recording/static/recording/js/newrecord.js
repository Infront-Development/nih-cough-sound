const recordAudio = () => {
    return new Promise( resolve => {
        navigator.mediaDevices.getUserMedia({
            audio : true
        })
          .then(
            stream => {
                const mediaRecorder = new MediaRecorder(stream);
                const audioChunks = new Array();

                mediaRecorder.addEventListener("dataavailable", event =>{
                    audioChunks.push(event.data);
                });
                
                const start = () => {
                    mediaRecorder.start();
                };

                const stop = () => {
                    return new Promise(resolve => {
                        mediaRecorder.addEventListener("stop", () => {
                            const audioBlob = new Blob(audioChunks, {
                                type : 'audio/wav'
                            });
                            const audioUrl = URL.createObjectURL(audioBlob);
                            const audio = new Audio(audioUrl);
                            const play = () =>{
                                audio.play();
                            };
                            resolve({audioBlob, audioUrl, play});
                        }) // End event listener
                        mediaRecorder.stop();
                    })
                }
                return resolve({start, stop});  
            }

        )
    })
}

const record = async (id) => {
    
    const recorder = await recordAudio();
    recorder.start();
    const stopButton = document.getElementById(id);   

    stopButton.onclick = async () => { 
        const {audioBlob, audioUrl, play } = await recorder.stop();
        console.log(audioUrl);
        // Do dom manipulation here
    }
}

// Usage
/*
e.g. makeRecordFunction("recordButtonOne", "stopButtonOne")
*/
function makeRecordFunction(playID , stopID){
    const playButton = document.getElementById(playID);
    playButton.onclick = () => record(stopID);
}