

// Search Bar
  $(document).ready(function(){
    $('input.autocomplete').autocomplete({
      data: {
        "{{ review.title }}": null,
      },
    });
  });

   $(document).ready(function(){
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
    $('.modal').modal();
  });
        