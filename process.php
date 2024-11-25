<?php
if ($_SERVER["REQUEST_METHOD"] == "GET") {
    $numbers = escapeshellarg($_GET['numbers']);
    $threshold = escapeshellarg($_GET['threshold']);

    $command = escapeshellcmd("python3 bitwise_operations.py $numbers $threshold");
    $output = shell_exec($command);

    echo "<h2>Results:</h2>";
    echo "<pre>$output</pre>";
} else {
    echo "Invalid Request";
}
?>