$(document).ready(function(){
    URL = window.URL || window.webkitURL;
    var gumStream;
    //stream from getUserMedia() 
    var rec;
    //Recorder.js object 
    var input;
//MediaStreamAudioSourceNode we'll be recording 

var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext = new AudioContext;

//new audio context to help record 
var recordButton = document.getElementById("recordButton");
var stopButton = document.getElementById("stopButton");

recordButton.addEventListener("click", startRecording);
stopButton.addEventListener("click", stopRecording);
//recordButton.addEventListener("click", completeRecording);
//var recordButton = document.getElementById("recordButton");

function startRecording() { 
    console.log("recordButton clicked");
 
    // Start Recording
    var constraints = {
        audio: true,
        video: false
    } 

    /* Disable the record button until we get a success or fail from getUserMedia() */

    recordButton.disabled = true;
    stopButton.disabled = false;

    /* We're using the standard promise based getUserMedia()

        https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia */

    navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
        console.log("getUserMedia() success, stream created, initializing Recorder.js ..."); 
        /* assign to gumStream for later use */
        gumStream = stream;
        /* use the stream */
        input = audioContext.createMediaStreamSource(stream);
        /* Create the Recorder object and configure to record mono sound (1 channel) Recording 2 channels will double the file size */
        rec = new Recorder(input, {
            numChannels: 1
        }) 
        //start the recording process 
        rec.record()
        console.log("Recording started");
    }).catch(function(err) {
        //enable the record button if getUserMedia() fails 
        recordButton.disabled = false;
        stopButton.disabled = true;

    });
}

function stopRecording() {
    console.log("stopButton clicked");
    //disable the stop button, enable the record too allow for new recordings 
    stopButton.disabled = true;
    recordButton.disabled = false;
    rec.stop(); //stop microphone access 
    gumStream.getAudioTracks()[0].stop();

    rec.exportWAV(createDownloadLink);
}


//This sends data via upload to the backend/database
function createDownloadLink(blob) {
    var url = URL.createObjectURL(blob);
    var au = document.createElement('audio');
    var li = document.createElement('li');
    var link = document.createElement('a');
    //add controls to the <audio> element 
    au.controls = true;
    au.src = url;
    //link the a element to the blob 
    link.href = url;
    link.download = new Date().toISOString() + '.wav';
    link.innerHTML = link.download;
    //add the new audio and a elements to the li element 
    li.appendChild(au);
    li.appendChild(link);
    //add the li element to the ordered list 
    recordingsList.appendChild(li);

    const max = 3;

    $('ul, ol').each(function(){
      $(this).find('li').each(function(index){
        if(index >= max) $(this).remove().document.getElementById("recordButton").disabled=true;
      });
    })    

    var filename = new Date().toISOString();
    //filename to send to server without extension 
    //upload link 
    var upload = document.createElement('a');
    upload.href = "#";
    upload.innerHTML = "Upload";
    }
})


// Functions to upload Audio Files with ajax
async function  submitAudio(){
    let csrf = $('input[name="csrfmiddlewaretoken"]').val();
    const fd = new FormData();    
    fd.append("csrfmiddlewaretoken", csrf);

    const audios =document.getElementsByTagName('audio');

    for(i=0; i < audios.length;i++){
        data = await fetch(audios[i].src);
        blob = await data.blob()
        fd.append("audio_data", blob)

    }
    
    const pathname = window.location.pathname;
    // Use same path name because we upload to same url name as the current pathname 
    $.ajax({
        type:'post',
        url: pathname,
        // type: $(this).attr('method'),
        data: fd,
        cache: false,
        processData: false,
        contentType: false,
        success: function(fd) {
            alert('Success')
            }
        });
    }



    async function submitAllAudio(event){
        event.preventDefault();
        const audios = document.getElementsByTagName('audio');
        if (audios.length < 3){
            alert("Must Record 3 Audios!");
            return;
        }else{
            await submitAudio(); // From record.js 
            alert("Success");
            // Simulate HTTP redirect
            window.location.href = event.target.href;
        }

    }