const express = require("express");
const app = express();
const port = 8092;

app.get("/", (req, res) => {
  var req = require("request");

//   var options = {
//     method: "POST",
//     url: "http://api.weatherapi.com/v1/current.json",
//     headers: {
//       key: "95681db4987f4596a47172325221404",
//       "content-type": "application/x-www-form-urlencoded",
//     },
//     form: { origin: "501", destination: "114", weight: 1700, courier: "tiki" },
//   };

  var coba = "http://api.weatherapi.com/v1/current.json?key=95681db4987f4596a47172325221404&q=indonesia&aqi=yes"

  req(coba, function (error, response, body) {
    if (error) throw new Error(error);
    res.send(body);
    const data = response.data
    return JSON.stringify(data);

  });
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}!`)
  });

