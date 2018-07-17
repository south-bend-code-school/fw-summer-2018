(function(){
  $(document).ready(initialize);

function initialize(){
$(".monster").click(rawr);
$(".winner").click(yay);
}

function yay(){
  alert ("YOU HAVE WON!");
  $('body').css('background-image', 'url(trophy.jpg)');
}

function rawr(){
  alert ("YOU HAVE LOST!");
  $('body').css('background-image', 'url(youjustlost.jpg)');

}


})();
