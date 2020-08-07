

// Search Bar
  $(document).ready(function(){
    $('input.autocomplete').autocomplete({
      data: {
        "{{ review.title }}": null,
      },
    });
    $('.modal').modal();
  });

   $(document).ready(function(){
    $('.sidenav').sidenav();
  });
        