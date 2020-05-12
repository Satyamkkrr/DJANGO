$('.btn-expand-collapse').click(function(e) {
    $('.navbar-primary').toggleClass('collapsed');
});
//* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
var dropdown = document.getElementsByClassName("dropdown-btn");
var i;
