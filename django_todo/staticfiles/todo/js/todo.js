
$(document).ready(function() {


	// $('.done-button').click(function(){
	//     var taskid;
	//     taskid = $(this).parent().attr("task-id");
	//     taskcard = $(this).parent();
	//     $.ajax(
	//     {
	//         type:"POST",
	//         datatype:"json",
	//        	url: "/todo/toggle_complete/",
	//         data:{
	//                  task_id: taskid
	//         },
	//         success: function(data) 
	//         {
	//            taskcard.css({'display':'none'});
	//         }
	//      });
	//     return false;
	// });
	$('.datepicker').datepicker({
    format: 'mm/dd/yyyy',
    startDate: '1d'
	});

	function getCookie(name) {
	    var cookieValue = null;
	    if (document.cookie && document.cookie !== '') {
	        var cookies = document.cookie.split(';');
	        for (var i = 0; i < cookies.length; i++) {
	            var cookie = jQuery.trim(cookies[i]);
	            // Does this cookie string begin with the name we want?
	            if (cookie.substring(0, name.length + 1) === (name + '=')) {
	                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                break;
	            }
	        }
	    }
	    return cookieValue;
	}
	var csrftoken = getCookie('csrftoken');


	function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});


});