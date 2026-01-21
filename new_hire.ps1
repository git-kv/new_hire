# Scheduled to check a folder every minute to see if there is an
# account creation waiting to be processed.
$root_path = "\\eocservices\apps$\programs\scripts\new_hire\need_processing\"
$smtp_server = "exnode2.dartadvantage.com"
$from = "AccountCreation@dart.net"
$vip_recipients = "kvoelker@dart.net"
$default_recipients = "kvoelker@dart.net"
$Global:disable_account = $false

while ($true) {
    $ShouldCreate = Test-Path "$root_path*"

    if ($ShouldCreate){
        # Create account using CSV
        # Delete CSV after processing
    }

    Start-Sleep -s 60
}