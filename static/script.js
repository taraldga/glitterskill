
var data;
$.ajax({
     url:"http://127.0.0.1:5000/data",
     dataType: 'json',
     success:function(data){
         var job = data.job;
         $('.title').append(job.title);
         $('.description').append(job.description);
         $('.date').append(job.date);
     },
     error:function(){
         alert("Error");
     }
});

