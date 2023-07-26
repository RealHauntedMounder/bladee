var currentAudio = null;


document.addEventListener('DOMContentLoaded', function() {
  var playIcons = document.querySelectorAll('.fa-play');
  for (var i = 0; i < playIcons.length; i++) {
    playIcons[i].addEventListener('click', playAudio);
  }


  
  function playAudio(event) {
    var url = event.target.getAttribute('data-url');
    var audio = new Audio(url);
    var playIcon = event.target;
    var li = playIcon.closest('li');
    
    if (currentAudio) {
      var currentPlayIcon = currentAudio.playIcon;
      var currentLi = currentPlayIcon.closest('li');
      currentAudio.pause();
      currentPlayIcon.classList.remove('text-red-800');
      currentLi.classList.remove('bg-gray-700');
    }
    
    currentAudio = audio;
    currentAudio.playIcon = playIcon;
    playIcon.classList.add('text-red-800');
    audio.play();
  }

});