

// Search Bar
  $(document).ready(function(){
    $('input.autocomplete').autocomplete({
      data: {
        "Mindset": null,
        "Grit": null,
        "Awaken The Giant Within": null
      },
    });
  });

  // Reviews textarea
    $(document).ready(function() {
    $('textarea#reviews').characterCounter();
  });