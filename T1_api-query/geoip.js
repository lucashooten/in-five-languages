/* 

*/

const fetch = require('cross-fetch');
const iparray = ['192.30.255.113','8.8.8.8','1.1.1.1', '192.168.0.1'];
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output:process.stdout
});

function return_lat(ipaddress) {

        var requestOptions = {
            method: 'GET',
            redirect: 'follow'
        };

        fetch("https://freegeoip.app/json/"+ipaddress, requestOptions)
            .then(response => response.json())
            .then(data => {
                console.log(ipaddress+' : '+data.latitude)
            })
            .catch(error => console.log('error', error));

    }

function ask() {
    rl.question('Please enter an IP address: ', (answer) => {
        return_lat(answer);
    })
}


for (var i = 0; i < iparray.length; i++) {
    try {
        return_lat(iparray[i]);
        if (i == iparray.length)
    }
    catch (error) {
        console.log('all done')
        ask()
    }
}

