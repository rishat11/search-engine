 $(function(){
  $('.input-search').focus(function(){
    $(this).parent().addClass('expanded');
  });

  $('.input-search').blur(function(){
    	$(this).parent().removeClass('expanded');
  });
});