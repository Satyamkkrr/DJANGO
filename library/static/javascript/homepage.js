
  $(document).ready(function(){

    var showHeaderAt = 60;

    var win = $(window),
    body = $('body');

    // Show the fixed header only on larger screen devices

    if(win.width() > 400){

      // When we scroll more than 150px down, we set the
      // "fixed" class on the body element.

      win.on('scroll', function(e){

        if(win.scrollTop() > showHeaderAt) {
          body.addClass('fixed');
        }
        else {
          body.removeClass('fixed');
        }
      });

    }

  });


function openNav() {
    document.getElementById("mySidenav").style.width = "30%";
    document.getElementById("main").style.marginLeft = "10%";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
}
