const express = require('express')
const app = express()
const bodyParser = require('body-parser');
const cp = require("child_process");

app.use(bodyParser.json()); // for parsing application/json
app.use(bodyParser.urlencoded({ extended: true })); // for parsing application/x-www-form-urlencoded

app.get('/', function(req,res){
	res.send('listening');
})

app.post('/webhook', function (req, res) {
  console.log(req.body.data);
  switch(req.body.data){
  	case "test":
  		console.log("test was activated");
  		cp.exec("C:/WINDOWS/system32/mspaint.exe");
  		break;

  }
 
});

app.listen(7050, () => {
	console.log('Example app listening on port 7050!')
})