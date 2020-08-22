
// document.addEventListener('DOMContentLoaded', function() {
//     x=document.getElementById('answer_id_field')
//     if(x !== null)
//     {
//         console.log(x.val());
//     }
// // }, false);
// $(function () {
//     $("#question_id_field").change(function () {
//         var selectedText = $(this).find("option:selected").text();
//         console.log(selectedText);
//         // var selectedValue = $(this).val();
//         // alert("Selected Text: " + selectedText + " Value: " + selectedValue);
//     })
// })
window.addEventListener("load", function() {
    (function($) {
        $("#question_id_field").change(function() {
            var selectedText = $(this).find("option:selected").text();
            var selectedValue = $(this).val();
            $.ajax({
                url: "/api/answers/",
                type: 'GET',
                data:  {question: selectedValue},
                dataType: "json",
                success: function(resp){
                    $("#answer_id_field").empty();

                    
                    $.each(resp, function(idx, obj) {
                        console.log(obj.answer_text);
                        $("#answer_id_field").append($('<option></option>').attr('value', obj.id).text(obj.answer_text));
                    });
                },
                error: function(jqXHR, textStatus, errorThrown) {
                    console.log(errorThrown);
                    console.log(textStatus);
                    console.log(jqXHR);
                }
            }); 
        });
    })(django.jQuery);
});
