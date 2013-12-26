function auto_query(){
  var hostname = $("#hostname").val()
    var req_url  = $("#req_url").val()
    console.log(hostname)
    console.log(req_url)

    var callback = function(data){
      eval(data)
        $("#client").text($_lanxun_cdn_servers.client)
        $("#localdns").text($_lanxun_cdn_servers.local_dns)
        $("#server").text($_lanxun_cdn_servers.edge_server)
        $("#commit_time").text($_lanxun_cdn_servers.commit_time)
        spinner.stop()
    }
  $.getJSON("http://"+req_url+"/query?hostname="+hostname+"&jsonback=?").done(callback).fail(callback)
    start_spin()
}

function start_spin(){
  var opts = {
    lines: 15, // The number of lines to draw
    length: 20, // The length of each line
    width: 5, // The line thickness
    radius: 15, // The radius of the inner circle
    speed: 1, // Rounds per second
    trail: 60, // Afterglow percentage
    className: 'spinner', // The CSS class to assign to the spinner
    top: '55px', // Top position relative to parent in px
  };
  var target = document.getElementById('loading');
  spinner = new Spinner(opts).spin(target);
}

auto_query()
