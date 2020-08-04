

// Search Bar
  $(document).ready(function(){
    $('input.autocomplete').autocomplete({
      data: {
        "{{ review.title }}": null,
      },
    });
    $('textarea#reviews').characterCounter();
    $('.modal').modal();
  });