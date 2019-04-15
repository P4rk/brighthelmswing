$(document).ready(function(){
  $(document).on('scroll', function() {
    if($(document).scrollTop() > 75) {
      $('.navbar-swing').addClass('navbar-swing--small');
    } else {
      $('.navbar-swing').removeClass('navbar-swing--small');
    }
  });
});