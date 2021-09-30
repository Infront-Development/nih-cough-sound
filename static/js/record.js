
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
var attempts = 0;
function pass(reco) {
  attempts++;
    if (reco.identifier.value=="GG") { 
      if (reco.pass.value=="123") { 
        attempts = 0;
       // window.location('https://www.google.com/');
      } else {
        //alert("Invalid Password");
        recordButton.style.display = attempts === 3 ? "none" : "block";
      }

    } else {  //alert("Invalid UserID");
    recordButton.style.display = attempts === 3 ? "none" : "block";
    }
  
}

var stopButton = document.getElementById("stopButton");

recordButton.addEventListener("click", startRecording);
stopButton.addEventListener("click", stopRecording);
//recordButton.addEventListener("click", completeRecording);

/*let recordButton = document.querySelectorAll('record');
let stopButton = document.querySelectorAll('stop');
let recordingsList = document.querySelectorAll('list');

recordButton.addEventListener('click', () => {
    if(recordingsList > 3) recordButton.disabled = true
    else recordButton.disabled = true;
});
*/
//var recordButton = document.getElementById("recordButton");

function startRecording() { 
    console.log("recordButton clicked");
 
    // Start Recording
    var constraints = {
        audio: true,
        video: false
    } 
    /*$('recordButton').click(function(recordButton) {
        if(!recordButton.click || recordButton.click == 3){//activate on first click only to avoid hiding again on multiple clicks
          // code here. // It will execute only once on multiple clicks
          recordButton.disabled = true;
          stopButton.disabled = false;
        }
      });*/

    /* Disable the record button until we get a success or fail from getUserMedia() */

    recordButton.disabled = true;
    stopButton.disabled = false;
    
   /* var startRecordcounter=3;
    $("recordButton").on('click', function(e) {
        if (startRecordcounter > 3) {
            recordButton.disabled = true;

            startRecordcounter++;
        }
    });*/

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

/*function completeRecording() {
    var startRecordcounter=3;
    $("recordButton").on('click', function(e) {
        if (startRecordcounter > 3) {
            recordButton.disabled = true;

            startRecordcounter++;
        }
    });
*/
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

    var filename = new Date().toISOString();
    //filename to send to server without extension 
    //upload link 
    var upload = document.createElement('a');
    upload.href = "#";
    upload.innerHTML = "Upload";
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    var fd = new FormData();

    // audio_file = new File([blob], link.download,{ type : "audio/wav"});
    
    fd.append("audio_data", blob, filename);
    fd.append('csrfmiddlewaretoken', csrf)

    $.ajax({
        type:'post',
        url: '/recording/record',
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
})
