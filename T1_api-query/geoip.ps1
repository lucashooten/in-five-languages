$iparray = '192.30.255.113','8.8.8.8','1.1.1.1', '192.168.0.1'
$geoIP = @('')


foreach ($ip in $iparray)
{
    $response = Invoke-RestMethod ("https://freegeoip.app/json/",$ip -join '') -Method Get
    If ($response.latitude -eq 0) {
      continue
      }  Else {
      write-host $ip ":" $response.latitude
      $geoIP += $ip
      }
        
}

while($true) {
$userIP = Read-Host "Please enter an IP address"
try {
$validate = [IPAddress] $userIP
$geoIP += $userIP
break
}
  catch {
           'That isnt a valid IP. Try again'
}
}

write-host $userIP ":" $((Invoke-RestMethod ("https://freegeoip.app/json/",$userIP -join '') -Method Get).latitude)
''
'The following IPs were returned with location data: '
$geoIP



