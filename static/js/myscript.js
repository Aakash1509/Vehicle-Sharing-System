$('.minusbtn').click(function(){
    var id= $(this).attr("pid").toString();
    console.log("Aakash")
    // var eml = this.parentNode.children[2]
    $.ajax({
        type:"GET",
        url:"/minusvehicle",
        data:{
            seats: id
        },
        success:function(data){
            // console.log(data)
            // eml.innerText = data.seats
            document.getElementById("nov").innerText=data.seats
        }
    })
})