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
                            resolve({audioBlob, audioUrl, audio});
                        }) // End event listener
                        mediaRecorder.stop();
                    })
                }
                return resolve({start, stop});  
            }

        )
    })
}

const record = async (id, callbackFn) => {
    
    const recorder = await recordAudio();
    recorder.start();
    const stopButton = document.getElementById(id);   

    stopButton.onclick = async () => { 
        const {audioBlob, audioUrl, audio } = await recorder.stop();
        callbackFn({audioBlob, audioUrl, audio});
        // Do dom manipulation here
    }
}
function makeRecordFunction(playID , stopID, callbackFn ){
    const playButton = document.getElementById(playID);
    playButton.onclick = () => record(stopID, callbackFn);
}

// Callback function takes 3 arguments : audioBlob, audioUrl, play as a single javascritp object
// audioBlob : An array of bytes representing the audio
// audioUrl  : A URL to the audio blob
// audio     : HTML Node of the audio tag
//Usage 
/*
makeRecordFunction("buttonOne", "buttonTwo", ({audioBlob, audioUrl, audio}) => {
    //Do Dom manipulation or operations here
}

*/