const express = require('express')
const app = express()
const bodyParser = require('body-parser');
const cp = require("child_process");
const jsonfile = require("jsonfile");

app.use(bodyParser.json()); // for parsing application/json
app.use(bodyParser.urlencoded({ extended: true })); // for parsing application/x-www-form-urlencoded

app.get('/', function(req,res){
	res.send('listening');
});

app.post('/webhook', function (req, res) {
  console.log(req.body.data);

  var file = 'data.json';
	jsonfile.readFile(file, function(err, obj) {
	  for(var i in obj){
	  	if(i == req.body.data){
	  		console.log("running ", obj[i]);
	  		cp.exec(obj[i]);
	  		return;
	  	}
	  }
	  console.log("not a command, add one?");
	});



  /*switch(req.body.data){
  	case "test":
  		console.log("test was activated");
  		cp.exec("C:/WINDOWS/system32/mspaint.exe");
  		break;
  	case "eokoStart":
  		console.log("eokoStart activated");
  		cp.exec("C:/Users/Dreality/Desktop/eokoStart.bat");
  }*/
 
});

app.listen(7050, () => {
	console.log('Example app listening on port 7050!')
});

