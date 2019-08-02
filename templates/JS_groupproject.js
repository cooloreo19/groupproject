

function NextQuestion() {
  ans = ($("input[name=Choices]:checked").val())
  jQuery.ajax({
    type: "post",
    url: "/brainquiz",
    data: {
      "answer": ans
    }
  })
}
