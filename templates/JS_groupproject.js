

function NextQuestion() {
  ans = ($("input[name=Choices]:checked").val())
  jQuery.ajax({
    type: "post",
    url: "/brainquiz",
    data: {
      "answer": ans
    }
  })
<<<<<<< HEAD
}
=======

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
>>>>>>> f6c11d5fd0fb0661f3cd2fc92b1c1d71df5d38a3
