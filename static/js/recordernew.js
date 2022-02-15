const audioRecorder = () => {
    return new Promise((resolve) =>{
        let gumStream;
        let rec;
        let input;
        const AudioContext = window.AudioContext || window.webkitAudioContenxt;
        const audioContext = new AudioContext();
        const  start = () =>{
            navigator.mediaDevices.getUserMedia(
                { audio : true, video : false}
            ).then( function(stream){
                gumStream = stream;
                input = audioContext.createMediaStreamSource(stream);
                rec = new Recorder(input, {
                    numChannels : 1,
                })
    
                rec.record();
            })
        }
        
        // const _processBlob = (blob) =>{
        //         URL = window.webkitURL || window.URL;
        //         const audioUrl = URL.createObjectURL(blob);
        //         const audioBlob = blob;
        //         const audio = new Audio();
        //         audio.src = audioUrl;
        //         audio.controls = true;
        //         ret
        // }
        const stop = (callbackFn) =>{
                rec.stop();
                gumStream.getAudioTracks()[0].stop();
                rec.exportWAV(callbackFn);
        }
        return resolve({start, stop})

    })
}