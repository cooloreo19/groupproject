function NextQuestion() {
  ans = ($("input[name=Choices]:checked").val())
  num = ($("#qtn").val())
  jQuery.ajax({
    type: "post",
    url: "/brainquiz",
    data: {
      "answer": ans,
      "question": num
    }
  })
}

 function selected(){
$(".buttonsec").click(function(){
          if($(this).is(':checked')){
              $(this).parent().addClass("selected");
          }
          $(".buttonsec").not(this).each(function(){
          $(this).parent().removeClass("selected");
          });
        });}

        $(document).ready(function (){
            selected();
        })
