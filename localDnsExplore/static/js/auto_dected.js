function auto_query(){
  console.log("query start")
    url      = $("#req_url").val()
    hostname = $("#hostname").val()
    req_url  = "http://"+url+"/query?hostname="+hostname+"&jsoncallback=?"
    var callback = function(data){
      eval(data);
      $("#client").text($_lanxun_cdn_servers.client);
      $("#localdns").text($_lanxun_cdn_servers.local_dns);
      $("#server").text($_lanxun_cdn_servers.edge_server);
      $("#commit_time").text($_lanxun_cdn_servers.commit_time);
    }
    $.getJSON(req_url).done(callback).fail(callback);
}
auto_query()
