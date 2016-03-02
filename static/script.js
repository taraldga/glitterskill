
jQuery("#top-five").click(function(e){
//do something
    if($("#topfive").is(':hidden')){
        $('#topfive').show();
        $('#map-container').hide();
        $('#wordcloud').hide();
    }
    e.preventDefault();
});
jQuery("#heat-map").click(function(e){
    if($("#map-container").is(':hidden')){
        $('#map-container').show();
        $('#topfive').hide();
        $('#wordcloud').hide();
    }
    e.preventDefault();
});
jQuery("#word-cloud").click(function(e){
    if($("#wordcloud").is(':hidden')){
        $('#wordcloud').show();
        $('#map-container').hide();
        $('#topfive').hide();
    }
    e.preventDefault();
});


var data;
$.ajax({
     url:"http://127.0.0.1:5000/data",
     dataType: 'json',
     success:function(data){
        var job = data.job;
        $('.adid').append(job.adid);
        $('.title').append(job.title);
        $('.firm').append(job.firm);
        $('.deadline').append(job.deadline);
        $('.duration').append(job.duration);      
        $('.NOPosition').append(job.NOPosition);
        $('.industry').append(job.industry);
        $('.dateRelease').append(job.dateRelease);
        $('.jobFunction').append(job.jobFunction);
        $('.description').append(job.description);
        $('.skills').append(job.skills);
        $('.location').append(job.location);
     },
     error:function(){
         alert("Error");
     }
});

