function NextQuestion() {
  ans = ($("input[name=Choices]:checked").val())
  num = ($("#qtn").val())
  //if(ans === document.querySelector()
  jQuery.ajax({
    type: "post",
    url: "/brainquiz",
    data: {
      "answer": ans,
      "question": num
    }
  })
}
