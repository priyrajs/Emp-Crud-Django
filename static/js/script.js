$(document).ready( function (){
    $('#myTable').DataTable();
} );

$('document').ready(function() {
    //alert(target_url); 
    $('#msg-box').hide();
    $('.delete').on('click',function(){ 
        // alert("hiii"); 
        
        var action = $(this).text();
        var emp_id = $('.delete').attr('id');
        var target_url = "/delete_user";
        var csrf = $('input[name=csrfmiddlewaretoken]').val();
        var data = {action: action, emp_id:emp_id, csrfmiddlewaretoken: csrf}
        console.log(data)
        $.ajax( { 
            url: target_url, 
            type: "post", 
            data: data,
            // datatype: "text",
            success:function(response) {
                console.log(response)
                if (response.status == "deleted"){
                    $('#msg-box').show();
                    $('#msg').html("Deleted Emplyee !");
                    setTimeout(function() {
                        window.location.reload();
                    }, 2000);
                }
                else{
                    $('#msg-box').show();
                    $('#res').html("Couldn't Delete Employee"); 
                }
            } 
        }); 
    });

    $('.edit').on('click',function(){ 
        var action = $(this).text();
        var emp_id = $('.edit').attr('id');
        var target_url = "";
        var csrf = $('input[name=csrfmiddlewaretoken]').val();
        var data = {action: action, emp_id:emp_id, csrfmiddlewaretoken: csrf}
        console.log(data)
        $.ajax( { 
            url: target_url, 
            type: "get", 
            data: data,
            // datatype: "text",
            // success:function(response) {
            //     if (response.status == "deleted"){
            //         $('#res').show();
            //         setTimeout(function() {
            //             window.location.reload();
            //         }, 3000);
            //     }
            //     else{
            //         $('#res').html("Couldn't Delete Employee"); 
            //     }
            // } 
        }); 
    });

    $('.adduser').on('click',function(){ 
        var name = $('#name').val();
        var salary = $('#salary').val();
        var dept_id = $('#department').val();
        var target_url = "/adduser";
        var csrf = $('input[name=csrfmiddlewaretoken]').val();
        var edit_id = $('input[name=edit_id]').val();
        //alert(name,salary,dept_id);
        if( name == "" || salary == "" || dept_id == "")
        {
            $('#msg-box').show();
        	$('#msg').html("All the fields are required");
        }
        else
        {
            var data = {name: name, salary:salary, department:dept_id, edit_id:edit_id, csrfmiddlewaretoken: csrf}
            console.log(data)
            $.ajax( { 
                url: target_url, 
                type: "post", 
                data: data,
                // datatype: "text",
                success:function(response) {
                    console.log(response)
                    if (response.status == "added"){
                        $('#msg-box').show();
                        $('#msg').html("Added User !"); 
                        setTimeout(function() {
                            window.location = "/viewusers";
                        }, 2000);
                    }
                    else if (response.status == "updated"){
                        $('#msg-box').show();
                        $('#msg').html("Updated User !"); 
                        setTimeout(function() {
                            window.location = "/viewusers";
                        }, 2000);
                    }
                    else{
                        $('#msg-box').show();
                        $('#msg').html("Couldn't Add Employee"); 
                    }
                } 
            });
        } 
    });

    // function confirmDeleteModal(id){
    //     $('#deleteModal').modal();
    //     $('#deleteButton').html('<a class="btn btn-danger delete" onclick="deleteData('+id+')">Delete</a>');
    // }     
    // function deleteData(id){
    //   // do your stuffs with id
    //   $("#successMessage").html("Record With id "+id+" Deleted successfully!");
    //   $('#deleteModal').modal('hide'); // now close modal
    // }  

    //show selected dept in UI
    // var selected_dept = $('input[name=selected_dept]').val();
    // if (selected_dept != ""){
    //     $("#department").each(function()
    //     {
    //         console.log(selected_dept);
    //         alert($(this).text());
    //         if(selected_dept == $(this).text()){
    //             $(this).attr("selected","selected");
    //         }
    //     });
    // }

});